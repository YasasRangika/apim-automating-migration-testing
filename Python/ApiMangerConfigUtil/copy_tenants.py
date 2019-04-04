import os
from shutil import *
from properties import *


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


def copyTenants():
    print("Ready to copy tenants to new version of APIM: ")
    src_dir = '%s/wso2am-%s/repository/tenants/' % (APIM_HOME_PATH, OLD_VERSION)
    src_seq = '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/sequences/' % (
        APIM_HOME_PATH, OLD_VERSION)
    dst_dir = '%s/wso2am-%s/repository/tenants/' % (APIM_HOME_PATH, NEW_VERSION)

    if os.path.isdir('%s/1' % src_dir):
        print("\tPlease wait, moving tenants...")
        copydir(src_dir, dst_dir)

        for item in os.listdir(dst_dir):
            d = os.path.join(dst_dir, item)
            copy('%s/_auth_failure_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/_cors_request_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/fault.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/main.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/_production_key_error_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/_resource_mismatch_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/_sandbox_key_error_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)
            copy('%s/_throttle_out_handler_.xml' % src_seq, '%s/synapse-configs/default/sequences' % d)

        print("\tTenants configuration is successful!")
    else:
        print("\tNo tenants to move!!")
