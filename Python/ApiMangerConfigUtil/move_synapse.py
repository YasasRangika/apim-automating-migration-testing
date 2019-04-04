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


def moveSynapse():
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

    print(
        "*****************************Move synapse configurations(created) -> /synapse-configs/default*********************************")

    if os.path.isdir(tmp):
        rmtree(tmp)

    copytree(src_api, tmp, symlinks=False,
             ignore=ignore_patterns('_RevokeAPI_.xml', '_AuthorizeAPI_.xml', '_TokenAPI_.xml', '_UserInfoAPI_.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_api, item)

        copy(t, d)

    rmtree(tmp)

    if os.path.isdir(tmp):
        rmtree(tmp)

    copytree(src_seq, tmp, symlinks=False,
             ignore=ignore_patterns('_auth_failure_handler_.xml', '_build_.xml', '_cors_request_handler_.xml',
                                    'fault.xml',
                                    'main.xml', '_production_key_error_.xml', '_resource_mismatch_handler_.xml',
                                    '_sandbox_key_error_.xml', '_throttle_out_handler_.xml', '_token_fault_.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_seq, item)

        copy(t, d)

    rmtree(tmp)

    if os.path.isdir(tmp):
        rmtree(tmp)

    copytree(src_serv, tmp, symlinks=False,
             ignore=ignore_patterns('WorkflowCallbackService.xml'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_serv, item)

        copy(t, d)

    rmtree(tmp)

    if os.path.isdir(tmp):
        rmtree(tmp)

    copytree(src_def, tmp, symlinks=False,
             ignore=ignore_patterns('api', 'proxy-services', 'sequences'))

    for item in os.listdir(tmp):
        t = os.path.join(tmp, item)
        d = os.path.join(dst_def, item)

        if os.path.isdir(t):
            copydir(t, d)
        else:
            copy(t, d)
    rmtree(tmp)

    print(
        "*****************************Moved all tenant synapse configurations -> /repository/tenants*********************************")
