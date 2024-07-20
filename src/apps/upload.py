import streamlit as st

# Helper functions
from database.loadData import loadData
from src.utils.animatedText import animatedText
from src.utils.uploadFile import uploadFile

def upload(directory_path):
    st.header("Upload Your File 📂")
    uploaded_file = st.file_uploader("Choose a file 🎉", type=['png', 'jpg', 'jpeg', 'pdf', 'webp'])

    if st.button("Upload 🚀") and uploaded_file is not None:
        file_name = uploaded_file.name
        file_id = uploadFile(file_name, uploaded_file, directory_path)
        st.success(f"File uploaded successfully with ID: {file_id} 🎊", icon="🎉")
    else:
        st.info("No file uploaded yet. 📁", icon="ℹ️")

def getDirectoryPath(data):
    directory_path = []
    current_data = data

    while True:
        category = st.selectbox("Select a category 📦", [None] + [key for key in current_data.keys()], key=len(directory_path))
        if category is None:
            break
        directory_path.append(category)
        current_data = current_data[category]

        if not isinstance(current_data, dict) or not current_data:
            break

    return directory_path if len(directory_path) > 1 else None

def main():
    st.set_page_config(page_title="My Gullak: File Upload Portal", page_icon="☁️")
    st.markdown(f'''<h1 style='text-align: center;'>{animatedText("My Gullak: File Upload Portal 🌈")}</h1>''', unsafe_allow_html=True)
    data = loadData()

    directory_path = getDirectoryPath(data)
    if directory_path:
        st.markdown(f"<h5 style='text-align: center;'>Selected Directory Path: {animatedText(f"{' > '.join(directory_path)}")}</h5>", unsafe_allow_html=True)
        upload(directory_path)
    else:
        st.warning("Please select all the categories to upload the file. 📁", icon="⚠️")

main()
