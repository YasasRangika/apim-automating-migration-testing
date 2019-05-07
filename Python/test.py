from properties import *
file = "/home/yasas/master-datasources.xml"
f = open(file, "r+")
url = ['jdbc:h2:repository/database/WSO2CARBON_DB;DB_CLOSE_ON_EXIT=FALSE','jdbc:mysql://%s:%d/%s?useSSL=false' % (HOST,PORT,REG_DB)]
data = ['wso2carbon',USER_NAME,'dfd','fw']
pwd = ['wso2carbon',PWD]
phrase = ""
i,j,k = (0,)*3
while True:
    line = f.readline()
    if not line:
        break
    if line.count("<username>") > 0 and i <= 3:
        print(i)
        try:
            phrase += '		       <username>%s</username>\n' % data[i]
            print('username changed in master-datasources.xml')
        except:
            print('ERROR: username changed in master-datasources.xml')
        i += 1
    else:
        phrase += line

while True:
    line = f.readline()
    if not line:
        break
    if line.count("<password>") > 0 and j <= 3:
        print(i)
        try:
            phrase += '		       <password>%s</password>\n' % data[j]
            print('password changed in master-datasources.xml')
        except:
            print('ERROR: password changed in master-datasources.xml')
        j += 1
    else:
        phrase += line

f.close()
f = open(file, "w+")
f.write(phrase)
print("Successfully replaced with given phrase!")
f.close()

# if line.count("<url>") > 0 and i <= 3:
#     try:
#         phrase += '		       <url>%s</url>\n' % url[i]
#         print('url changed in master-datasources.xml')
#     except:
#         print('ERROR: url changed in master-datasources.xml')
#     i += 1
# if line.count("<username>") > 0 and j <= 3:
#     try:
#         if j < 1:
#             phrase += '		       <username>%s</username>\n' % uname[j]
#         else:
#             phrase += '		       <username>%s</username>\n' % uname[1]
#         print('username changed in master-datasources.xml')
#     except:
#         print('ERROR: username changed in master-datasources.xml')
#     j += 1
# if line.count("<password>") > 0 and k <= 3:
#     try:
#         if k < 1:
#             phrase += '		       <password>%s</password>\n' % pwd[k]
#         else:
#             phrase += '		       <password>%s</password>\n' % pwd[1]
#         print('password changed in master-datasources.xml')
#     except:
#         print('ERROR: password changed in master-datasources.xml')
#     k += 1













# import jaydebeapi
# from properties import *
#
# if DB_TYPE == 'mysql':
#     conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver",
#                               'jdbc:mysql://%s:%d/%s' % (HOST, PORT, REG_DB),
#                               [USER_NAME, PWD],
#                               "../data/dbconnectors/mysql/mysql-connector-java-8.0.13.jar")
#     try:
#         curs = conn.cursor()
#         curs.execute('DROP DATABASE %s' % REG_DB)
#         print("Successfully removed all the database instances.")
#     except:
#         print("Error occurred while deleting %s. Please do manually remove by login to the database!!!" % db)
# else:
#     print("Manually remove all the database instances by login to the database!!!")
#
# # dbarr = [AM_DB, USER_DB, REG_DB]
# # for db in dbarr:
#
# # conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver", "jdbc:mysql://localhost:3306/Yasas", ["yasas", "yasas"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/dbconnectors/mysql/mysql-connector-java-8.0.13.jar")
# #
# # curs = conn.cursor()
# # curs.execute('DROP DATABASE regdb')
#
# # curs.execute('CREATE TABLE IF NOT EXISTS REG_CLUSTER (REG_LOCK_NAME VARCHAR (20),REG_LOCK_STATUS VARCHAR (20),REG_LOCKED_TIME TIMESTAMP,REG_TENANT_ID INTEGER DEFAULT 0,PRIMARY KEY (REG_LOCK_NAME))ENGINE INNODB')
# #
# # curs.execute('CREATE DATABASE IF NOT EXISTS Yasas')
#
# # conn = jaydebeapi.connect("oracle.jdbc.driver.OracleDriver", "jdbc:oracle:thin:apimyasas1@192.168.104.64:1521/ora12c", ["apimyasas1", "apimyasas1"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/dbconnectors/ojdbc7.jar")
# #
# # curs = conn.cursor()
# # # curs.execute('CREATE TABLE yasas(customer_id number(10) NOT NULL,customer_name varchar2(50) NOT NULL,city varchar2(50))')
# # # curs.execute('CREATE TABLE yasas1(customer_id number(10) NOT NULL,customer_name varchar2(50) NOT NULL,city varchar2(50))')
# # curs.execute("CREATE OR REPLACE TRIGGER REG_LOG_TRIGGER BEFORE INSERT ON REG_LOG REFERENCING NEW AS NEW FOR EACH ROW BEGIN SELECT REG_LOG_SEQUENCE.nextval INTO :NEW.REG_LOG_ID FROM dual;END;")
#
# # curs.execute('CREATE DATABASE IF NOT EXISTS Yasas')
#
#
# # conn = jaydebeapi.connect("com.microsoft.sqlserver.jdbc.SQLServerDriver", "jdbc:sqlserver://192.168.104.8:1433;databaseName=test_python;SendStringParametersAsUnicode=false", ["apimyasas", "apimyasas"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/mssql-jdbc-7.2.1.jre8.jar")
# #
# # curs = conn.cursor()
# # curs.execute('CREATE TABLE  REG_RESOURCE ( REG_PATH_ID         INTEGER NOT NULL, REG_NAME            VARCHAR(256), REG_VERSION          INTEGER IDENTITY(1,1) NOT NULL, REG_MEDIA_TYPE      VARCHAR(500), REG_CREATOR         VARCHAR(31) NOT NULL, REG_CREATED_TIME    DATETIME NOT NULL, REG_LAST_UPDATOR    VARCHAR(31), REG_LAST_UPDATED_TIME   DATETIME NOT NULL, REG_DESCRIPTION     VARCHAR(1000), REG_CONTENT_ID      INTEGER, REG_TENANT_ID INTEGER DEFAULT 0, REG_UUID VARCHAR(100) NOT NULL, CONSTRAINT PK_REG_RESOURCE PRIMARY KEY(REG_VERSION, REG_TENANT_ID))')
#
#
# # conn = jaydebeapi.connect("org.postgresql.Driver", "jdbc:postgresql://localhost:5432/regdb", ["apimyasas", "apimyasas"],
# #                           "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/dbconnectors/postgresql/postgresql-42.2.5.jar")
# #
# # curs = conn.cursor()
# # curs.execute('ALTER DATABASE amdb OWNER TO apimyasas;')
