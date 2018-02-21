from flask import Flask, request, redirect, url_for, render_template
from flask_login import LoginManager

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
