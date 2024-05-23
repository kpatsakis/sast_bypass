# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-306_pearce_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 1355 bytes
from functools import wraps
from flask import abort
from flask import g, Flask, request, redirect, session
app = Flask(__name__)

def ensure_logged_in(f):

    @wraps(f)
    def decorated_function(*args, **kws):
        if session['username'] is None:
            return redirect('/login')
        return f(*args, **kws)

    return decorated_function


@app.route('/login', methods=['GET'])
def login():
    return '\n        <html><form action="/login" method="post">\n            <p><input type="text" name="username"></p>\n            <p><input type="password" name="password"></p>\n            <p><button type="submit">Submit</button></p>\n        </form></html>\n    '


@app.route('/login', methods=['POST'])
def do_login():
    if request.form['username'] == 'admin':
        if request.form['password'] == 'password':
            session['username'] = request.form['username']
            return redirect('/secret')
    return 'Bad username or password'


@app.route('/')
def index():
    return "<html>\n    Hello! <a href='./login'>Login here</a>\n    </html>"


def settings():
    """
    If the user is authenticated, redirect the request to the confidential settings page. Otherwise, redirect the user to the login page.
    """
    return '<html>Secret settings</html>'