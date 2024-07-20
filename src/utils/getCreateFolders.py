from src.utils.createGetFolder import createGetFolder

def getCreateFolders(PARENT_FOLDER_ID, service, path):
    parent_folder_id = PARENT_FOLDER_ID
    for folder_name in path:
        parent_folder_id = createGetFolder(service, folder_name, parent_folder_id)
    return parent_folder_id
