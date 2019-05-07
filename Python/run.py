from ApiMangerConfigUtil.unzippingAPIMs import unzipFiles
from ApiMangerConfigUtil.run_APIM import runAPIM
from ApiMangerConfigUtil.stop_running_APIM import stopRunningServer
from ApiMangerConfigUtil.configuring_synapse_and_tenants import *
from ApiMangerConfigUtil.run_gateway_artifacts_config_script import runGatewayArtifacts
from ApiMangerConfigUtil.configuring_identity_components import *
from ApiMangerConfigUtil.remove_files import *
from ApiMangerConfigUtil.change_config_files import *
from ApiMangerConfigUtil.waiting import wait
from ApiMangerConfigUtil.run_jmeter_scripts import runJmeter
from ApiMangerConfigUtil.xml_file_change import *
from DbUtil.copy_db_connector import copyDbConnector
from DbUtil.run_sql_queries import *


def main():
    # # Unzipping all the given API Manager versions
    # unzipFiles()
    #
    # # Copy database connector into repository/components/lib directory
    # copyDbConnector(APIM_HOME_PATH, OLD_VERSION)
    #
    # # Create tables in provided database information
    # createTables()
    #
    # # master-datasource.xml file changing
    # if DB_TYPE == 'mysql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/mysql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # elif DB_TYPE == 'oracle':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/oracle/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # elif DB_TYPE == 'mssql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/mssql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # elif DB_TYPE == 'postgresql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/postgresql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # else:
    #     print("Database type provided is not valid when configuring master-datasource xml file!!!")
    #
    # # registry.xml file changing
    # change_file("registry.xml file", '../data/API-M_%s/registry.xml' % OLD_VERSION,
    #             '%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # # user-mgt.xml file changing
    # change_file("user-mgt.xml", '../data/user-mgt.xml',
    #             '%s/wso2am-%s/repository/conf/user-mgt.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # # Copy backEndService.xml for testing purposes
    # # --This back end service will forward all the requests same as it received
    # # --For token validation
    # change_file("backEndService.xml file", "../data/backEndService.xml",
    #             '%s/wso2am-%s/repository/deployment/server/synapse-configs/default/api/backEndService.xml' % (
    #                 APIM_HOME_PATH, OLD_VERSION))
    #
    # # Enabling JWT in api-manager.xml
    # # --This is for testing of jwt token in testing
    #
    # # --Uncomment the jwt enabling phrase
    # uncomment_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "EnableJWTGeneration")
    #
    # # --Change value of <EnableJWTGeneration> to true
    # edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "<EnableJWTGeneration>",
    #          "\t<EnableJWTGeneration>true</EnableJWTGeneration> \n")
    #
    # # --Change value of <JWTHeader> to jwt to use in testing process
    # edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "<JWTHeader>",
    #          "\t<JWTHeader>jwt</JWTHeader> \n")

    # run old API Manger version with database connection
    # runAPIM(APIM_HOME_PATH, OLD_VERSION)
    runAPIM()
    # os.system("gnome-terminal -e /home/yasas/Videos/testing2/wso2am-2.1.0/bin/wso2server.sh")
    # subprocess.Popen(["gnome-terminal", "-e", "/home/yasas/Videos/testing2/wso2am-2.1.0/bin/wso2server.sh"])
    # subprocess.Popen(["gnome-terminal", "-e", "%s/wso2am-%s/bin/wso2server.sh" % (APIM_HOME_PATH, OLD_VERSION)])

    # # Waiting till server getting started
    # wait()

    # # Run users and roles creation JMeter script on running APIM
    # runJmeter("RolesAndUsersCreation")

    # Run data population script to generate some previously used data on running old version of APIM
    # runJmeter("DataPopulationInOldVersion")

    # # Stop running old version of API Manager
    # stopRunningServer(APIM_HOME_PATH, OLD_VERSION)

    # # ******Configurations in new APIM******
    #
    # # Copy database connector into repository/components/lib directory
    # copyDbConnector(APIM_HOME_PATH, NEW_VERSION)
    #
    # # master-datasource.xml file changing
    # if DB_TYPE == 'mysql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/mysql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # elif DB_TYPE == 'oracle':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/oracle/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # elif DB_TYPE == 'mssql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/mssql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # elif DB_TYPE == 'postgresql':
    #
    #     change_file("master-datasources.xml file", '../data/dbconnectors/postgresql/master-datasources.xml',
    #                 '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # else:
    #     print("Database type provided is not valid when configuring master-datasource xml file!!!")
    #
    # # registry.xml file changing
    # change_file("registry.xml file", '../data/API-M_%s/registry.xml' % NEW_VERSION,
    #             '%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # # user-mgt.xml file changing
    # change_file("user-mgt.xml", '../data/user-mgt.xml',
    #             '%s/wso2am-%s/repository/conf/user-mgt.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    # # Moving all the mentioned configuaration files in migration document from old API Manger to new
    # # --Moving synapse files
    # moveSynapse()
    # # --Copying tenants
    # copyTenants()
    #
    # # Running gate way artifacts script in new API Manager version
    # runGatewayArtifacts()
    #
    # # Upgrading databases as mentioned in migration documentation
    # upgradeDBs()
    #
    # # Identity componants configuring
    # upgrade_identity_components()
    #
    # check = input("Are you ready to continue([y]/[n]): ")
    # if check.strip().lower() == "y":
    #
    #     # Copy access control migration clint and remove previously copied org.wso2.carbon.is.migration-5.6.0.jar jar file and migration-resources zip file generated
    #     access_control_migration_client()
    #
    #     check = input("Are you ready to continue([y]/[n]): ")
    #     if check.strip().lower() == "y":
    #
    #         # Upgrade registry database with new configurations of tables
    #         confRegDB()
    #         # Copy tenant loader jar
    #         copy_tenant_loader("../data/rush_re-indexing_2.5.0/tenantloader-1.0.jar",
    #                            '%s/wso2am-%s/repository/components/dropins' % (APIM_HOME_PATH, NEW_VERSION))
    #         # re-indexing artifacts
    #         reindex_artifacts('%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, NEW_VERSION))
    #
    #         # run old API Manger version with database connection
    #         runAPIM(APIM_HOME_PATH, NEW_VERSION)
    #
    #         print("Please manually check and stop(^c) the APIM server after it start...")
    #
    #         wait()
    #
    #         check = input("Are you ready to continue([y]/[n]): ")
    #         if check.strip().lower() == "y":
    #             # Remove copied tenant loader jar file
    #             remove_tenant_loaderJar()
    #             # Remove client migration zip file
    #             remove_client_migration_zip()
    #
    #             # Enabling JWT in api-manager.xml
    #             # --This is for testing of jwt token in testing
    #
    #             # --Uncomment the jwt enabling phrase
    #             uncomment_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION),
    #                           "EnableJWTGeneration")
    #
    #             # --Change value of <EnableJWTGeneration> to true
    #             edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION),
    #                      "<EnableJWTGeneration>",
    #                      "\t<EnableJWTGeneration>true</EnableJWTGeneration> \n")
    #
    #             # --Change value of <JWTHeader> to jwt to use in testing process
    #             edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "<JWTHeader>",
    #                      "\t<JWTHeader>jwt</JWTHeader> \n")
    #
    #             runAPIM(APIM_HOME_PATH, NEW_VERSION)
    #
    #             wait()
    #
    #             # test previous version's data using JMeter script on running new APIM
    #             # runJmeter("Validation_in_new_APIM")
    #
    #             # Integration testing using JMeter script on running new APIM
    #             # runJmeter("Integration_testing_in_new_APIM")


if __name__ == "__main__":
    main()