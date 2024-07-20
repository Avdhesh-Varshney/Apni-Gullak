import streamlit as st

# Helper functions
from src.utils.fetchData import fetchData, fetchFile
from src.utils.animatedText import animatedText

# Load the general settings from secrets
PARENT_FOLDER_ID = st.secrets["general"]["PARENT_FOLDER_ID"]
if 'folder_trackback' not in st.session_state:
    st.session_state.folder_trackback = [PARENT_FOLDER_ID]

def segregateData(data):
    folders, files = [], []
    for item in data:
        if item['mimeType'] == "application/vnd.google-apps.folder":
            folders.append({'id': item['id'], 'name': item['name']})
        else:
            files.append({'id': item['id'], 'name': item['name']})
    return folders, files

def showFolders(folders):
    st.title("Folders 📁")
    folder_names = [folder['name'] for folder in folders]
    selected_folder = st.selectbox("Select a folder", [None] + folder_names)

    if selected_folder:
        current_folder_id = next(folder['id'] for folder in folders if folder['name'] == selected_folder)
        st.session_state.folder_trackback.append(current_folder_id)
        st.experimental_rerun()

def showFiles(service, files):
    st.title("Files 📄")
    for file in files:
        st.markdown(f"<h2>{file['name']}</h2>", unsafe_allow_html=True)
        if st.button(f"View {file['name']}", key=file['id']):
            file_content, mime_type = fetchFile(service, file['id'])
            if mime_type.startswith('image/'):
                st.image(file_content, caption=file['name'])
            elif mime_type.startswith('text/'):
                st.text(file_content.decode('utf-8'))
            elif mime_type == 'application/pdf':
                st.write("PDF files cannot be directly rendered in the app. Please use the download button below.")
            else:
                st.write(f"Cannot render this file type: {mime_type}")
            st.download_button(label="Download", data=file_content, file_name=file['name'], key=f"{file['id']}_download")

def main():
    st.set_page_config(page_title="My Gullak: File Reading Portal", page_icon="☁️")
    st.markdown(f'''<h1 style='text-align: center;'>{animatedText("My Gullak: File Reading Portal 🌈")}</h1>''', unsafe_allow_html=True)

    service = st.session_state.authenticate
    current_folder_id = st.session_state.folder_trackback[-1]

    if len(st.session_state.folder_trackback) > 1 and st.button("Back"):
        st.session_state.folder_trackback.pop()
        st.experimental_rerun()

    data = fetchData(service, current_folder_id)
    if data:
        FOLDERS, FILES = segregateData(data)
        if len(FOLDERS) > 0:
            st.markdown("---")
            showFolders(FOLDERS)
        if len(FILES) > 0:
            st.markdown("---")
            showFiles(service, FILES)
    else:
        st.warning("No data found in this folder. 📁", icon="⚠️")

main()
