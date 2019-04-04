import mysql.connector as mdb
import mysql.connector
from properties import *


def createDBs():

    """Creating databases in mysql"""

    # making mysql connection
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER_NAME,
        passwd=PWD
    )
    print("MySQl server connection is successful!")

    # creating databases
    print("Trying to create databases...")
    mycursor = mydb.cursor()
    mycursor.execute('CREATE DATABASE %s' % REG_DB)
    mycursor.execute('CREATE DATABASE %s' % USER_DB)
    mycursor.execute('CREATE DATABASE %s' % AM_DB)
    print("Successfully created the databases!")
    return 1


def run_sql_file(filename, connection):

    """Format and run database table creation script files in mysql"""

    print("Trying to create database tables in mysql server...")
    cursor = connection.cursor()

    # Removing tabs, new lines since cursor.execute doesn't allow to use them
    with open(filename, 'r') as my_file:
        data = my_file.read()
        para = ''
        for line in data.splitlines():
            if not line.startswith('--'):
                para += line
        para = para.replace('\n', '')
        para = para.replace('\t', '')
        para = para.split(';')
        for line in para:
            print("Executing Query-> {}".format(line))
            # Running formatted dbscript
            cursor.execute(line)
            connection.commit()


def createTables():

    """Call to each database to execute the run command to create database tables"""

    connection = mdb.connect(user=USER_NAME, password=PWD, host=HOST, database=REG_DB)
    run_sql_file('%s/wso2am-%s/dbscripts/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), connection)
    connection = mdb.connect(user=USER_NAME, password=PWD, host=HOST, database=USER_DB)
    run_sql_file('%s/wso2am-%s/dbscripts/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), connection)
    connection = mdb.connect(user=USER_NAME, password=PWD, host=HOST, database=AM_DB)
    run_sql_file('%s/wso2am-%s/dbscripts/apimgt/mysql5.7.sql' % (APIM_HOME_PATH, OLD_VERSION), connection)
    connection.close()

def main():
    createDBs()

