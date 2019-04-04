#!/bin/bash

echo Trying to configure master-datasources.xml...
if cp -R data/master-datasources.xml $1/wso2am-$2/repository/conf/datasources
then
	echo  Successfully  configured
else
	echo Configuration failed
fi
