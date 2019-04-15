import os
import shutil
from properties import *


# Have to write this function because of the error mentioned in https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copydir(source, dest):
    for root, dirs, files in os.walk(source):
        if not os.path.isdir(root):
            os.makedirs(root)

        # break the path and merge it with given destination since have to copy all the ingredient files
        for file in files:
            rel_path = root.replace(source, '').lstrip(os.sep)
            dest_path = os.path.join(dest, rel_path)
            # To overcome 'no directory found' error create the directories before copy
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
            # Now it allows to copy with copyfile method from shutil module
            shutil.copyfile(os.path.join(root, file), os.path.join(dest_path, file))
            return 1


def moveSynapse():
    """Move all the synapse configurations created in old API manger version"""

    src_api = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/api/' % (APIM_HOME_PATH, OLD_VERSION)
    dst_api = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/api/' % (APIM_HOME_PATH, NEW_VERSION)
    src_seq = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/sequences/' % (
        APIM_HOME_PATH, OLD_VERSION)
    dst_seq = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/sequences/' % (
        APIM_HOME_PATH, NEW_VERSION)
    src_serv = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/proxy-services/' % (
        APIM_HOME_PATH, OLD_VERSION)
    dst_serv = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/proxy-services/' % (
        APIM_HOME_PATH, NEW_VERSION)
    src_def = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/' % (
        APIM_HOME_PATH, OLD_VERSION)
    dst_def = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/' % (
        APIM_HOME_PATH, NEW_VERSION)
    tmp = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/tmp/' % (APIM_HOME_PATH, NEW_VERSION)

    print("Trying to move synapse configurations(created) -> /synapse-configs/default...")

    # IMPORTANT: Please note that it couldn't refactor this code properly since the ignore patterns are different in each

    # Moving files from api directory excepting mentioned files in the migration document
    if os.path.isdir(tmp):
        # create a temporary location to keep files copied from old version till it copy to formated end location
        # REASON: Issue with shutil.copytree(as mentioned in very first comments)
        shutil.rmtree(tmp)

    shutil.copytree(src_api, tmp, symlinks=False,
                    ignore=shutil.ignore_patterns('_RevokeAPI_.xml', '_AuthorizeAPI_.xml', '_TokenAPI_.xml',
                                                  '_UserInfoAPI_.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_api, item)

        shutil.copy(t, d)

    shutil.rmtree(tmp)

    # Moving files from sequences directory excepting mentioned files in the migration document
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

    shutil.copytree(src_seq, tmp, symlinks=False,
                    ignore=shutil.ignore_patterns('_auth_failure_handler_.xml', '_build_.xml',
                                                  '_cors_request_handler_.xml',
                                                  'fault.xml',
                                                  'main.xml', '_production_key_error_.xml',
                                                  '_resource_mismatch_handler_.xml',
                                                  '_sandbox_key_error_.xml', '_throttle_out_handler_.xml',
                                                  '_token_fault_.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_seq, item)

        shutil.copy(t, d)

    shutil.rmtree(tmp)

    # Moving files from proxy-services directory excepting mentioned files in the migration document
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

    shutil.copytree(src_serv, tmp, symlinks=False,
                    ignore=shutil.ignore_patterns('WorkflowCallbackService.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_serv, item)

        shutil.copy(t, d)

    shutil.rmtree(tmp)

    # Moving files from default directory excepting above copied directories
    if os.path.isdir(tmp):
        shutil.rmtree(tmp)

    shutil.copytree(src_def, tmp, symlinks=False,
                    ignore=shutil.ignore_patterns('api', 'proxy-services', 'sequences'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_def, item)

        if os.path.isdir(t):
            copydir(t, d)
        else:
            shutil.copy(t, d)
    shutil.rmtree(tmp)

    print("Successfully moved all tenant synapse configurations -> /repository/tenants!")


def copyTenants():
    """Copy tenants from old version to new version of API Manager"""

    print("Ready to copy tenants to new version of APIM...")
    src_dir = '%s/wso2am-%s/repository/tenants/' % (APIM_HOME_PATH, OLD_VERSION)
    src_seq = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/sequences/' % (
        APIM_HOME_PATH, OLD_VERSION)
    dst_dir = '%s/wso2am-%s/repository/tenants/' % (APIM_HOME_PATH, NEW_VERSION)

    if os.path.isdir('%s/1' % src_dir):
        print("Please wait, moving tenants...")
        copydir(src_dir, dst_dir)

        # Since there is no copy method in shutil module to copy selected files from except ignoring and there are small number of files to move; had to copy one by one using defined copydir method
        for item in os.listdir(src_dir):
            d = os.path.join(dst_dir, item)
            copydir('%s/_auth_failure_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/_cors_request_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/fault.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/main.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/_production_key_error_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/_resource_mismatch_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/_sandbox_key_error_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copydir('%s/_throttle_out_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)

        print("Tenants configuration is successful!")
    else:
        print("No tenants to move!!!")
