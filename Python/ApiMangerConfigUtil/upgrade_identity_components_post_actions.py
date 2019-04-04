import os
import socket
import subprocess
from shutil import *
from properties import *
from time import sleep


def accessControlMigrationClient():
    dir = '%s/wso2am-%s/migration-resources' % (APIM_HOME_PATH, NEW_VERSION)
    if os.path.isdir(dir):
        rmtree(dir)

    jar_dir = '%s/wso2am-%s/repository/components/dropins/org.wso2.carbon.is.migration-5.6.0.jar' % (
        APIM_HOME_PATH, NEW_VERSION)
    os.remove(jar_dir)

    if copy(
            '../data/Access_control_migration_client/org.wso2.carbon.apimgt.access.control.migration.client-1.0-SNAPSHOT.jar',
            '%s/wso2am-%s/repository/components/dropins' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully copied the apimgt.access.control.migration.client JAR.")

    subprocess.Popen(["gnome-terminal", "-e",
                      "%s/wso2am-%s/bin/wso2server.sh -DmigrateAccessControl=true" % (APIM_HOME_PATH, NEW_VERSION)])

    print("Please manually check and stop(^c) the APIM server after it start...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', 9443))
    while result != 0:
        result = s.connect_ex(('127.0.0.1', 9443))
        sleep(5)
    s.close()
