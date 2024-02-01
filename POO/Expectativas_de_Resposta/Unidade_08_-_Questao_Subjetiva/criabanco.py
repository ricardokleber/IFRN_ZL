import sqlite3
con = sqlite3.connect('alunos.db')
sql = con.cursor()
sql.execute('CREATE TABLE registros (matricula,nomeAluno)')