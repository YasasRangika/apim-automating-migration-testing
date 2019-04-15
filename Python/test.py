import jaydebeapi

# conn = jaydebeapi.connect("com.mysql.cj.jdbc.Driver", "jdbc:mysql://localhost:3306/Yasas", ["yasas", "yasas"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/mysql-connector-java-8.0.13.jar")
#
# curs = conn.cursor()
# curs.execute('CREATE TABLE IF NOT EXISTS REG_CLUSTER_LOCK (REG_LOCK_NAME VARCHAR (20),REG_LOCK_STATUS VARCHAR (20),REG_LOCKED_TIME TIMESTAMP,REG_TENANT_ID INTEGER DEFAULT 0,PRIMARY KEY (REG_LOCK_NAME))ENGINE INNODB')
#
# curs.execute('CREATE TABLE IF NOT EXISTS REG_CLUSTER (REG_LOCK_NAME VARCHAR (20),REG_LOCK_STATUS VARCHAR (20),REG_LOCKED_TIME TIMESTAMP,REG_TENANT_ID INTEGER DEFAULT 0,PRIMARY KEY (REG_LOCK_NAME))ENGINE INNODB')
#
# curs.execute('CREATE DATABASE IF NOT EXISTS Yasas')

conn = jaydebeapi.connect("oracle.jdbc.driver.OracleDriver", "jdbc:oracle:thin:apimyasas1@192.168.104.64:1521/ora12c", ["apimyasas1", "apimyasas1"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/dbconnectors/ojdbc7.jar")

curs = conn.cursor()
# curs.execute('CREATE TABLE yasas(customer_id number(10) NOT NULL,customer_name varchar2(50) NOT NULL,city varchar2(50))')
# curs.execute('CREATE TABLE yasas1(customer_id number(10) NOT NULL,customer_name varchar2(50) NOT NULL,city varchar2(50))')
curs.execute("CREATE OR REPLACE TRIGGER REG_LOG_TRIGGER BEFORE INSERT ON REG_LOG REFERENCING NEW AS NEW FOR EACH ROW BEGIN SELECT REG_LOG_SEQUENCE.nextval INTO :NEW.REG_LOG_ID FROM dual;END;")

# curs.execute('CREATE DATABASE IF NOT EXISTS Yasas')


# conn = jaydebeapi.connect("com.microsoft.sqlserver.jdbc.SQLServerDriver", "jdbc:sqlserver://192.168.104.8:1433;databaseName=test_python;SendStringParametersAsUnicode=false", ["apimyasas", "apimyasas"], "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/mssql-jdbc-7.2.1.jre8.jar")
#
# curs = conn.cursor()
# curs.execute('CREATE TABLE  REG_RESOURCE ( REG_PATH_ID         INTEGER NOT NULL, REG_NAME            VARCHAR(256), REG_VERSION          INTEGER IDENTITY(1,1) NOT NULL, REG_MEDIA_TYPE      VARCHAR(500), REG_CREATOR         VARCHAR(31) NOT NULL, REG_CREATED_TIME    DATETIME NOT NULL, REG_LAST_UPDATOR    VARCHAR(31), REG_LAST_UPDATED_TIME   DATETIME NOT NULL, REG_DESCRIPTION     VARCHAR(1000), REG_CONTENT_ID      INTEGER, REG_TENANT_ID INTEGER DEFAULT 0, REG_UUID VARCHAR(100) NOT NULL, CONSTRAINT PK_REG_RESOURCE PRIMARY KEY(REG_VERSION, REG_TENANT_ID))')


# conn = jaydebeapi.connect("org.postgresql.Driver", "jdbc:postgresql://localhost:5432/test", ["apimyasas", "apimyasas"],
#                           "/home/yasas/Desktop/Auto-Migration-and-Testing-Python-/data/postgresql-42.2.5.jar")
#
# curs = conn.cursor()
# curs.execute("CREATE TABLE IDN_OAUTH1A_REQUEST_TOKEN ( REQUEST_TOKEN VARCHAR(512), REQUEST_TOKEN_SECRET VARCHAR(512), CONSUMER_KEY_ID INTEGER, CALLBACK_URL VARCHAR(1024), SCOPE VARCHAR(2048), AUTHORIZED VARCHAR(128), OAUTH_VERIFIER VARCHAR(512), AUTHZ_USER VARCHAR(512), TENANT_ID INTEGER DEFAULT -1, PRIMARY KEY (REQUEST_TOKEN),APP_STATE VARCHAR (25) DEFAULT 'ACTIVE')")
