#!/usr/bin/env python3
"""
fetch-stars.py — 自动抓取 awesome-distill-persona 列表中所有项目的 GitHub Stars 数
Usage: python fetch-stars.py
"""

import subprocess
import re

REPOS = [
    "titanwings/colleague-skill",
    "therealXiaomanChu/ex-skill",
    "perkfly/ex-skill",
    "notdog1998/yourself-skill",
    "leilei926524-tech/anti-distill",
    "agenmod/immortal-skill",
    "ooyinet/WeClone",
    "liangjfblue/huaxia-wisdom",
    "ybq22/supervisor",
    "nicepkg/boss-skill",
    "zhanghaichao520/senpai-skill",
]


def get_stars(repo: str) -> int:
    """使用 gh CLI 获取 stars"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}", "--jq", ".stargazers_count"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return int(result.stdout.strip())
    except Exception:
        pass
    return 0


def main():
    print(f"{'Repository':<45} | {'Stars':>8}")
    print("-" * 58)
    for repo in REPOS:
        stars = get_stars(repo)
        print(f"{repo:<45} | {stars:>8,}⭐")
    print("-" * 58)
    print("数据来源: GitHub API | 请复制最新 Stars 数到 README.md")


if __name__ == "__main__":
    main()
