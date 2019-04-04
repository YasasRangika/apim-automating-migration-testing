import fileinput
import os
from shutil import *
from properties import *

def reindexArtifacts():
    filename = '%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, NEW_VERSION)
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("/_system/local/repository/components/org.wso2.carbon.registry/indexing/lastaccesstime",
                               "/_system/local/repository/components/org.wso2.carbon.registry/indexing/lastaccesstime_1"),
                  end='')

    solr = '%s/wso2am-%s/solr' % (APIM_HOME_PATH, NEW_VERSION)
    if os.path.isdir(solr):
        rmtree(solr)

