import shutil


def copyDbConnector(home, version):
    if shutil.copy("../data/mysql-connector-java-8.0.13.jar",
                   home + "/wso2am-" + version + "/repository/components/lib"):
        print("Successfully copied the MySQL JDBC driver JAR.")
    else:
        print("Copying the MySQL JDBC driver JAR is failed.")
