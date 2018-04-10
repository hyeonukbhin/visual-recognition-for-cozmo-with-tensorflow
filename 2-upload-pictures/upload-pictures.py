import os
from swiftclient.service import Connection
import urllib.request
import shutil

def upload():
    try:
        conn = Connection(key='@Dkagh99',
                          authurl='https://identity.open.softlayer.com/v3',
                          auth_version='3',
                          os_options={"project_id": 'Default',
                                      "user_id": 'bhu@kist.re.kr',
                                      "region_name": 'Default'}
                          )       

        zipFileName = 'cozmo-photos' 
        shutil.make_archive(zipFileName, 'zip', '../1-take-pictures/pictures')
        print("Done: Zipping Pictures") 

        container = 'tensorflow'
        conn.put_container(container)
        resp_headers, containers = conn.get_account()            

        with open('./' + zipFileName + '.zip', 'rb') as local:            
            conn.put_object(
                container,
                zipFileName + '.zip',
                contents=local,
                content_type='application/zip'
            )  
            print("Done: Uploading Pictures")  

    except Exception as e:
        print("Error: Uploading Pictures")
        print(e)

    return

upload()
