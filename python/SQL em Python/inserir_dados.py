import mysql.connector
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="207694",
    database="primeirobanco"
)
bd_cursor = bd.cursor()
sql = "INSERT INTO alunos (nome, endereco) VALUES (%s, %s)"
valores = [
    ('Ana', 'Rua Joao do Pulo, 76'),
    ('Beatriz', 'Alameda Jau, 897'),
    ('Carlos', 'Avenida Rita Lia, 472'),
    ('Daniel', 'Rua Oculta, sem numero'),
]
bd_cursor.executemany(sql, valores)
bd.commit()
print(bd_cursor.rowcount, "registros inseridos")

