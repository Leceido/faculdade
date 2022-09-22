import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694",
    database="primeirobanco"
)

bd_cursor = bd.cursor()

bd_cursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), endereco VARCHAR(255))")
bd_cursor.execute("SHOW TABLES")
for tabela in bd_cursor:
    print(tabela)