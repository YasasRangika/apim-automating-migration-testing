import mysql.connector as mdb
import mysql.connector
from properties import *
import jaydebeapi


def run_sql_file(filename, db_name):
    """Format and run database table creation script files in mysql"""

    print('Trying to create database tables in %s database server...' % DB_TYPE)

    # Removing tabs, new lines since cursor.execute doesn't allow to use them
    with open(filename, 'r') as my_file:
        data = my_file.read()
        para = ''
        for line in data.splitlines(True):
            if not line.startswith('--'):
                para += line
        para = para.replace('\n', ' ')
        para = para.replace('\t', ' ')

        if DB_TYPE == 'oracle':
            para = para.split('/')
        else:
            para = para.split(';')
        for line in para:
            if format(line) != '':
                print("Executing Query-> {}".format(line))
                # Running formatted dbscript
                if DB_TYPE == 'mysql':
                    conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver",
                                              'jdbc:mysql://%s:%d/%s' % (HOST, PORT, db_name),
                                              [USER_NAME, PWD],
                                              "../data/dbconnectors/mysql/mysql-connector-java-8.0.13.jar")
                elif DB_TYPE == 'oracle':
                    conn = jaydebeapi.connect("oracle.jdbc.driver.OracleDriver",
                                              'jdbc:oracle:thin:%s@%s:%d/%s' % (USER_NAME, HOST, PORT, SID),
                                              [USER_NAME, PWD],
                                              "../data/dbconnectors/oracle/ojdbc7.jar")
                elif DB_TYPE == 'mssql':
                    conn = jaydebeapi.connect("com.microsoft.sqlserver.jdbc.SQLServerDriver",
                                              'jdbc:sqlserver://%s:%d;databaseName=%s;SendStringParametersAsUnicode=false' % (
                                                  HOST, PORT, db_name),
                                              [USER_NAME, PWD],
                                              "../data/dbconnectors/mssql/mssql-jdbc-7.2.1.jre8.jar")
                elif DB_TYPE == 'postgresql':
                    conn = jaydebeapi.connect("org.postgresql.Driver",
                                              'jdbc:postgresql://%s:%d/%s' % (HOST, PORT, db_name),
                                              [USER_NAME, PWD],
                                              "../data/dbconnectors/postgresql/postgresql-42.2.5.jar")
                else:
                    print("Database provided is not valid when creating connection!!!")

                cursor = conn.cursor()

                # Used very bad exception handling strategy here because it is throwing empty query executing error while reading line by line it gives empty line couldn't handle
                try:
                    cursor.execute(line)
                except:
                    pass
                conn.close()


def createTables():
    """Call to each database to execute the run command to create database tables"""

    if DB_TYPE == 'mysql':
        run_sql_file('%s/wso2am-%s/dbscripts/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), REG_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), USER_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/apimgt/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), AM_DB)

    elif DB_TYPE == 'oracle':
        run_sql_file('%s/wso2am-%s/dbscripts/oracle.sql' % (APIM_HOME_PATH, OLD_VERSION), SID)
        run_sql_file('%s/wso2am-%s/dbscripts/apimgt/oracle.sql' % (APIM_HOME_PATH, OLD_VERSION), SID)
    elif DB_TYPE == 'mssql':
        run_sql_file('%s/wso2am-%s/dbscripts/mssql.sql' % (APIM_HOME_PATH, OLD_VERSION), REG_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/mssql.sql' % (APIM_HOME_PATH, OLD_VERSION), USER_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/apimgt/mssql.sql' % (APIM_HOME_PATH, OLD_VERSION), AM_DB)
    elif DB_TYPE == 'postgresql':
        run_sql_file('%s/wso2am-%s/dbscripts/postgresql.sql' % (APIM_HOME_PATH, OLD_VERSION), REG_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/postgresql.sql' % (APIM_HOME_PATH, OLD_VERSION), USER_DB)
        run_sql_file('%s/wso2am-%s/dbscripts/apimgt/postgresql.sql' % (APIM_HOME_PATH, OLD_VERSION), AM_DB)
    else:
        print("Database provided is not valid when table creation!!!")


def upgradeDBs():
    """Upgrade am database with new configurations of tables"""

    if DB_TYPE == 'mysql':
        run_sql_file(
            '../data/migration_scripts/apimgt-db-migration-scripts-%sto%s/mysql.sql' % (OLD_VERSION, NEW_VERSION),
            AM_DB)

    elif DB_TYPE == 'oracle':
        run_sql_file(
            '../data/migration_scripts/apimgt-db-migration-scripts-%sto%s/oracle.sql' % (OLD_VERSION, NEW_VERSION),
            SID)

    elif DB_TYPE == 'mssql':
        run_sql_file(
            '../data/migration_scripts/apimgt-db-migration-scripts-%sto%s/mssql.sql' % (OLD_VERSION, NEW_VERSION),
            AM_DB)

    elif DB_TYPE == 'postgresql':
        run_sql_file(
            '../data/migration_scripts/apimgt-db-migration-scripts-%sto%s/postgresql.sql' % (OLD_VERSION, NEW_VERSION),
            AM_DB)

    else:
        print("Database provided is not valid when table creation!!!")


def confRegDB():
    """Upgrade registry database with new configurations of tables"""

    if DB_TYPE == 'mysql':
        run_sql_file('../data/rush_re-indexing_2.5.0/reg-index.sql',
                     REG_DB)

    elif DB_TYPE == 'oracle':
        run_sql_file('../data/rush_re-indexing_2.5.0/reg-index.sql',
                     SID)

    elif DB_TYPE == 'mssql':
        run_sql_file('../data/rush_re-indexing_2.5.0/reg-index.sql',
                     REG_DB)

    elif DB_TYPE == 'postgresql':
        run_sql_file('../data/rush_re-indexing_2.5.0/reg-index.sql',
                     REG_DB)

    else:
        print("Database provided is not valid when table creation!!!")
