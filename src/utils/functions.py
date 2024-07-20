import streamlit as st
from src.auth.profile import profile

def logout():
  if st.session_state.logged_in:
    profile()
    if st.button("Log out"):
      st.session_state.logged_in = False
      st.rerun()

logout_page = st.Page(logout, title="My Profile", icon=":material/account_circle:")
dashboard = st.Page("src/apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")

# Pages
read = st.Page("src/apps/read.py", title="Read", icon=":material/cloud_download:")
upload = st.Page("src/apps/upload.py", title="Upload", icon=":material/cloud_upload:")

# Loading All The Pages After Login 
def load_functions():
  pages = {
    "": [dashboard],
    "Account": [logout_page],
    "Services": [read, upload]
  }
  return pages
