#!/bin/bash

if [ "$2" == "2.1.0" ] || [ "$2" == "2.2.0" ]
then
echo "*****************************Re-indexing the artifacts in the registry*********************************"
sed -i.bak 's/\/_system\/local\/repository\/components\/org.wso2.carbon.registry\/indexing\/lastaccesstime/\/_system\/local\/repository\/components\/org.wso2.carbon.registry\/indexing\/lastaccesstime_1/' $1/wso2am-$2/repository/conf/registry.xml
if [ $? -eq 0 ]
then
	printf "\033[32m Re-indexing the artifacts in the registry.xml is successful. \033[0m\n"
else
	printf "\033[31m Configuration failed, Please manually rename the <lastAccessTimeLocation> element in the <API-M_2.x.0_HOME>/repository/conf/registry.xml file. \033[0m\n"
fi
fi
