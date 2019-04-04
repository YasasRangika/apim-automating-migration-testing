#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source "$DIR/../properties.conf"

case "$2" in
	"2.1.0")
		echo "Still not developed this part of code :)"
	;;
	"2.2.0")
		case "$1" in
			"2.0.0")
				echo "Still not developed this part of code :)"

#####################%%%%%%%%%%%%%%%%%%%%%%MAKE A SEPERATE SCRIPTS TO DO TASKS IN EACH ONE(COMPARE EACH VERSION BEFORE IT)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####################################

			;;
			"2.1.0")
				echo "Still not developed this part of code :)"
			;;
		esac
	;;
	"2.5.0")
		case "$1" in
			"2.0.0")
				echo "Still not developed this part of code :)"
			;;
			"2.1.0")
				sed -i 's/.*migrationEnable.*/migrationEnable: "true"/' data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/migration-resources/migration-config.yaml
				sed -i 's/.*currentVersion.*/currentVersion: "'$is_current_version'"/' data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/migration-resources/migration-config.yaml
				sed -i -n '/EventPublisherMigrator/{x;d;};1h;1!{x;p;};${x;p;}' data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/migration-resources/migration-config.yaml
				sed -i -e '/EventPublisherMigrator/,/order: 11/d' data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/migration-resources/migration-config.yaml
				cp -R data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/migration-resources $3/wso2am-$2

				if cp data/Identity_component_upgrade/wso2is-$is_migrate_version-migration/org.wso2.carbon.is.migration-$is_migrate_version.jar $3/wso2am-$2/repository/components/dropins
				then
					printf "\033[32m Successfully copied the wso2.carbon.is.migration JAR. \033[0m\n"
				else
					printf "\033[31m Failed to copy the wso2.carbon.is.migration JAR. \033[0m\n"
				fi

				if cp -R $4/wso2am-$1/repository/resources/security $3/wso2am-$2/repository/resources/security
				then
					printf "\033[32m Successfully Copied and replaced the keystores used in the previous version. \033[0m\n"
				else
					printf "\033[31m Failed to Copy and replace the keystores used in the previous version. \033[0m\n"
				fi
		
				gnome-terminal -e "sh $3/wso2am-$2/bin/wso2server.sh -Dmigrate -Dcomponent=identity"

				while ! echo exit | nc localhost 9443
				do 
					sleep 10
				done

				printf "\033[33m waiting till user manually stop the server!!! \033[0m\n"

				while lsof -Pi :9443 -sTCP:LISTEN -t >/dev/null
				do 
					sleep 10
				done

				rm -rf $3/wso2am-$2/migration-resources
				if [ $? -eq 0 ]
				then
					printf "\033[32m Successfully removed migration-resources directory from it\'s locations. \033[0m\n"
				else
					printf "\033[31m Failed to remove migration-resources directory from their locations. \033[0m\n"
				fi

				rm -rf $3/wso2am-$2/repository/components/dropins/org.wso2.carbon.is.migration-5.6.0.jar
				if [ $? -eq 0 ]
				then
					printf "\033[32m Successfully removed org.wso2.carbon.is.migration-5.6.0.jar from it\'s locations. \033[0m\n"
				else
					printf "\033[31m Failed to remove org.wso2.carbon.is.migration-5.6.0.jar from it\'s locations. \033[0m\n"
				fi
				
				if cp data/Access_control_migration_client/org.wso2.carbon.apimgt.access.control.migration.client-1.0-SNAPSHOT.jar $3/wso2am-$2/repository/components/dropins
				then
					printf "\033[32m Successfully copied the apimgt.access.control.migration.client JAR. \033[0m\n"
				else
					printf "\033[31m Failed to copy the apimgt.access.control.migration.client JAR. \033[0m\n"
				fi

				gnome-terminal -e "sh $3/wso2am-$2/bin/wso2server.sh -DmigrateAccessControl=true"

				while ! echo exit | nc localhost 9443
				do 
					sleep 10
				done

				printf "\033[33m waiting till user manually stop the server!!! \033[0m\n"

				while lsof -Pi :9443 -sTCP:LISTEN -t >/dev/null
				do 
					sleep 10
				done

				
			;;
			"2.2.0")
				echo "Still not developed this part of code :)"
			;;
		esac
	;;
	"2.6.0")
		case "$1" in
			"2.0.0")
				echo "Still not developed this part of code :)"
			;;
			"2.1.0")
				echo "Still not developed this part of code :)"
			;;
			"2.2.0")
				echo "Still not developed this part of code :)"
			;;
			"2.5.0")
				echo "Still not developed this part of code :)"
			;;
		esac
	;;
	*)
		echo "Upgrading failed in Identity components!"
	;;
esac
