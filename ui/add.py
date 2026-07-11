"""
标签页 1：添加账目
"""
from datetime import date

import streamlit as st

from config import CATEGORIES
from database import add_transaction


def render():
    """渲染添加账目表单"""
    st.subheader("记一笔")

    with st.form("add_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            amount = st.number_input(
                "金额（元）", min_value=0.01, step=0.01, format="%.2f"
            )
            category = st.selectbox("分类", CATEGORIES)

        with col2:
            trans_date = st.date_input("日期", value=date.today())
            note = st.text_input("备注", placeholder="例如：午餐外卖")

        submitted = st.form_submit_button("✅ 添加", use_container_width=True)

        if submitted:
            add_transaction(amount, category, trans_date.isoformat(), note)
            st.success(f"已记录：{category} {amount:.2f} 元")
            st.rerun()
