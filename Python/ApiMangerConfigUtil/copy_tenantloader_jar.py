from shutil import *
from properties import *


def copyTenantLoader():
    if copy(
            '../data/rush_re-indexing_2.5.0/tenantloader-1.0.jar',
            '%s/wso2am-%s/repository/components/dropins' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully copied the tenantloader JAR.")
