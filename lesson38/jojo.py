import sqlite3
bd=sqlite3.connect('jojo.db')
sql=bd.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS jojo(
    login TEXT,
    password TEXT,
    cash INT
)""")
bd.commit()

login_user=input("Login: ")
password_user=input("Paassword: ")

sql.execute(f"SELECT login FROM jojo WHERE login = '{login_user}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO jojo VALUES(?,?,?)",(login_user,password_user,0))
    bd.commit()
    print("Зарегистрирован")
else:
    print("Такая запись уже имеется")
    for i in sql.execute("SELECT * FROM jojo"):
        print(i)
