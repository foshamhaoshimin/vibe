"""
标签页 2：账目列表
"""
import streamlit as st
import pandas as pd

from database import get_transactions


def render(selected_month: str, selected_categories: list):
    """渲染账目列表表格"""
    st.subheader("账目明细")

    transactions = get_transactions(
        month=selected_month,
        categories=selected_categories if selected_categories else None,
    )

    if not transactions:
        st.info("暂无账目记录，去添加一笔吧！")
        return

    df = pd.DataFrame(transactions)

    # 汇总指标
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("📊 记录笔数", len(df))
    with col_b:
        st.metric("💵 合计金额", f"{df['amount'].sum():.2f} 元")

    st.divider()

    # 数据表格
    st.dataframe(
        df,
        column_config={
            "id": st.column_config.NumberColumn("ID", width="small"),
            "amount": st.column_config.NumberColumn("金额", format="%.2f 元"),
            "category": st.column_config.TextColumn("分类"),
            "date": st.column_config.TextColumn("日期"),
            "note": st.column_config.TextColumn("备注"),
        },
        hide_index=True,
        use_container_width=True,
    )
