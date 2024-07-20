# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
import streamlit as st
from googleapiclient.http import MediaIoBaseUpload

# Helper functions
from src.utils.getCreateFolders import getCreateFolders

# Load the general settings from secrets
PARENT_FOLDER_ID = st.secrets["general"]["PARENT_FOLDER_ID"]

def uploadFile(file_name, file, directory_path):
    service = st.session_state.authenticate

    folder_id = getCreateFolders(PARENT_FOLDER_ID, service, directory_path)
    
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaIoBaseUpload(file, mimetype='application/octet-stream')
    uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return uploaded_file.get('id')
