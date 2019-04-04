#!/bin/bash

gnome-terminal -e "sh /home/yasas/Videos/testing/wso2am-2.1.0/bin/wso2server.sh"

while ! echo exit | nc localhost 9443
do 
	sleep 10
done
