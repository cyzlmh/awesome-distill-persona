# 🤝 投稿指南

欢迎为 awesome-distill-persona 贡献内容！

## 收录标准

✅ **接受的投稿：**
- 公开可访问的 GitHub 仓库
- 与「蒸馏人类 / 数字分身 / persona 提取」主题相关（整活 or 严肃均可）
- 至少是可运行的代码或文档，不是空壳项目
- 收录时附上：项目名、仓库链接、Stars 数、简短描述

⚠️ **不接受的投稿：**
- 纯付费/闭源项目
- 空壳仓库或长期不维护的项目（>1年无更新）
- 与主题无关的内容

## 如何投稿

### 方式一：提交 Pull Request（推荐）

1. Fork 本仓库
2. 在 `README.md` 中找到对应分类，添加你的项目
3. 更新 Stars 数据（可用 `scripts/fetch-stars.py` 自动更新）
4. 提交 PR，标题格式：`feat: 添加 <项目名>`
5. 等待 maintainer 审核

### 方式二：提交 Issue

在 [Issue 页面](https://github.com/cyzlmh/awesome-distill-persona/issues/new/choose) 提交「📝 添加项目」类型的 Issue，格式如下：

```
## 项目名称
[项目名]

## GitHub 仓库
https://github.com/xxx/xxx

## Stars 数（可选）
xxx

## 项目简介
一句话介绍这个项目是做什么的

## 收录分类
- [ ] 整活系列
- [ ] 打工人系列
- [ ] 技术框架
- [ ] 数据采集器
```

## 分类说明

| 分类 | 说明 |
|------|------|
| **整活系列** | 一句话的事，认真的技术。如同事.skill、前任.skill、自己.skill |
| **打工人系列** | 整活外壳，打工人保护内核。如老板.skill、反蒸馏.skill |
| **技术框架** | 通用蒸馏框架，不绑定特定角色 |
| **数据采集器** | 特定平台的数据采集工具或方法 |

## 自动更新 Stars

可以使用 `scripts/fetch-stars.py` 自动抓取所有项目的最新 Stars 数：

```bash
cd scripts
pip install requests
python fetch-stars.py
```

## 免责声明

- 蒸馏他人前请务必获得**本人知情同意**
- 本列表仅供技术研究与娱乐参考
- 禁止用于任何侵犯隐私或违法用途
- 「整活有度，永生有道」

---

感谢你的贡献！🙏
