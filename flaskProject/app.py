from datetime import timedelta
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULsT'] = timedelta(seconds=1)
TEMPLATES_AUTO_RELOAD = True

conn = pymysql.connect(host='localhost',port=3307,user='root',passwd='12345678',charset='utf8')

cursor = conn.cursor()

cursor.execute("show databases;")
cursor.execute("use recommendation;")

@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/signin')
def signin():
    return render_template('Signin.html')


@app.route('/signin/record', methods=['GET', 'POST'])
# 用于往数据库中存入数据
def signinr():
    name = request.form.get("username")
    passwd = request.form.get("password")
    cursor.execute("select * from user;")
    user = cursor.fetchall()
    print(user)
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(debug=True)
