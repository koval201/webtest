import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
#from parser import main

def upload():
    os.system('python --version > file.txt')

    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    folder_id = '1Bz75IcdiIB-bdmc68ux-v42hlyolup2G'

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    file_names = ['file.txt']
    mime_types = ['text/plain']

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        media = MediaFileUpload('./{0}'.format(file_name), mimetype=mime_type)
        service.files().create(
            body = file_metadata,
            media_body = media,
            fields = 'id'
        ).execute()

#try:
#   main()
#except:
#    print("error")