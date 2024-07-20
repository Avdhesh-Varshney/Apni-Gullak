import json

DATA_FILE_PATH = './database/data.json'

def loadData():
    with open(DATA_FILE_PATH, 'r') as file:
        data = json.load(file)
    return data
