import os
import subprocess
import socket
from shutil import *
from properties import *
from time import sleep


def copydir(source, dest):
    for root, dirs, files in os.walk(source):
        if not os.path.isdir(root):
            os.makedirs(root)

        for file in files:
            rel_path = root.replace(source, '').lstrip(os.sep)
            dest_path = os.path.join(dest, rel_path)

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)

            copyfile(os.path.join(root, file), os.path.join(dest_path, file))
            return 1


def upgradeIdentityComponents():
    is_src = '../data/Identity_component_upgrade/wso2is-%s-migration' % IS_MIGRATE_VERSION
    is_dest = '%s/wso2am-%s' % (APIM_HOME_PATH, NEW_VERSION)

    copytree('%s/migration-resources' % is_src, '%s/migration-resources' % is_dest)

    # filename = '%s/migration-config.yaml' % is_dest
    # with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    #     for line in file:
    #         if "migrationEnable: " in line:
    #             line = line.replace("migrationEnable: ", "migrationEnable: \"true\"")
    #             print(line)

    if copy('%s/org.wso2.carbon.is.migration-%s.jar' % (is_src, IS_MIGRATE_VERSION),
            '%s/repository/components/dropins' % is_dest):
        print("Successfully copied the wso2.carbon.is.migration JAR.")

    if copydir('%s/wso2am-%s/repository/resources/security' % (APIM_HOME_PATH, OLD_VERSION),
               '%s/wso2am-%s/repository/resources/security' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully Copied and replaced the keystores used in the previous version.")

    subprocess.Popen(["gnome-terminal", "-e",
                      "%s/wso2am-%s/bin/wso2server.sh -Dmigrate -Dcomponent=identity" % (APIM_HOME_PATH, NEW_VERSION)])

    print("Please manually check and stop(^c) the APIM server after it start...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', 9443))
    while result != 0:
        result = s.connect_ex(('127.0.0.1', 9443))
        sleep(5)
    s.close()
