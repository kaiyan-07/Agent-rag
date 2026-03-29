# Nanobot + Local RAG 学习助手（QQ Bot）

## 项目简介

本项目是一个基于 nanobot 的超轻量级个人 AI 学习助手，结合本地 RAG 系统与 QQ 机器人，实现一个可对话、可扩展的智能学习工具。

系统支持在聊天过程中自动调用本地知识库，帮助用户完成算法题理解、知识点分析与学习路径规划。

👉 QQ 对话示例：
<p align="center">
  <img src="https://github.com/user-attachments/assets/c920b0b3-837e-4d6e-b19b-f349d6fe2c3a" width="350"/>
</p>

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

<img width="960" height="283" alt="截屏2026-03-30 04 23 20" src="https://github.com/user-attachments/assets/8831ce70-4810-480f-ad21-778038892a35" />


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
调用rag VS 不调用rag：

<p align="center">
  <img src="https://github.com/user-attachments/assets/f577dbbb-9dde-487c-906a-00697b62120f" width="300"/>
  <img src="https://github.com/user-attachments/assets/9edac14c-3646-4d3e-9e31-8ee5620da5ed" width="300"/>
</p>
---

### 3. QQ 机器人对话

接入 QQ Bot，实现真实对话场景：

* 支持私聊问答
* 实时交互

<p align="center">
  <img src="https://github.com/user-attachments/assets/7a5976c1-ea23-495b-81da-cf739222a8f9" width="400"/>
</p>
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

## 设计说明（Tool 调用验证机制）

为了确保 Agent 实际调用了本地 RAG，而不是基于大模型进行推测（hallucination），本项目在 RAG 服务层返回结果中加入了：

* `source`：标识结果来源（如 LOCAL_RAG_API）
* `trace_id`：唯一请求标识（用于追踪调用链路）

Agent 在输出中必须包含这些字段，从而实现：

* Tool 调用可验证
* 防止伪造结果
* 提高系统可解释性

<img width="638" height="325" alt="截屏2026-03-30 04 28 49" src="https://github.com/user-attachments/assets/f0a6ab0c-6179-4f6e-b7e7-bf6994040943" />

---

## Agent 工具执行能力

基于 nanobot 的工具机制，Agent 具备基础系统操作能力，包括：

* 执行本地脚本（Python / Shell）
* 创建 / 修改 / 删除文件
* 调用外部工具（通过 exec）

该能力使系统不仅限于问答，还具备扩展为：

* 自动任务执行 Agent
* 本地自动化助手
* 多工具协作系统

👉 当前项目主要聚焦于 RAG 学习场景，但已具备扩展为通用 Agent 的基础能力。
<p align="center">
  <img src="https://github.com/user-attachments/assets/05e7cfdc-e74a-4401-b221-d48054ecee4f" width="300"/>
  <img src="https://github.com/user-attachments/assets/3e12c316-adef-4195-be74-9ca1bc9cd7fc" width="300"/>
   <img src="https://github.com/user-attachments/assets/38cf3cc9-6b5e-453a-8d35-14684a46a7df" width="300"/>
</p>
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

* 可全程本地部署（无外部依赖）
* Agent + Tool 架构
* RAG 解耦设计（HTTP）
* 支持真实 IM 场景（QQ）
* 可扩展为通用 Agent 系统

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
