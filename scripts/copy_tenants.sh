#!/bin/bash

#rsync -aP $end_version/repository/tenants/* ../../../repository/tenants
cp -R $1/wso2am-$2/repository/tenants/* $3/wso2am-$4/repository/tenants

if [ ! -e "$3"/wso2am-"$4"/repository/tenants ] 
then
  echo Path does not exists
fi

if [ -z "$3"/wso2am-"$4"/repository/tenants/1 ]
then
  echo No tenants to configure!!!
else
	[[ $(ls -A $3/wso2am-$4/repository/tenants) ]] && for dirs in $3/wso2am-$4/repository/tenants/*
	do
		if cp -R $3/wso2am-$4/repository/deployment/server/synapse-configs/default/sequences/{_auth_failure_handler_.xml,_cors_request_handler_.xml,fault.xml,main.xml,_production_key_error_.xml,_resource_mismatch_handler_.xml,_sandbox_key_error_.xml,_throttle_out_handler_.xml} $3/wso2am-$4/repository/tenants/$(basename $dirs)/synapse-configs/default/sequences
		then
			printf "\033[32m Successfully configured tenants files to new version's tenent: $(basename $dirs) \033[0m\n"
		else
			printf "\033[31m Configuration failed please do manually copy <API-M_X.X.0_MANAGER_HOME>/repository/deployment/server/synapse-configs/default/sequences directory and replace the corresponding files in the <API-M_X.X.0_MANAGER_HOME>/repository/tenants/<tenant-id>/synapse-configs/default/sequences directory \033[0m\n"
		fi
	done
fi
