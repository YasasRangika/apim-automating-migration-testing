import os
from properties import *

def runGatewayArtifacts():
    os.system(
        "/bin/bash ../data/migration_scripts/apim210_to_apim250_gateway_artifact_migrator.sh %s/wso2am-%s/repository/deployment/server/synapse-configs/default" % (
        APIM_HOME_PATH, NEW_VERSION))

    os.system(
        "/bin/bash ../data/migration_scripts/apim210_to_apim250_gateway_artifact_migrator.sh %s/wso2am-%s/repository/tenants" % (
        APIM_HOME_PATH, NEW_VERSION))
