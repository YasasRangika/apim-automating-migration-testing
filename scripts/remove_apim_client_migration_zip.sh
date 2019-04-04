#!/bin/bash

if [ -e wso2-api-migration-client.zip ]
then
	rm -rf $1/wso2am-$2/repository/components/dropins/wso2-api-migration-client.zip
	if [ $? -eq 0 ]
	then
		printf "\033[32m Successfully removed wso2-api-migration-client.zip from it\'s locations. \033[0m\n"
	else
		printf "\033[31m Failed to remove wso2-api-migration-client.zip from it\'s locations. \033[0m\n"
	fi
fi
