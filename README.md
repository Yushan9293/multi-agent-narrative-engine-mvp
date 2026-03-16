# 多 Agent 剧本生成协作骨架（MVP）

## 项目简介

这是一个用于短剧 / 漫剧剧本生成的多 Agent 协作骨架项目。

当前目标不是做完整成品，而是先搭建清晰、可扩展的最小工程结构，包括：

- Router：负责总调度
- Global State / Schema：负责状态流转
- Agent1 ~ Agent5：按职责拆分的独立模块

这个版本主要用于团队内部对齐方向，并为后续多人协作开发预留清晰边界。

---

## 当前结构

- `main.py`
  - 最小运行入口
  - 当前用于演示 Agent1 的输出结果

- `src/router.py`
  - Router 总调度器
  - 当前支持只运行到 Agent1 的最小演示链路

- `src/models.py`
  - 使用 `pydantic` 定义全局状态和最小数据结构
  - 包括 `StoryElements`、`PipelineState` 等核心模型

- `src/agents/agent1_extractor.py`
  - Agent1：灵感提取 Agent
  - 当前已具备最小可运行能力
  - 当前输出以“灵感拆解”为主，聚焦六大核心要素与缺失要素识别

- `src/agents/agent2_generator.py`
  - Agent2：梗概生成 Agent
  - 当前为骨架预留

- `src/agents/agent3_rhythm.py`
  - Agent3：节奏 Agent
  - 当前为骨架预留

- `src/agents/agent4_mapping.py`
  - Agent4：映射 Agent
  - 当前为骨架预留

- `src/agents/agent5_writer.py`
  - Agent5：撰写 Agent
  - 当前为骨架预留

- `src/prompts/`
  - 各 Agent 对应的 prompt 草稿文件
  - 当前主要作为后续接入模型时的占位

---

## 当前已完成

- 多 Agent 主链路骨架已搭建
- Router / State / Agent 的边界已拆分清楚
- Agent1（灵感提取 Agent）已经可以最小运行
- 输入一段故事灵感后，可以输出结构化 `StoryElements`
- Agent1 当前会将灵感拆解为六大核心要素：
  - 外在目标与内在缺陷
  - 核心反派力量
  - 核心赌注
  - 关键设定与道具
  - 核心困境主题
  - 黄金开局点
- Agent1 同时会给出缺失要素提示，便于后续补全或接入 HITL
- Agent1 的结果已经可以写入 `PipelineState`
- `main.py` 可以直接运行，用于内部演示当前阶段能力

---

## 当前运行方式

建议先进入项目目录并使用虚拟环境运行。

### 1. 创建并激活虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. 安装最小依赖

```bash
pip install pydantic
```

### 3. 运行演示

```bash
python main.py
```

运行后，终端会打印：

- 原始用户输入
- Agent1 输出的“灵感拆解结果”
- 六大核心要素与缺失要素提示
- 写入结果后的 `PipelineState`

---

## 当前演示范围

当前版本只演示 Agent1 的最小可运行能力，不代表完整剧本生成流程已经完成。

当前可展示的是：

- 用户输入一段故事灵感
- Router 调用 Agent1
- Agent1 将灵感拆解为六大核心要素与缺失要素
- 结果成功挂载到全局状态中

---

## 后续开发方向

后续可在当前骨架基础上继续推进：

- 完善 Agent2：基于 `StoryElements` 生成多个梗概候选
- 完善 Agent3：将已选梗概转成 beats / 节奏表
- 完善 Agent4：将节奏表映射为分集大纲
- 完善 Agent5：根据分集大纲生成剧本正文
- 将各 Agent 的 mock 输出逐步替换为真实模型调用
- 完善 Router 的主链路控制、选择策略和错误处理

---

## 当前定位说明

这是一个 **最小工程骨架（MVP）**，重点在于：

- 主链路清晰
- 模块边界清楚
- 方便后续多人协作
- 便于逐步替换 mock 为真实能力

当前版本不包含：

- 真实 LLM / API 接入
- 前端界面
- 数据库
- 工作流框架
- 复杂调度与评估系统

---

## 适合的协作拆分

按当前结构，后续可以比较自然地分工：

- 一人负责 Router / State 演进
- 一人负责 Agent1 / Agent2 原型
- 一人负责 Agent3 / Agent4 结构设计
- 一人负责 Agent5 剧本正文生成
- 一人负责 prompts 与后续模型接入

---

## 说明

当前 README 面向团队内部快速同步，重点是说明项目现状、可运行范围与后续开发接口，不作为正式产品文档使用。
