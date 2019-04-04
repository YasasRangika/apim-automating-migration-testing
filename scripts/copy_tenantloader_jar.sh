#!/bin/bash

if cp data/rush_re-indexing_2.5.0/tenantloader-1.0.jar $1/wso2am-$2/repository/components/dropins
then
	echo  Successfully copied the tenantloader JAR.
else
	echo Failed to copy the tenantloader JAR.
fi
