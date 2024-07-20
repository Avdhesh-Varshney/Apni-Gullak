def fetchData(service, folder_id):
    results = service.files().list(
        q=f"'{folder_id}' in parents",
        pageSize=1000,
        fields="nextPageToken, files(id, name, mimeType, parents)"
    ).execute()
    return results.get('files', [])

def fetchFile(service, file_id):
    request = service.files().get_media(fileId=file_id)
    file_content = request.execute()
    file_info = service.files().get(fileId=file_id, fields='mimeType').execute()
    mime_type = file_info['mimeType']
    return file_content, mime_type
