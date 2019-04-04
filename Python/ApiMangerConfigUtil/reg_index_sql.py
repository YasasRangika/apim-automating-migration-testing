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


def confRegDB():
    connection = mdb.connect(user=USER_NAME, password=PWD, host=HOST, database='regdb1')
    run_sql_file('../data/rush_re-indexing_2.5.0/reg-index.sql',
                 connection)
    connection.close()

