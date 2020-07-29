from upload_file import upload

from perser import perser

from testrail import *

client = APIClient('https://kovalenco0.testrail.io/')
client.user = 'kovalenco0@gmail.com'
client.password = 'Nolimits2101'

try:
    add_run = client.send_post(
        'add_run/1',
    {'suite_id': 1, 'name': 'APIRun', 'description': 'test'}
    )

    print(add_run)


    runs = client.send_get(
        'get_runs/1'
    )
    addresult = 'add_result/{id}'

    upload()
    perser()

    

    add_result_passed = client.send_post(
        addresult.format(id = runs[0].get('id')),
        {'status_id': 1, 'comment': 'Test passed'}
    )

    print(add_result_passed)
except:
    print('ERROR!!!')
    add_result_failed = client.send_post(
        addresult.format(id = runs[0].get('id')),
        {'status_id': 5, 'comment': 'Test failed'}
    )

    print(add_result_failed)


