#!/bin/bash

echo "*****************************Re-indexing the artifacts in the registry*********************************"
sed -i.bak 's/\/_system\/local\/repository\/components\/org.wso2.carbon.registry\/indexing\/lastaccesstime/\/_system\/local\/repository\/components\/org.wso2.carbon.registry\/indexing\/lastaccesstime_1/' $1/wso2am-$2/repository/conf/registry.xml
if [ $? -eq 0 ]
then
	printf "\033[32m Re-indexing the artifacts in the registry.xml is successful. \033[0m\n"
else
	printf "\033[31m Configuration failed, Please manually rename the <lastAccessTimeLocation> element in the <API-M_2.x.0_HOME>/repository/conf/registry.xml file. \033[0m\n"
fi

if [ -e ../solr ] 
then
  rm -R ../solr
fi

gnome-terminal -e "sh $1/wso2am-$2/bin/wso2server.sh"

while ! echo exit | nc localhost 9443
do 
	sleep 10
done

printf "\033[33m waiting till user manually stop the server!!! \033[0m\n"

while lsof -Pi :9443 -sTCP:LISTEN -t >/dev/null
do 
	sleep 10
done

rm -rf $1/wso2am-$2/repository/components/dropins/tenantloader-1.0.jar
if [ $? -eq 0 ]
then
	printf "\033[32m Successfully removed tenantloader-1.0.jar from it\'s locations. \033[0m\n"
else
	printf "\033[31m Failed to remove tenantloader-1.0.jar from it\'s locations. \033[0m\n"
fi
