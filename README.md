# 需求评审自动化工具

## 概述
本项目是一个基于大语言模型的软件需求评审系统，专为航空电子设备开发设计。通过支持 OpenAI 的大模型接口，实现按照检查单要求对航空软件需求的自动化合规性检查，并输出对应的评审结果。

## 功能特性
✅ **核心能力**
- 自动化DO-178C A级标准合规性检查 
- 支持多维度评审指标统计（通过/失败/不确定等） 
- 实时进度监控与ETA预测 
- 结果可视化输出（Excel格式） 

## 环境要求
- Python 3.7+
- pandas
- openai
- openpyxl
- httpx
- python-dotenv

## 安装依赖
```bash
pip install pandas openai openpyxl httpx
```

## 文件结构
```
AutoReqReview/
├── requirements.xlsx           # 待评审的需求文档（需含指定字段）
├── 接口需求集合/
│   └── CREATE_MUTEX.xlsx      # 接口需求文档示例
├── checklist.txt              # LLM评审检查单
├── prompt.txt                 # LLM评审提示模板（单个需求）
├── prompt_batch.txt           # LLM评审提示模板（批量接口评审）
├── reviewer.py                # 单个需求评审程序
├── reviewer_batch.py          # 批量接口评审程序
├── create_sample_data.py      # 创建示例数据的脚本
├── requirements.txt           # Python依赖列表
└── README.md                  # 本文档
```

## 快速启动

### 🚀 一键启动（推荐）
```bash
# 1. 项目初始化（首次使用）
python main.py setup

# 2. 测试配置
python main.py test

# 3. 运行评审
python main.py single   # 单个需求评审
python main.py batch    # 批量接口评审
```

### 📋 详细步骤

### Step 1: 准备环境
```bash
# 克隆项目或下载文件
cd AutoReqReview

# 安装依赖
pip install -r requirements.txt
```

### Step 2: 创建示例数据（可选）
```bash
python create_sample_data.py
```

### Step 3: 配置大模型API
本工具支持 OpenAI 和 DeepSeek 两种大模型，通过 `.env` 文件进行配置：

1. **复制并编辑配置文件**：
```bash
# .env 文件内容
# 模型提供商选择：'openai' 或 'deepseek'
MODEL_PROVIDER=deepseek

# OpenAI 配置
OPENAI_API=your_openai_api_key_here
OPENAI_URL=https://api.openai.com/v1

# DeepSeek 配置
DEEPSEEK_API=your_deepseek_api_key_here
DEEPSEEK_URL=https://api.deepseek.com/v1
```

2. **测试配置**：
```bash
python test_config.py
```

### Step 4: 准备输入文件

#### 4.1 需求文件格式
待分析的需求需要保存为Excel文件，包含以下字段：
- 标识
- 标题
- 版本信息
- 需求类型
- 是否派生的需求
- 派生理由
- 接口原型
- 需求描述
- 测试建议
- 注释
- 作者

#### 4.2 检查单文件
`checklist.txt` 包含基于DO-178C标准的检查条目，格式如：
```
**CHKI_17**
- **编号**: CHKI_17  
- **检查项**: [SRD] 需求条目是否只包含一个"应"？  
- **适用性**: 必须遵守  
```

### Step 5: 运行评审

#### 单个需求评审
```bash
python reviewer.py
```
- 输入：`requirements.xlsx`
- 输出：`评审结果-cot.xlsx`

#### 批量接口评审
```bash
python reviewer_batch.py
```
- 输入：`接口需求集合/` 目录下的所有Excel文件
- 输出：`评审结果/` 目录下的评审结果和汇总

## 输出结果

### 单个需求评审结果
包含以下字段：
- 标识
- 作者
- 失败（数量）
- 不确定（数量）
- 不适用（数量）
- 通过（数量）
- 额外问题（数量）
- 评审结果（详细文本）

### 批量接口评审结果
- 每个接口生成单独的评审结果文件
- 生成接口评审汇总文件
- 详细的日志文件记录处理过程

## 配置说明

### 支持的大模型
本工具支持以下大模型：

#### OpenAI 模型
- **gpt-4o** (默认)：最新的GPT-4 Omni模型，性能强大
- **gpt-4**：标准GPT-4模型
- **gpt-3.5-turbo**：高性价比选择

#### DeepSeek 模型
- **deepseek-reasoner** (默认)：DeepSeek推理模型，逻辑分析能力强
- **deepseek-chat**：通用对话模型
- **deepseek-coder**：代码专用模型

### 模型配置
在 `.env` 文件中配置：
```bash
# 选择提供商
MODEL_PROVIDER=deepseek  # 或 openai

# 可选：指定具体模型
DEEPSEEK_MODEL=deepseek-reasoner
OPENAI_MODEL=gpt-4o
```

### 参数调整
默认参数在 `model_config.py` 中设置：
```python
max_tokens=10000,    # 最大输出长度
temperature=0.7,     # 创造性参数（0-1）
```

## 使用注意事项

1. **文件格式**：确保Excel文件包含所有必需字段
2. **API配置**：正确配置工号和API地址
3. **网络连接**：确保能访问星云大模型服务
4. **文件权限**：确保输出目录有写入权限
5. **资源使用**：大批量处理时注意API调用频率限制

## 故障排除

### 常见问题
1. **文件读取错误**：检查Excel文件格式和字段名称
2. **API调用失败**：检查网络连接和API配置
3. **权限错误**：确保有文件写入权限
4. **依赖包缺失**：重新安装所需依赖

### 日志文件
- `review_log.txt`：单个需求评审日志
- `评审结果/评审总日志.txt`：批量评审总日志
- `评审结果/评审日志-[接口名].txt`：各接口详细日志

## 开发说明

### 扩展检查单
编辑 `checklist.txt` 添加新的检查条目

### 自定义提示词
- 修改 `prompt.txt` 调整单个需求评审逻辑
- 修改 `prompt_batch.txt` 调整批量评审逻辑

### 结果处理
可根据需要修改结果统计和输出格式

## 技术支持
如遇问题，请检查：
1. 依赖包版本兼容性
2. 文件格式规范性
3. API服务可用性
4. 系统资源充足性

---
*更新时间：2025年8月31日*
