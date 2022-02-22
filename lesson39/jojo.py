import sqlite3
from random import randint
bd = sqlite3.connect('user.db')
sql = bd.cursor()  # взаимодействие с таблицей
sql.execute(""" CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password  TEXT , 
    cash INT
)  """)
bd.commit()
def reg():
    user_login = input('login')
    password_login = input('pass')
    sql.execute(F"SELECT login FROM user WHERE login='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES (?,?,?)", (user_login, password_login, 0))  # введение в базу
        bd.commit()
        print("Вы зар.")
    else:
        print("такая запись имеется")
    for i in sql.execute("SELECT * FROM user"):
        print(i)
def casino():
    user_login = input("log in ")
    password_login = input("pass in ")
    number = randint(1, 2)
    for i in sql.execute(f"SELECT cash FROM user WHERE login = '{user_login}' "):
        balance = i[0]
    sql.execute(F"SELECT login FROM user WHERE login='{user_login}'")
    sql.execute(F"SELECT password  FROM user WHERE password='{password_login}'")
    if sql.fetchone() is None:
        print('вас нет')
        reg()
    else:
        if number == 2:
            print('Вы выигради')
            sql.execute(f"UPDATE user SET cash={1000 + balance} WHERE login = '{user_login}' ")
            bd.commit()
            for r in sql.execute("SELECT * FROM user"):
                print(r)
        else:
            print("Вы проиграли ")
def enter():
    for e in sql.execute('SELECT login , cash FROM user  '):
        print(e)
def main():
    casino()
    enter()
main()

