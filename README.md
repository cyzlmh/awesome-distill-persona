# awesome-distill-persona
<!-- Header -->
<div align="center">
  <img src="https://img.shields.io/badge/stars-🔥整活蒸馏人类-FF6B6B?style=for-the-badge" alt="Distill Humans"/>

  [简体中文](./README.md) · [English](./README_EN.md)

  *「与其等着被别人蒸，不如先蒸自己。」*

  <!-- SHIELD -->
  [![Stars](https://img.shields.io/github/stars/cyzlmh/awesome-distill-persona?style=for-the-badge&color=FF6B6B)](https://github.com/cyzlmh/awesome-distill-persona/stargazers)
  [![Forks](https://img.shields.io/github/forks/cyzlmh/awesome-distill-persona?style=for-the-badge&color=4ECDC4)](https://github.com/cyzlmh/awesome-distill-persona/network/members)
  [![License](https://img.shields.io/badge/License-MIT-FFE66D?style=for-the-badge)](./LICENSE)
  <!-- TOC -->
  > 🔗 Last updated: 2026-04-04 | 数据来源: GitHub API

  ---

  ### 📌 什么是「蒸馏人类」？

  把一个人的**聊天记录 + 工作文档 + 性格标签**，喂给 AI，出来一个会按 TA 的方式说话、判断、协作的 AI Skill。

  不是复制粘贴，是真的理解——TA 怎么说话、怎么想、在乎什么。

  ---

  ## 📂 目录

  [🧑‍💻 按角色分类](#-按角色分类) ·
  [⚙️ 技术框架](#️-技术框架) ·
  [📡 数据采集器](#-数据采集器) ·
  [📰 媒体报道](#-媒体报道) ·
  [🤝 投稿指南](./CONTRIBUTING.md)

  ---
</div>

## 🧑‍💻 按角色分类

### 整活系列（一句话的事，认真的技术）

| 项目 | 角色 | ⭐ Stars | 数据源 | 特点 | 仓库 |
|------|------|:--------:|--------|------|------|
| **同事.skill** | 跑路的同事 | 6,802 | 飞书/钉钉/邮件/文档 | 把同事的技能与性格蒸馏成 AI Skill，让它替他工作 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) |
| **前任.skill** | 离开的她/他 | 2,239 | 微信/照片/社交媒体 | 将回忆蒸馏成 Skill，不是为了挽回，是为了记住 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) |
| **前女友.skill** | 前女友（细分版） | 362 | 微信/iMessage/微博/小红书 | 5层性格结构 + 依恋类型 + 吵架模式分析 | [perkfly/ex-skill](https://github.com/perkfly/ex-skill) |
| **自己.skill** | 你自己 | 395 | 微信/文档/照片 | 与其被别人蒸，不如先蒸馏自己 | [notdog1998/yourself-skill](https://github.com/notdog1998/yourself-skill) |
| **senpai-skill** | 大师兄/师姐 | 35 | 文档/聊天记录 | 把前辈经验蒸馏成可复用的 skill | [zhanghaichao520/senpai-skill](https://github.com/zhanghaichao520/senpai-skill) |
| **华夏老祖宗.skill** | 华夏智囊全家桶 | 87 | 公开资料 | 华夏老祖宗智慧蒸馏 | [liangjfblue/huaxia-wisdom](https://github.com/liangjfblue/huaxia-wisdom) |

### 打工人系列（整活外壳，打工人保护内核）

| 项目 | 角色 | ⭐ Stars | 特点 | 仓库 |
|------|------|:--------:|------|------|
| **反蒸馏.skill** | 打工人的反制 | 543 | 公司逼写 skill？洗掉核心知识再交差，格式保留、精华留给自己 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) |
| **老板.skill** | PUA 来源 | 35 | PUA检测(10大厂流派) · 反击教练(三档话术) · 画饼鉴定 · 翻车模拟文字游戏 | [nicepkg/boss-skill](https://github.com/nicepkg/boss-skill) |
| **导师.skill** | 退休导师 | 56 | 把导师蒸馏成随时可问的 AI Skill | [ybq22/supervisor](https://github.com/ybq22/supervisor) |

---

## ⚙️ 技术框架

通用蒸馏框架，不绑定特定角色，可蒸馏任何人。

| 项目 | ⭐ Stars | 说明 | 仓库 |
|------|:--------:|------|------|
| **immortal-skill** ♾️ | 190 | 开源数字永生框架，从聊天记录蒸馏任何人的七维数字分身。支持 12+ 平台，7种角色模板，对齐 OpenClaw Soul Spec 标准 | [agenmod/immortal-skill](https://github.com/agenmod/immortal-skill) |
| **WeClone** | 125 | 微信数字分身，从微信聊天记录蒸馏个人数字形象 | [ooyinet/WeClone](https://github.com/ooyinet/WeClone) |

---

## 📡 数据采集器

| 平台 | 采集方式 | 说明 |
|------|---------|------|
| **微信** | WechatExporter 等工具导出 | 聊天记录 |
| **飞书** | API / 浏览器 / MCP | 消息 + 文档 |
| **钉钉** | 导出工具 | 消息 |
| **iMessage** | macOS chat.db | 聊天记录 |
| **Twitter / X** | API 抓取 | 公开推文 |
| **微博** | JSON/HTML 导出 | 社交媒体 |
| **小红书** | JSON 导出 | 笔记 + 评论 |
| **豆瓣** | JSON/HTML 导出 | 广播 + 日记 |
| **Instagram** | JSON 导出 | 帖子 |

> 📖 详见各项目文档，部分平台需要用户自行导出数据。

---

## 📰 媒体报道

| 媒体 | 标题 | 日期 |
|------|------|------|
| 36氪 | [同事、老板、前任皆成Skill：人类正被重新定价](https://eu.36kr.com/zh/p/3750265177899778) | 2026-04-03 |
| SunAI | [我去 GitHub 翻了一圈，发现大家已经开始把同事、前任、老师，甚至老祖宗做成 Skill 了](https://www.sunai.net/t/topic/1372) | 2026-03 |

---

## 🤝 投稿指南

欢迎补充新项目！请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。

**收录标准：**
- 必须是公开可访问的 GitHub 仓库
- 项目与「蒸馏人类」主题相关（整活 or 严肃均可）
- 至少是可运行的代码/文档，不是空壳项目
- 提交 PR 时请附上 Stars 数和简短介绍

---

## ⚠️ 免责声明

- 蒸馏他人前请务必获得**本人知情同意**
- 本列表仅供技术研究与娱乐参考
- 禁止用于任何侵犯隐私或违法用途
- 「整活有度，永生有道」

---

<div align="center">

  *与其等着被别人蒸，不如先蒸自己。*

  [![Stars](https://img.shields.io/github/stars/cyzlmh/awesome-distill-persona?style=social&color=FF6B6B)](https://github.com/cyzlmh/awesome-distill-persona/stargazers)

</div>
