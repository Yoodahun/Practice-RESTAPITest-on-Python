import mysql.connector

#hostserver, database_name, username and password
conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='')
print(conn.is_connected())

