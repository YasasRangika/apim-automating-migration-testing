import os
from properties import *

def remove_tenant_loaderJar():
    if not os.remove('%s/wso2am-%s/repository/components/dropins/tenantloader-1.0.jar' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully removed tenantloader-1.0.jar from it\'s locations.")
    else:
        print("Failed to remove tenantloader-1.0.jar from it\'s locations!!!")


def remove_client_migration_zip():
    if os.path.isfile('%s/wso2am-%s/repository/components/dropins/wso2-api-migration-client.zip' % (APIM_HOME_PATH, NEW_VERSION)):
        if not os.remove(
                '%s/wso2am-%s/repository/components/dropins/wso2-api-migration-client.zip' % (APIM_HOME_PATH, NEW_VERSION)):
            print("Successfully removed wso2-api-migration-client.zip from it\'s locations.")
        else:
            print("Failed to remove wso2-api-migration-client.zip from it\'s locations!!!")
