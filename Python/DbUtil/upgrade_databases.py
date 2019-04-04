import mysql.connector as mdb
from properties import *


def run_sql_file(filename, connection):
    cursor = connection.cursor()

    with open(filename, 'r') as myfile:
        data = myfile.read()
        para = ''
        for line in data.splitlines():
            if not line.startswith('--'):
                para += line
        para = para.replace('\n', '')
        para = para.replace('\t', '')
        para = para.split(';')
        for line in para:
            print("Executing Query-> {}".format(line))
            cursor.execute(line)
            connection.commit()


def upgradeDBs():
    connection = mdb.connect(user=USER_NAME, password=PWD, host=HOST, database='amdb1')
    run_sql_file('../data/migration_scripts/apimgt-db-migration-scripts-%sto%s/mysql.sql' % (OLD_VERSION, NEW_VERSION),
                 connection)
    connection.close()
