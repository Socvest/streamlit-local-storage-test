import streamlit as st
from streamlit_local_storage import LocalStorage
localS = LocalStorage()

cols = st.columns(3)

def add_to_storage():
  itemKey = st.session_state["local_storage_set_key"]
  itemValue = st.session_state["local_storage_set_value"]
  localS.set(itemKey, itemValue)
  

cols[0].subheader("add to local storage")
with cols[0].form("add_local_storage"):
  add_cols = st.columns(2)
  add_cols[0].text_input("key", key="local_storage_set_key")
  add_cols[1].text_input("value", key="local_storage_set_value")
  st.form_submit_button("submit", on_click=add_to_storage)



