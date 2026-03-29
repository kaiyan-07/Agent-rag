# Nanobot + Local RAG 学习助手（QQ Bot）

## 项目简介

本项目是一个基于 nanobot 的超轻量级个人 AI 学习助手，结合本地 RAG 系统与 QQ 机器人，实现一个可对话、可扩展的智能学习工具。

系统支持在聊天过程中自动调用本地知识库，帮助用户完成算法题理解、知识点分析与学习路径规划。

---

## 核心功能

### 1. 本地 RAG 学习助手

接入本地 RAG 项目：

👉 https://github.com/kaiyan-07/Study_assistant

该 RAG 系统基于 RAG（Retrieval-Augmented Generation）架构构建，主要用于算法学习辅助：

* 输入题意描述 → 匹配 LeetCode Hot100 相似题目
* 自动分析：

  * 知识点
  * 解题思路
  * 推荐练习路径
* 支持：

  * 题目查询
  * 分类推荐
  * 错题统计

整个系统采用本地部署（FAISS + 本地 LLM），不依赖外部 API。

---

### 2. Agent + Tool 调用（核心设计）

本项目通过 Agent 实现：

* 自动解析用户输入
* 判断是否调用 RAG
* 调用本地工具（HTTP / Python）
* 返回结构化结果

用户可以通过前缀触发 RAG：

```text
[USE_RAG] 给定数组找三个数之和等于0
```

---

### 3. QQ 机器人对话

接入 QQ Bot，实现真实对话场景：

* 支持私聊问答
* 实时交互

---

### 4. 模型切换（灵活扩展）

支持通过配置切换模型，例如：

* DeepSeek
* Ollama 本地模型（如 llama3）

只需修改：

```json
"model": "YOUR_MODEL"
```

即可完成切换。

---

### 5. 个性化学习助手

系统不仅是聊天机器人，还具备：

* 个人知识库问答（RAG）
* 学习路径建议
* 错题复盘辅助
* 可扩展定时提醒（学习任务）

👉 本质是一个“可扩展的个人学习 Agent”。

---

## 系统架构

```text
QQ 用户
   ↓
Nanobot Agent（决策 + Tool Routing）
   ↓
rag_http_query.py（工具层）
   ↓
RAG FastAPI（/ask）
   ↓
FAISS + 本地 LLM
```

---

## 运行方式

### 1. 克隆项目

```bash
git clone https://github.com/HKUDS/nanobot.git
git clone https://github.com/kaiyan-07/Study_assistant
```

---

### 2. 启动 RAG 服务

```bash
uvicorn api.app:app --reload
```

默认地址：

```
http://127.0.0.1:8000/ask
```

---

### 3. 初始化 nanobot

```bash
nanobot onboard
```

---

### 4. 配置 (~/.nanobot/config.json)

#### 设置 API Key

```json
{
  "providers": {
    "deepseek": {
      "apiKey": "YOUR_API_KEY"
    }
  }
}
```

---

#### 设置模型（支持切换）

```json
{
  "agents": {
    "defaults": {
      "model": "YOUR_MODEL",
      "provider": "auto"
    }
  }
}
```

---

### 5. 启动 Agent

```bash
nanobot agent
```

---

## QQ Bot 配置

### 1. 创建机器人

* 登录 QQ 开放平台
* 创建 Bot 应用
* 获取：

  * AppID
  * AppSecret

---

### 2. 沙箱测试

* 添加自己为测试用户
* 扫码进入机器人
* 开始对话

---

### 3. 配置 nanobot

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "YOUR_APP_ID",
      "secret": "YOUR_APP_SECRET",
      "allowFrom": ["YOUR_OPENID"],
      "msgFormat": "plain"
    }
  }
}
```

---

### 4. 启动网关

```bash
nanobot gateway
```

---

## 使用示例

在 QQ 中发送：

```text
[USE_RAG] 给定数组找三个数之和等于0
```

系统将：

* 调用本地 RAG
* 返回最相似题目
* 输出知识点与建议

---

## 项目特点

* 本地部署（无外部依赖）
* Agent + Tool 架构
* RAG 解耦设计（HTTP）
* 可扩展多工具系统
* 支持真实 IM 场景（QQ）

---

## 总结

本项目实现了一个完整的 AI 应用链路：

> Agent（决策） + Tool（调用） + RAG（知识） + IM（交互）

适用于：

* AI 应用开发学习
* Agent 系统实践
* RAG 项目扩展
* 个性化学习助手

---
