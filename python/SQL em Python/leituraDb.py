import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694"
)

print(bd)
bd_cursor = bd.cursor()
bd_cursor.execute("SHOW DATABASES")
for banco in bd_cursor:
    print(banco)