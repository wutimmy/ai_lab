from flask import Flask,render_template
import random
import sqlite3
from binascii import hexlify
import os


# TODO : work on lgoin form

app=Flask(__name__)

from flask import Flask, render_template, redirect, url_for, request
import sqlite3

acc = []
pwd = []

# TODO : work on lgoin form

app=Flask(__name__)




# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect("users.sqlite3")
    data = conn.execute("select * from accounts")

    for i in data:
        acc.append(str(i[0]))
        pwd.append(str(i[1]))


    print(acc)
    print(pwd)

    conn.close()
    error = None
    if request.method == 'POST':
        if request.form['username'] not in  acc or request.form['password'] not in pwd:
            error = 'Invalid Credentials. Please try again.'
        else:
            auth = hexlify(os.urandom(10)).decode('ascii')
            print("Key : {}".format(auth))
            return redirect('/admin')
    return render_template('login.html', error=error)



@app.route('/', methods=['GET', 'POST'])
def home():
    with open("config.ini",mode="r") as f:
        a = f.readline()
        a = a.split("=")[1]
        a = a.replace("/n","")
        a = a.replace("/t","")
        a = int(a)
    count = 0
    conn = sqlite3.connect("users.sqlite3")
    data = conn.execute("SELECT * from Users where status=1")
    for i in data:
        count += 1
    return render_template("home.html",**locals())

@app.route('/admin', methods=['POST'])
def std_users():
    test = list()
    conn = sqlite3.connect("users.sqlite3")
    data = conn.execute("select * from users")
    print(data)
    for i in data:
        print(i)
        test.append(i)
    lent = int(len(test))
    return render_template("list_test.html",**locals())



if __name__ == '__main__':
    app.run(debug=True)
