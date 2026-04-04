#!/usr/bin/env python3
"""
update-readme-stars.py — 自动更新 README.md 中的 Stars 数据
Usage: python update-readme-stars.py

依赖: pip install requests
需要: gh CLI 已登录 (gh auth login)
"""

import subprocess
import re
import sys
from datetime import datetime
from pathlib import Path

# 需要追踪的仓库列表（格式：owner/repo → markdown中的简称）
REPOS = {
    "titanwings/colleague-skill":    "titanwings/colleague-skill",
    "therealXiaomanChu/ex-skill":     "therealXiaomanChu/ex-skill",
    "perkfly/ex-skill":               "perkfly/ex-skill",
    "notdog1998/yourself-skill":     "notdog1998/yourself-skill",
    "leilei926524-tech/anti-distill": "leilei926524-tech/anti-distill",
    "agenmod/immortal-skill":         "agenmod/immortal-skill",
    "ooyinet/WeClone":                "ooyinet/WeClone",
    "liangjfblue/huaxia-wisdom":      "liangjfblue/huaxia-wisdom",
    "ybq22/supervisor":                "ybq22/supervisor",
    "nicepkg/boss-skill":             "nicepkg/boss-skill",
    "zhanghaichao520/senpai-skill":   "zhanghaichao520/senpai-skill",
}

# README 中的 Markdown 表格行匹配（GitHub Flavored Markdown 表格格式）
# 匹配形如: | xxx | repo | 123 | ... | [link](url) |
# 重点是捕获 Stars 列（第3列）和仓库名列（第2列）的组合
REPO_PATTERN = re.compile(
    r'(\|\s*)([^\|]+?)(\s*\|\s*)'          # 第1列（项目名）
    r'([^\|]+?\s*\|\s*)'                   # 第2列（角色）
    r'(\s*)(\d{1,6})\s*(\|)'               # 第3列（Stars，需要替换）
    r'(.*?)'                               # 剩余列
    rf'(https://github\.com/{re.escape(r"|".join(REPOS.keys()))})',
    re.IGNORECASE | re.DOTALL
)


def get_stars(repo: str) -> int:
    """使用 gh CLI 获取仓库 stars"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}", "--jq", ".stargazers_count"],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            return int(result.stdout.strip())
    except Exception as e:
        print(f"  ⚠️  获取 {repo} 失败: {e}", file=sys.stderr)
    return 0


def main():
    readme_path = Path(__file__).parent.parent / "README.md"
    readme_en_path = Path(__file__).parent.parent / "README_EN.md"

    for path in [readme_path, readme_en_path]:
        if not path.exists():
            print(f"⚠️  跳过不存在的文件: {path}")
            continue

        content = path.read_text(encoding="utf-8")
        new_content = content
        changed = False

        for repo, repo_key in REPOS.items():
            stars = get_stars(repo)
            print(f"  {repo:<45} → {stars:>6,} ⭐")

            # 在 README 中搜索该 repo 的链接所在的表格行
            # 找到 [owner/repo](https://github.com/owner/repo) 所在的行
            link_pattern = re.compile(
                rf'^(\|.*?)(https://github\.com/{re.escape(repo)}(?:\s|\?|/|#|$).*?)(\|.*?)$',
                re.MULTILINE | re.IGNORECASE
            )

            def replace_stars(m):
                row_start = m.group(1)
                row_end = m.group(3)

                # 从该行中找出 Stars 列（第三个 | 分隔的字段）
                # 格式: | col1 | col2 | **123** | col4 | ... | [link] |
                # 我们在 col3 位置替换数字
                parts = row_start.rstrip('|').split('|')
                if len(parts) >= 3:
                    # parts[-1] 是第3列内容，可能是 "123" 或 "**123**⭐"
                    col3 = parts[-1]
                    # 提取其中的数字
                    num_match = re.search(r'\d+', col3)
                    if num_match:
                        old_num = int(num_match.group())
                        if old_num != stars:
                            new_col3 = col3[:num_match.start()] + str(stars) + col3[num_match.end():]
                            parts[-1] = new_col3
                            changed = True
                            return '|' + '|'.join(parts) + row_end
                return m.group(0)

            new_content = link_pattern.sub(replace_stars, new_content)

        # 更新 "Last updated" 时间戳
        today = datetime.now().strftime("%Y-%m-%d")
        new_content = re.sub(
            r'(Last updated:)\s*\d{4}-\d{2}-\d{2}',
            f'\\1 {today}',
            new_content
        )

        if changed or new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  ✅ 已更新: {path.name}")
        else:
            print(f"  ➖ 无变化: {path.name}")

    print(f"\n🎉 完成！变更已写入文件，请检查并提交。")


if __name__ == "__main__":
    print(f"🚀 开始抓取 Stars 数据 ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n")
    main()
