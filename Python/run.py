from ApiMangerConfigUtil.unzippingAPIMs import unzipFiles
from ApiMangerConfigUtil.run_APIM import runAPIM
from ApiMangerConfigUtil.stop_running_APIM import stopRunningServer
from ApiMangerConfigUtil.move_synapse import moveSynapse
from ApiMangerConfigUtil.copy_tenants import copyTenants
from ApiMangerConfigUtil.run_gateway_artifacts_config_script import runGatewayArtifacts
from ApiMangerConfigUtil.upgrade_identity_components import upgradeIdentityComponents
from ApiMangerConfigUtil.reg_index_sql import confRegDB
from ApiMangerConfigUtil.copy_tenantloader_jar import copyTenantLoader
from ApiMangerConfigUtil.reindex_artifacts_registry_xml import reindexArtifacts
from ApiMangerConfigUtil.remove_tenantloader_jar import removeTenantLoaderJar
from ApiMangerConfigUtil.remove_apim_client_migration_zip import removeClientMigrationZip
from ApiMangerConfigUtil.test_previous_version_APIs import testPreviousVersionData
from ApiMangerConfigUtil.create_and_test_APIs_in_new_version import createNTestInNewAPIM
from ApiMangerConfigUtil.upgrade_identity_components_post_actions import accessControlMigrationClient
from ApiMangerConfigUtil.change_config_files import change_file
from properties import *
from ApiMangerConfigUtil.waiting import wait
from ApiMangerConfigUtil.run_jmeter_scripts import runJmeter
from ApiMangerConfigUtil.xml_file_change import *
from DbUtil.copy_db_connector import copyDbConnector
from DbUtil.mysql_connection_old_apim import *
from DbUtil.upgrade_databases import upgradeDBs



def main():

    # # Unzipping all the given API Manager versions
    # unzipFiles()

    # # Copy database connector into repository/components/lib directory
    # copyDbConnector(APIM_HOME_PATH, OLD_VERSION)
    #
    # # Create database tables after the successful databases creation
    # if createDBs():
    #     createTables()
    # else:
    #     print("Error occurred while crating databases in mysql server!!")
    #
    # # master-datasource.xml file changing
    # change_file("master-datasources.xml file", '../data/master-datasources.xml',
    #             '%s/wso2am-%s/repository/conf/datasources/master-datasources.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # # registry.xml file changing
    # change_file("registry.xml file", '../data/API-M_%s/registry.xml' % OLD_VERSION,
    #             '%s/wso2am-%s/repository/conf/registry.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # # user-mgt.xml file changing
    # change_file("user-mgt.xml", '../data/user-mgt.xml',
    #             '%s/wso2am-%s/repository/conf/user-mgt.xml' % (APIM_HOME_PATH, OLD_VERSION))
    #
    # # run old API Manger version with database connection
    # runAPIM(APIM_HOME_PATH, OLD_VERSION)
    # #
    # # Waiting till server getting started
    # wait();
    # print("Done!!!")
    #
    # # Run users and roles creation JMeter script on running APIM
    # runJmeter("RolesAndUsersCreation")
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
    # # --Uncomment the jwt enabling phrase
    # uncomment_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "EnableJWTGeneration")
    # # --Change value of <EnableJWTGeneration> to true
    # edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "<EnableJWTGeneration>",
    #         "\t<EnableJWTGeneration>true</EnableJWTGeneration> \n")
    # # --Change value of <JWTHeader> to jwt to use in testing process
    # edit_xml('%s/wso2am-%s/repository/conf/api-manager.xml' % (APIM_HOME_PATH, OLD_VERSION), "<JWTHeader>",
    #         "\t<JWTHeader>jwt</JWTHeader> \n")
    #
    # # Run data population script to generate some previously used data on running old version of APIM
    # runJmeter("DataPopulationInOldVersion")
    #
    # # Stop running old version of API Manager
    # stopRunningServer(APIM_HOME_PATH, OLD_VERSION)





    #
    # ###Configurations in new APIM--------------------------------------
    #
    # copyDbConnector(APIM_HOME_PATH, NEW_VERSION)
    # confMasterDataSource(APIM_HOME_PATH, NEW_VERSION)
    # confRegXml(APIM_HOME_PATH, NEW_VERSION)
    # confUsrMgtXml(APIM_HOME_PATH, NEW_VERSION)
    # moveSynapse()
    # copyTenants()
    # runGatewayArtifacts()
    # upgradeDBs()
    # upgradeIdentityComponents()
    #
    # check = input("Are you ready to continue([y]/[n]): ")
    # if check.strip().lower() == "y":
    #
    #     accessControlMigrationClient()
    #     check = input("Are you ready to continue([y]/[n]): ")
    #     if check.strip().lower() == "y":
    #
    #         confRegDB()
    #         copyTenantLoader()
    #         reindexArtifacts()
    #
    #         runAPIM(APIM_HOME_PATH, NEW_VERSION)
    #
    #         print("Please manually check and stop(^c) the APIM server after it start...")
    #
    #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         result = s.connect_ex(('127.0.0.1', 9443))
    #         while result != 0:
    #             result = s.connect_ex(('127.0.0.1', 9443))
    #             sleep(5)
    #         s.close()
    #
    #         check = input("Are you ready to continue([y]/[n]): ")
    #         if check.strip().lower() == "y":
    #             removeTenantLoaderJar()
    #             removeClientMigrationZip()
    #
    #             runAPIM(APIM_HOME_PATH, NEW_VERSION)
    #
    #             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #             result = s.connect_ex(('127.0.0.1', 9443))
    #             while result != 0:
    #                 result = s.connect_ex(('127.0.0.1', 9443))
    #                 sleep(5)
    #
    #             # testPreviousVersionData()
    #             # createNTestInNewAPIM()


if __name__ == "__main__":
    main()
