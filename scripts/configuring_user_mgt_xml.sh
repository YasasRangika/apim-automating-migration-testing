#!/bin/bash

echo "*****************************Configuring the /repository/conf/user-mgt.xml file*********************************"

case "$2" in

	"2.1.0" | "2.2.0" | "2.5.0")
		echo Trying to configure user-mgt.xml
		if cp -R data/user-mgt.xml $1/wso2am-$2/repository/conf/user-mgt.xml
		then
			printf "Successfully  configured\n"
		else
			printf "Configuration failed, Please manually configure the /repository/conf/user-mgt.xml file as previous version\n"
		fi
	;;

	#If a new version with defferent user-mgt.xml file,
	# copy configured user-mgt.xml file to new folder named version in data directory, then edit xxx and uncomment this
	# "x.x.x")
	#	echo "Trying to configure user-mgt.xml"
	#	if cp -R data/registryXXX.xml $1/wso2am-$2/repository/conf/user-mgt.xml
	#	then
	#		echo  "Successfully  configured"
	#	else
	#		echo "Configuration failed, Please manually configure the /repository/conf/user-mgt.xml file as previous version"
	#	fi
	# ;;
	

	*)
		printf "Error while selecting wso2am-$2 version of API Manager\n"
	;;
esac


