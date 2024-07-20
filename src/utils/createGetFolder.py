import streamlit as st
from googleapiclient.errors import HttpError

def createGetFolder(service, folder_name, parent_folder_id):
    query = f"mimeType='application/vnd.google-apps.folder' and '{parent_folder_id}' in parents and trashed=false"
    try:
        response = service.files().list(q=query, spaces='drive').execute()
        for file in response.get('files', []):
            if file.get('name') == folder_name:
                return file.get('id')
    except HttpError as error:
        st.error(f'An error occurred: {error}')
    
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]
    }
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    return folder.get('id')

