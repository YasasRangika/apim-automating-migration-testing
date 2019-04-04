import zipfile
import os
from properties import *


def unzipFiles():
    print("Unzipping old APIM version...\nThis will take few seconds, please wait")
    zip_ref = zipfile.ZipFile(TO_OLD_PATH, 'r')
    zip_ref.extractall(APIM_HOME_PATH)
    zip_ref.close()
    for root, dirs, files in os.walk('%s/wso2am-%s' % (APIM_HOME_PATH, OLD_VERSION)):
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o777)
        for f in files:
            os.chmod(os.path.join(root, f), 0o777)

    print("Unzipping new APIM version...\nThis will take few seconds, please wait")
    zip_ref = zipfile.ZipFile(TO_NEW_PATH, 'r')
    zip_ref.extractall(APIM_HOME_PATH)
    zip_ref.close()
    print("Unzipping APIMs are completed!")
    for root, dirs, files in os.walk('%s/wso2am-%s' % (APIM_HOME_PATH, NEW_VERSION)):
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o777)
        for f in files:
            os.chmod(os.path.join(root, f), 0o777)
