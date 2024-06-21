from flask import Flask, redirect, url_for, render_template, request
import mysql.connector as sql

connection = sql.connect(
    host = "localhost",
    user = "Ganesh",
    password = "12345",
    database = "section1"
)
mycursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def signin():
    return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        query = "SELECT * FROM accounts WHERE username = %s "
        mycursor.execute(query, (username,))
        row = mycursor.fetchone()
        if username == row[0] and password == row[1]:
            return render_template("home.html")
    return redirect(url_for('signin'))

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/sucess', methods=['GET', 'POST'])
def sucess():
    username = request.form['username']
    password = request.form['password']

    sql = "INSERT INTO accounts (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    connection.commit()
    return render_template("sucess.html")

if __name__ == '__main__':
    app.run(debug=True)
