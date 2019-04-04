import os
from properties import *

def removeClientMigrationZip():
    if os.path.isfile('%s/wso2am-%s/repository/components/dropins/wso2-api-migration-client.zip' % (APIM_HOME_PATH, NEW_VERSION)):
        if not os.remove(
                '%s/wso2am-%s/repository/components/dropins/wso2-api-migration-client.zip' % (APIM_HOME_PATH, NEW_VERSION)):
            print("Successfully removed wso2-api-migration-client.zip from it\'s locations.")
        else:
            print("Failed to remove wso2-api-migration-client.zip from it\'s locations.")


            #Python exception handling*******
