import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694"
)

bd_cursor = bd.cursor()
bd_cursor.execute("CREATE DATABASE primeirobanco")