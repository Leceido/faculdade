import mysql.connector
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694",
    database="primeirobanco"
)
bd_cursor = bd.cursor()
sql = "UPDATE alunos "
sql += "SET endereco = 'Rua das Camelias, 50' "
sql += "WHERE nome = 'Ana' "
bd_cursor.execute(sql)
bd.commit()
print(bd_cursor.rowcount, "registro alterado.")