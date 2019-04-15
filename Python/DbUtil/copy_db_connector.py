import shutil
from properties import *


def copyDbConnector(home, version):

    """Copy database connector to the api manager"""

    if DB_TYPE == 'mysql':

        if shutil.copy("../data/dbconnectors/mysql/mysql-connector-java-8.0.13.jar",
                       home + "/wso2am-" + version + "/repository/components/lib"):
            print("Successfully copied the MySQL JDBC driver JAR.")
        else:
            print("Copying the MySQL JDBC driver JAR is failed.")

    elif DB_TYPE == 'oracle':

        if shutil.copy("../data/dbconnectors/oracle/ojdbc7.jar",
                       home + "/wso2am-" + version + "/repository/components/lib"):
            print("Successfully copied the Oracle JDBC driver JAR.")
        else:
            print("Copying the Oracle JDBC driver JAR is failed.")

    elif DB_TYPE == 'mssql':

        if shutil.copy("../data/dbconnectors/mssql/mssql-jdbc-7.2.1.jre8.jar",
                       home + "/wso2am-" + version + "/repository/components/lib"):
            print("Successfully copied the MSSQL JDBC driver JAR.")
        else:
            print("Copying the MSSQL JDBC driver JAR is failed.")

    elif DB_TYPE == 'postgresql':

        if shutil.copy("../data/dbconnectors/postgresql/postgresql-42.2.5.jar",
                       home + "/wso2am-" + version + "/repository/components/lib"):
            print("Successfully copied the PostgreSQL JDBC driver JAR.")
        else:
            print("Copying the PostgreSQL JDBC driver JAR is failed.")

    else:
        print("Database type provided is not valid when copying the database connector!!!")
