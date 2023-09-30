import time
import datetime
import streamlit as st
from streamlit_local_storage import LocalStorage

st.set_page_config(layout="wide")

localS = LocalStorage()

if "get_local_storage_item" not in st.session_state:
  st.session_state["get_local_storage_item"] = None

if "get_storage" not in st.session_state:
  st.session_state["get_storage"] = None
if "test_get_click_btn" not in st.session_state:
  st.session_state["test_get_click_btn"] = False

start = 1
cols = st.columns([0.5,1,1,1,0.5])

def add_to_storage():
  itemKey = st.session_state["local_storage_set_key"]
  itemValue = st.session_state["local_storage_set_value"]
  localS.setItem(itemKey, itemValue)
  

cols[1].subheader("add to local storage")
with cols[1].form("add_local_storage"):
  add_cols = st.columns(2)
  add_cols[0].text_input("key", key="local_storage_set_key")
  add_cols[1].text_input("value", key="local_storage_set_value")
  st.form_submit_button("submit", on_click=add_to_storage)

def testFunc():
  st.session_state["test_get_click_btn"] = True

cols[2].subheader("get from local storage")
with cols[2].form("get_data"):
    st.text_input("key", key="get_local_storage_v")
    st.form_submit_button("Submit", on_click=testFunc) 

if st.session_state["get_local_storage_v"] != "" or st.session_state["test_get_click_btn"]:
  st.session_state["test_get_click_btn"] = False
  start +=1
  st.write(start)
  val_ = localS.getItem(st.session_state["get_local_storage_v"], key="test_get_item")
  st.session_state["get_storage"] = val_
cols[2].write(st.session_state["get_storage"])


def delete_from_storage():
  itemKey = st.session_state["local_storage_delete_key"]
  value = localS.deleteItem(itemKey)
  

cols[3].subheader("delete to local storage")
with cols[3].form("delete_local_storage"):
  st.text_input("key", key="local_storage_delete_key")
  st.form_submit_button("submit") #, on_click=delete_from_storage)


if st.session_state["local_storage_delete_key"] != "":
  itemKey_ = st.session_state["local_storage_delete_key"]
  localS.deleteItem(itemKey_)
  # if st.session_state["get_storage"]["item"] == itemKey_:
  #   st.session_state["get_storage"] = None

if "get_storage" in st.session_state and st.session_state["get_storage"] != None:
  st.write("Post del",st.session_state["get_storage"]) # st.session_state["get_storage"].get('item') == st.session_state["local_storage_delete_key"], st.session_state["get_storage"].get('item'), st.session_state["get_storage"])



  



