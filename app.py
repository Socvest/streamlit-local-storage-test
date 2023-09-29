import streamlit as st
from streamlit_local_storage import LocalStorage

if "get_local_storage_item" not in st.session_state:
  st.session_state["get_local_storage_item"] = None

st.set_page_config(layout="wide")

localS = LocalStorage()

cols = st.columns([0.5,1,1,1,0.5])

def add_to_storage():
  itemKey = st.session_state["local_storage_set_key"]
  itemValue = st.session_state["local_storage_set_value"]
  localS.set(itemKey, itemValue)
  

cols[1].subheader("add to local storage")
with cols[1].form("add_local_storage"):
  add_cols = st.columns(2)
  add_cols[0].text_input("key", key="local_storage_set_key")
  add_cols[1].text_input("value", key="local_storage_set_value")
  st.form_submit_button("submit", on_click=add_to_storage)


def add_to_storage():
  itemKey = st.session_state["local_storage_set_key"]
  value = localS.get(itemKey)
  st.session_state["get_local_storage_item"] = value
  

cols[1].subheader("add to local storage")
with cols[1].form("add_local_storage"):
  # add_cols = st.columns(2)
  st.text_input("key", key="local_storage_get_key")
  if st.session_state["get_local_storage_item"] != None:
    st.write(st.session_state["get_local_storage_item"])
  st.form_submit_button("submit", on_click=add_to_storage)
  



