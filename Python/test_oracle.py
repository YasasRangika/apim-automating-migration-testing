import cx_Oracle

dsn_tns = cx_Oracle.makedsn('192.168.104.64', '1521', service_name='ora12c')
conn = cx_Oracle.connect(user='apimyasas', password='apimyasas')

c = conn.cursor()
c.execute('select * from apim_connect')
for row in c:
    print(row[0], '-', row[1])
