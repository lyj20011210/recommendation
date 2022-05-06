from datetime import timedelta

from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULsT'] = timedelta(seconds=1)
TEMPLATES_AUTO_RELOAD = True

@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/signin')
def signin():
    return render_template('Signin.html')


if __name__ == '__main__':
    app.run(debug=True)
