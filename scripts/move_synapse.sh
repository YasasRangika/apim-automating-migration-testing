#!/bin/bash

echo "*****************************Move synapse configurations(created) -> /synapse-configs/default*********************************"

if [ -z "$1" ]
then
  echo Path is empty!
  exit
fi

if [ ! -e "$1" ] 
then
  echo Path does not exists
fi

#Copy all created /synapse-configs/default/api configs - 5
rsync -aP --exclude=_RevokeAPI_.xml --exclude=_AuthorizeAPI_.xml --exclude=_TokenAPI_.xml --exclude=_UserInfoAPI_.xml  $1/wso2am-$2/repository/deployment/server/synapse-configs/default/api/* $3/wso2am-$4/repository/deployment/server/synapse-configs/default/api

#Copy all created /synapse-configs/default/sequences configs
rsync -aP --exclude=_auth_failure_handler_.xml --exclude=_build_.xml --exclude=_cors_request_handler_.xml --exclude=fault.xml --exclude=main.xml --exclude=_production_key_error_.xml --exclude=_resource_mismatch_handler_.xml --exclude=_sandbox_key_error_.xml --exclude=_throttle_out_handler_.xml --exclude=_token_fault_.xml $1/wso2am-$2/repository/deployment/server/synapse-configs/default/sequences/* $3/wso2am-$4/repository/deployment/server/synapse-configs/default/sequences

#Copy all created /synapse-configs/default/proxy-services configs
rsync -aP --exclude=WorkflowCallbackService.xml $1/wso2am-$2/repository/deployment/server/synapse-configs/default/proxy-services/* $3/wso2am-$4/repository/deployment/server/synapse-configs/default/proxy-services

#Copy all created /synapse-configs/default configs
rsync -aP --exclude=api --exclude=proxy-services --exclude=sequences $1/wso2am-$2/repository/deployment/server/synapse-configs/default/* $3/wso2am-$4/repository/deployment/server/synapse-configs/default

printf "\033[32m *****************************Moved all tenant synapse configurations -> /repository/tenants********************************* \033[0m\n"

