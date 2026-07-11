"""
标签页 4：分类统计
"""
import streamlit as st
import pandas as pd

from database import get_monthly_stats


def render(selected_month: str):
    """渲染分类统计：柱状图 + 统计表"""
    st.subheader(f"📅 {selected_month} 分类统计")

    stats = get_monthly_stats(selected_month)

    if not stats:
        st.info(f"{selected_month} 暂无账目记录")
        return

    df_stats = pd.DataFrame(stats)

    # 计算占比
    total = df_stats["total"].sum()
    df_stats["占比"] = df_stats["total"].apply(lambda x: f"{x / total * 100:.1f}%")

    # ---- 柱状图 ----
    st.subheader("📊 各分类支出（柱状图）")
    chart_data = df_stats.set_index("category")["total"]
    st.bar_chart(chart_data, use_container_width=True)

    # ---- 统计表 ----
    st.subheader("📋 统计明细")
    st.dataframe(
        df_stats,
        column_config={
            "category": st.column_config.TextColumn("分类"),
            "count": st.column_config.NumberColumn("笔数"),
            "total": st.column_config.NumberColumn("总额", format="%.2f 元"),
            "占比": st.column_config.TextColumn("占比"),
        },
        hide_index=True,
        use_container_width=True,
    )

    # 总计
    st.caption(f"💰 {selected_month} 总支出：{total:.2f} 元")
