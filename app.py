import streamlit as st
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load the general settings from secrets
SCOPES = st.secrets["general"]["SCOPES"]
SERVICE_ACCOUNT_FILE_URL = st.secrets["general"]["SERVICE_ACCOUNT_FILE"]

def downloadFile(file_url):
    file_id = file_url.split('/')[-2]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    response = requests.get(download_url)
    response.raise_for_status()
    
    with open('universal-ion-430004-j8-6c20be48b0ab.json', 'wb') as f:
        f.write(response.content)

def authenticate():
    downloadFile(SERVICE_ACCOUNT_FILE_URL)
    credentials = service_account.Credentials.from_service_account_file('universal-ion-430004-j8-6c20be48b0ab.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
  st.session_state.username = ""
  st.session_state.name = ""
  st.session_state.role = ""
  st.session_state.gender = ""
  st.session_state.age = 5
  st.session_state.email = ""
  st.session_state.about = ""
  st.session_state.authenticate = None

from src.auth.login import login
def logged_in():
  userData = login()
  if userData != []:
    st.session_state.logged_in = True
    st.session_state.username = userData[0][1]
    st.session_state.name = userData[0][2]
    st.session_state.role = userData[0][3]
    st.session_state.gender = userData[0][4]
    st.session_state.age = userData[0][5]
    st.session_state.email = userData[0][6]
    st.session_state.about = userData[0][7]
    st.session_state.authenticate = authenticate()
    st.rerun()

login_page = st.Page(logged_in, title="Log in", icon=":material/login:")
sign_up_page = st.Page("src/auth/signup.py", title="Sign Up", icon=":material/assignment_ind:")

dashboard = st.Page("src/apps/dashboard.py", title="Dashboard", icon=":material/dashboard:")

from src.utils.functions import load_functions
if st.session_state.logged_in:
  app = st.navigation(pages=load_functions())
else:
  app = st.navigation({"": [dashboard], "Account": [login_page, sign_up_page]})

app.run()
