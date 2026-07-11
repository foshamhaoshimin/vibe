"""
记账工具 — 主入口
"""
from datetime import date

import streamlit as st

from config import CATEGORIES
from database import init_db, get_available_months
from ui import add, list_view, delete, stats

# ============================================================
# 页面配置
# ============================================================
st.set_page_config(page_title="记账工具", page_icon="💰", layout="wide")
st.title("💰 个人记账本")

# ============================================================
# 初始化数据库
# ============================================================
init_db()

# ============================================================
# 侧边栏 — 全局筛选条件
# ============================================================
st.sidebar.header("🔍 全局筛选")

available_months = get_available_months()
if not available_months:
    available_months = [date.today().strftime("%Y-%m")]

selected_month = st.sidebar.selectbox("选择月份", available_months)
selected_categories = st.sidebar.multiselect(
    "选择分类（留空 = 全部）", CATEGORIES, default=[]
)

st.sidebar.divider()
st.sidebar.caption("💡 提示：在各标签页中查看和管理账目")

# ============================================================
# 主区域 — 4 个标签页
# ============================================================
tab_add, tab_list, tab_delete, tab_stats = st.tabs(
    ["➕ 添加账目", "📋 账目列表", "🗑️ 删除账目", "📊 分类统计"]
)

with tab_add:
    add.render()

with tab_list:
    list_view.render(selected_month, selected_categories)

with tab_delete:
    delete.render()

with tab_stats:
    stats.render(selected_month)
