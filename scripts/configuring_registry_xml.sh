#!/bin/bash

echo "***************************Configuring the /repository/conf/registry.xml file***********************************"
case "$2" in
	"2.1.0")
		echo Trying to configure registry.xml
		if cp -R data/API-M_2.1.0/registry.xml $1/wso2am-$2/repository/conf
		then
			echo  Successfully  configured registry.xml
		else
			echo Configuration failed, Please manually configure the /repository/conf/registry.xml file as previous version
		fi
	;;
	"2.2.0")
		echo Trying to configure registry.xml
		if cp -R data/API-M_2.2.0/registry.xml $1/wso2am-$2/repository/conf/registry.xml
		then
			echo  Successfully  configured registry.xml
		else
			echo Configuration failed, Please manually configure the /repository/conf/registry.xml file as previous version
		fi
	;;
	"2.5.0")
		echo Trying to configure registry.xml
		if cp -R data/API-M_2.5.0/registry.xml $1/wso2am-$2/repository/conf/registry.xml
		then
			echo  Successfully  configured registry.xml
		else
			echo Configuration failed, Please manually configure the /repository/conf/registry.xml file as previous version
		fi
	;;
	*)
		echo Error while selecting wso2am-$2 version of API Manager
	;;
esac

