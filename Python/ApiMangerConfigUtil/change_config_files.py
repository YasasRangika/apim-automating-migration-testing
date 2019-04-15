import shutil
import fileinput
import os
from properties import *

def change_file(task, src, dst):
    """This function will copy the files from given location to required location in API Manger

        Later this will replaced by templating"""

    print('Trying to configure %s' % task)
    if shutil.copyfile(src, dst):
        print('Successfully  changed %s' % task)
    else:
        print("%s changing failed!!" % task)


def copy_tenant_loader(src, dst):
    if shutil.copy(src, dst):
       print("Successfully copied the tenant loader")
    else:
        print("Error occurred while copying tenant loader")


def reindex_artifacts(filename):

    """Re-indexing artifacts"""

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("/_system/local/repository/components/org.wso2.carbon.registry/indexing/lastaccesstime",
                               "/_system/local/repository/components/org.wso2.carbon.registry/indexing/lastaccesstime_1"),
                  end='')
        print("Successfully re-indexed")
    # Remove if there any solr directory created
    solr = '%s/wso2am-%s/solr' % (APIM_HOME_PATH, NEW_VERSION)
    if os.path.isdir(solr):
        shutil.rmtree(solr)
