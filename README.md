# 💰 个人记账本
#记账用的

基于 **Python + Streamlit + SQLite3** 的 Web 记账工具，纯 Python 实现，无需前端知识，开箱即用。

## ✨ 功能

- **➕ 添加账目** — 填写金额、分类、日期、备注，一键记录
- **📋 账目列表** — 按月份和分类筛选，表格展示所有记录
- **🗑️ 删除账目** — 输入 ID 删除错误/过期记录
- **📊 分类统计** — 柱状图 + 统计表（笔数、总额、占比）

## 🖼️ 界面预览

```
┌──────────────────────────────────────────────┐
│  💰 个人记账本                                │
│ ┌────────────┬──────────────────────────────┐ │
│ │ 🔍 全局筛选 │  ➕添加 │ 📋列表 │ 🗑️删除 │ 📊统计 │ │
│ │  月份选择   │                               │ │
│ │  分类多选   │      [当前标签页内容]           │ │
│ └────────────┴──────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

## 🚀 快速开始

### 环境要求

- Python 3.8+

### 安装 & 运行

```bash
# 1. 克隆项目
git clone https://github.com/< foshanhaoshimin >/bookkeeping.git
cd bookkeeping

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动应用
streamlit run app.py
```

浏览器访问 **http://localhost:8501** 即可使用。

## 📁 项目结构

```
记账/
├── app.py              # 主入口：页面配置 + 侧边栏筛选 + 标签页布局
├── config.py           # 常量：6 个预设分类、数据库路径
├── database.py         # 数据层：建表、增删查、统计查询（纯 SQLite3）
├── ui/                 # UI 层 — 每个标签页一个文件
│   ├── __init__.py     # 包初始化
│   ├── add.py          # ➕ 添加账目表单
│   ├── list_view.py    # 📋 账目列表 + 表格展示
│   ├── delete.py       # 🗑️ 按 ID 删除
│   └── stats.py        # 📊 分类统计（柱状图 + 统计表）
├── requirements.txt    # 依赖清单
├── .gitignore
├── CLAUDE.md           # Claude Code 项目说明
└── README.md
```

## 🗄️ 数据库

单表 `transactions`：

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 自增主键 |
| amount | REAL | 金额 |
| category | TEXT | 分类 |
| date | TEXT | 日期 (YYYY-MM-DD) |
| note | TEXT | 备注 |

6 个预设分类：`餐饮` `交通` `购物` `娱乐` `居住` `其他`

## 🧱 架构设计

```
用户操作 → ui/*.py → database.py → SQLite (data.db)
                  ↑
app.py（侧边栏筛选）→ ui/list_view.py → database.py → 表格渲染
```

- **config.py** — 所有常量集中管理，修改分类/路径只需改一处
- **database.py** — 全部 SQL 操作封装为函数，UI 层不直接写 SQL
- **ui/\*.py** — 每个标签页独立模块，暴露统一的 `render()` 函数
- **app.py** — 薄入口，只做布局串联，不包含业务逻辑

## 📄 License

MIT
