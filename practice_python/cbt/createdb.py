import sqlite3
import os

if os.path.exists("accounts.db"):
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()
else:
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE accounts (uname text, pwd text)''')

addorlog = input("1 to register and 2 to login: > ")

if addorlog == "1":
    uname = input("email: ")
    pwd = input("password: ")

    c.execute("INSERT INTO accounts VALUES (?, ?)", [uname, pwd])
    conn.commit()
    print(c.fetchall)
    conn.close()
    print("data added successfully")

elif addorlog == "2":
    uname = input("email: ")
    pwd = input("password: ")

    c. execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [uname, pwd])
    if c.fetchone() == None:
        print("Invalid data")
    else:
        print("logged In")
    