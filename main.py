from upload_file import upload

from perser import perser

try:
    upload()
    perser()
except:
    print('Error')