import subprocess
import os
import shutil
import ApiMangerConfigUtil.configuring_synapse_and_tenants
import ApiMangerConfigUtil.waiting
from properties import *


def upgrade_identity_components():

    """Upgrading identity componants"""

    is_src = '../data/Identity_component_upgrade/wso2is-%s-migration' % IS_VERSION
    is_dest = '%s/wso2am-%s' % (APIM_HOME_PATH, NEW_VERSION)

    shutil.copytree('%s/migration-resources' % is_src, '%s/migration-resources' % is_dest)

    # Choose relevant IS version
    if shutil.copy('%s/org.wso2.carbon.is.migration-%s.jar' % (is_src, IS_VERSION),
            '%s/repository/components/dropins' % is_dest):
        print("Successfully copied the wso2.carbon.is.migration JAR!")

    if ApiMangerConfigUtil.configuring_synapse_and_tenants.copydir('%s/wso2am-%s/repository/resources/security' % (APIM_HOME_PATH, OLD_VERSION),
               '%s/wso2am-%s/repository/resources/security' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully Copied and replaced the keystores used in the previous version!")

    subprocess.Popen(["gnome-terminal", "-e",
                      "%s/wso2am-%s/bin/wso2server.sh -Dmigrate -Dcomponent=identity" % (APIM_HOME_PATH, NEW_VERSION)])

    print("Please manually check and stop(^c) the APIM server after it get started...")

    ApiMangerConfigUtil.waiting.wait()


def access_control_migration_client():

    """Copy access control migration client and configure server"""

    dir = '%s/wso2am-%s/migration-resources' % (APIM_HOME_PATH, NEW_VERSION)
    if os.path.isdir(dir):
        shutil.rmtree(dir)

    jar_dir = '%s/wso2am-%s/repository/components/dropins/org.wso2.carbon.is.migration-%s.jar' % (
        APIM_HOME_PATH, NEW_VERSION, IS_VERSION)
    os.remove(jar_dir)

    if shutil.copy(
            '../data/Access_control_migration_client/org.wso2.carbon.apimgt.access.control.migration.client-1.0-SNAPSHOT.jar',
            '%s/wso2am-%s/repository/components/dropins' % (APIM_HOME_PATH, NEW_VERSION)):
        print("Successfully copied the apimgt.access.control.migration.client JAR.")

    subprocess.Popen(["gnome-terminal", "-e",
                      "%s/wso2am-%s/bin/wso2server.sh -DmigrateAccessControl=true" % (APIM_HOME_PATH, NEW_VERSION)])

    print("Please manually check and stop(^c) the APIM server after it get started...")

    ApiMangerConfigUtil.waiting.wait()
