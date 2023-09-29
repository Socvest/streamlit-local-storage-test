import time
import streamlit as st
from streamlit_local_storage import LocalStorage
localS = LocalStorage()

if "get_local_storage_item" not in st.session_state:
  st.session_state["get_local_storage_item"] = None

if "get_storage" not in st.session_state:
  st.session_state["get_storage"] = None

st.set_page_config(layout="wide")


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


def get_from_storage():
  itemKey = st.session_state["local_storage_set_key"]
  value = localS.get(itemKey, key="get_storage")
  cols[2].write(st.session_state["get_storage"])  

cols[2].subheader("get to local storage")
with cols[2].form("get_local_storage"):
  st.text_input("key", key="local_storage_get_key")
  st.form_submit_button("submit", on_click=get_from_storage)
  
# cols[2].write(st.session_state["get_local_storage_item"])

def delete_from_storage():
  itemKey = st.session_state["local_storage_delete_key"]
  value = localS.deleteItem(itemKey)
  

cols[3].subheader("delete to local storage")
with cols[3].form("delete_local_storage"):
  st.text_input("key", key="local_storage_delete_key")
  st.form_submit_button("submit", on_click=delete_from_storage)



  



