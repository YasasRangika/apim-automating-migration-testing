import os
from properties import *

def removeTenantLoaderJar():
    if not os.remove('%s/wso2am-%s/repository/components/dropins/tenantloader-1.0.jar' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully removed tenantloader-1.0.jar from it\'s locations.")
    else:
        print("Failed to remove tenantloader-1.0.jar from it\'s locations.")
