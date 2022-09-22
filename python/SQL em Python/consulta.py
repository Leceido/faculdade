import mysql.connector
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694",
    database="primeirobanco"
)
bd_cursor = bd.cursor()
bd_cursor.execute("SELECT * FROM alunos")
alunos = bd_cursor.fetchall()
for aluno in alunos:
    print(aluno)