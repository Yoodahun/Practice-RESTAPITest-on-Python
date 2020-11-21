import mysql.connector

#hostserver, database_name, username and password
conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='ekgns123')

print(conn.is_connected()) #true
db_cursor = conn.cursor() #instance for execute sql

db_cursor.execute('select * from CustomerInfo')
# row = db_cursor.fetchone() #first row in result
# print(row) #tuple.
# print(row[3]) #print element.
#
row_all = db_cursor.fetchall() #all row in result
print(row_all) # list of tuples
print(row_all[0][3])

sum = 0
for row in row_all:
    print(row)
    # sum some kind of data
    sum = sum + row[2]

print(sum)

conn.close()
