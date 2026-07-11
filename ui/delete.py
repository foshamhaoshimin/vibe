"""
标签页 3：删除账目
"""
import streamlit as st

from database import delete_transaction, get_all_ids


def render():
    """渲染删除账目界面"""
    st.subheader("删除账目")

    all_ids = get_all_ids()

    if not all_ids:
        st.info("暂无账目可删除")
        return

    st.caption(f"当前共有 {len(all_ids)} 条记录，ID 范围：{all_ids[0]} ~ {all_ids[-1]}")

    with st.form("delete_form", clear_on_submit=True):
        trans_id = st.number_input("输入要删除的账目 ID", min_value=1, step=1, value=1)
        confirm = st.checkbox("我确认要删除这条记录")
        submitted = st.form_submit_button("🗑️ 确认删除", use_container_width=True)

        if submitted:
            if not confirm:
                st.warning("请先勾选确认")
            elif delete_transaction(trans_id):
                st.success(f"已删除 ID = {trans_id} 的账目")
                st.rerun()
            else:
                st.error(f"未找到 ID = {trans_id} 的账目，请检查后重试")
