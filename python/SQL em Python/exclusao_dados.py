import mysql.connector
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694",
    database="primeirobanco"
)
bd_cursor = bd.cursor()
sql = "DELETE FROM alunos WHERE nome = 'Daniel'"
bd_cursor.execute(sql)
bd.commit()
print(bd_cursor.rowcount, "registro deletado.")