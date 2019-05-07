import jaydebeapi
import shutil
from properties import *


def tier_down():
    """This function takes care about tier downing main changes did to the system i.e.database remove[mysql],remove APIM instances"""
    if DB_TYPE == 'mysql':
        conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver",
                                  'jdbc:mysql://%s:%d/%s' % (HOST, PORT, REG_DB),
                                  [USER_NAME, PWD],
                                  "../data/dbconnectors/mysql/mysql-connector-java-8.0.13.jar")
    else:
        print("Manually remove all the database instances by login to the database!!!")

    dbarr = [AM_DB, USER_DB, REG_DB]
    for db in dbarr:
        try:
            curs = conn.cursor()
            curs.execute('DROP DATABASE %s' % db)
            print('Successfully removed the %s database.' % db)
        except:
            print("Error occurred while deleting %s. Please do manually remove by login to the database!!!" % db)

    try:
        versionarr = [OLD_VERSION, NEW_VERSION]
        for version in versionarr:
            shutil.rmtree('%s/wso2am-%s' % (APIM_HOME_PATH, version))
        print("Successfully removed all unzipped APIM versions.")
    except:
        print("Error occurred while removing unzipped APIM versions!!!")
