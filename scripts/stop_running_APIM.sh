#!/bin/bash

echo Stop all running WSO2 API Manager server instances...
if fuser -k 9443/tcp
then
	printf "\033[33m Stopped running server \033[0m\n"
else
	printf "\033[31m Error occured while stopping the server \033[0m\n"
fi
