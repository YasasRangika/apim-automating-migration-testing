#!/bin/bash
source properties.conf



##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$CHANGE THE DATA BASE NAMES IN MASTER DATA SOURCE XML FILE$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*********************************

#Doc part 01:

if [[ $to_old_path -ef $to_new_path ]] 
then
	#Unzip APIMs (same directory)
	unzip -qq $to_new_path/\*.zip -d $to_new_path &
	PID=$!
	i=1
	sp="/―\|"
	echo -n Unzipping API manger all the versions [processing] : ' '
	while [ -d /proc/$PID ]
	do
	  printf "\b${sp:i++%${#sp}:1}"
	done
	echo

	#prepare variables
	i=1
	[[ $(ls -A $to_new_path) ]] && for dirs in $to_new_path/*
	do
		[[ $dirs =~ .zip ]] && continue
		re="wso2am-([^/]+)"
		if [[ $(basename $dirs) =~ $re ]]
		then
			eval "version$i=${BASH_REMATCH[1]}"
			i=$((i+1))
		fi
	done

	if [ $version1 \> $version2 ]
	then
		new_version=$version1
		old_version=$version2
	else
		new_version=$version2
		old_version=$version1
	fi
else
	#Unzip APIMs (different directory)
	unzip -qq $to_old_path/\*.zip -d $to_old_path &
	PID=$!
	i=1
	sp="/―\|"
	echo -n Unzipping API manger old version [processing] : ' '
	while [ -d /proc/$PID ]
	do
	  printf "\b${sp:i++%${#sp}:1}"
	done
	echo

	unzip -qq $to_new_path/\*.zip -d $to_new_path &
	PID=$!
	i=1
	sp="/―\|"
	echo -n Unzipping API manger new version [processing] : ' '
	while [ -d /proc/$PID ]
	do
	  printf "\b${sp:i++%${#sp}:1}"
	done
	echo

	#prepare variables
	[[ $(ls -A $to_old_path) ]] && for dirs in $to_old_path/*
	do
		[[ $dirs =~ .zip ]] && continue
		re="wso2am-([^/]+)"
		if [[ $(basename $dirs) =~ $re ]]
		then
			eval "old_version=${BASH_REMATCH[1]}"
		fi
	done
	[[ $(ls -A $to_new_path) ]] && for dirs in $to_new_path/*
	do
		[[ $dirs =~ .zip ]] && continue
		re="wso2am-([^/]+)"
		if [[ $(basename $dirs) =~ $re ]]
		then
			eval "new_version=${BASH_REMATCH[1]}"
		fi
	done
fi

#Doc part 02:

if cp data/mysql-connector-java-8.0.13.jar $to_old_path/wso2am-$old_version/repository/components/lib
then
	printf "\033[32m Successfully copied the MySQL JDBC driver JAR. \033[0m\n"
else
	printf "\033[31m Copying the MySQL JDBC driver JAR is failed. \033[0m\n"
fi

#Doc part 03:

./scripts/mysql_connection_old_apim.sh $to_old_path $old_version

#Doc part 04:

./scripts/configuring_master_datasource.sh $to_old_path $old_version

#Doc part 05:

./scripts/configuring_registry_xml.sh $to_old_path $old_version

#Doc part 06:

./scripts/configuring_user_mgt_xml.sh $to_old_path $old_version

#Doc part 07:
 
gnome-terminal -e "sh $to_old_path/wso2am-$old_version/bin/wso2server.sh"

while ! echo exit | nc localhost 9443
do 
	sleep 10
done

#Doc part 08:

./scripts/roles_and_users_creation.sh

#Doc part 09:

./scripts/jmeter_data_population.sh

#Doc part 10:

if cp data/mysql-connector-java-8.0.13.jar $to_new_path/wso2am-$new_version/repository/components/lib
then
	printf "\033[32m Successfully copied the MySQL JDBC driver JAR. \033[0m\n"
else
	printf "\033[31m Copying the MySQL JDBC driver JAR is failed. \033[0m\n"
fi

#Doc part 04:

./scripts/configuring_master_datasource.sh $to_new_path $new_version

#Doc part 05:

./scripts/configuring_registry_xml.sh $to_new_path $new_version

#Doc part 06:

./scripts/configuring_user_mgt_xml.sh $to_new_path $new_version

#Doc part 11:

./scripts/move_synapse.sh $to_old_path $old_version $to_new_path $new_version

#Doc part 12:

./scripts/copy_tenants.sh $to_old_path $old_version $to_new_path $new_version

#Doc part 13:

./scripts/stop_running_APIM.sh #Done

#Doc part 14:

./scripts/run_gateway_artifacts_config_script.sh $old_version $new_version $to_new_path

#Doc part 15:

./scripts/reindex_artifacts_registry_xml.sh $to_new_path $new_version

if [ -e ../solr ] 
then
  rm -R ../solr
fi

#Doc part 16:

./scripts/upgrade_databases.sh $old_version $new_version
if [ $? -eq 0 ]
then
	printf "\033[33m Upgraded the API Manager database from version-$old_version to version-$new_version \033[0m\n"
fi

#Doc part 17:

./scripts/upgrade_identity_components.sh $old_version $new_version $to_new_path $to_old_path

#Doc part 18:

./scripts/reg_index_sql.sh

#Doc part 19:

./scripts/copy_tenantloader_jar.sh $to_new_path $new_version

#Doc part 15:

./scripts/reindex_artifacts_registry_xml.sh $to_new_path $new_version

#Doc part 20:

./scripts/remove_apim_client_migration_zip.sh $to_new_path $new_version

#Doc part 21:

gnome-terminal -e "sh $to_new_path/wso2am-$new_version/bin/wso2server.sh"

while ! echo exit | nc localhost 9443
do 
	sleep 10
done

#Doc part 22:

./scripts/test_previous_version_APIs.sh

#Doc part 23:
##Run jmeter script to create new API and test it on new version of APIM

./scripts/create_and_test_APIs_in_new_version.sh


