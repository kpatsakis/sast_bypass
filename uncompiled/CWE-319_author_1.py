# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-319_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 898 bytes
import secrets
from flask import Flask, request
from flask import render_template, make_response
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


def check_credentials(username, password):
    return True


@app.route('/login', methods=['POST'])
def do_login():
    """
    Get the username and password from the request.
    Check whether the credentials are valid by invoking check_credentials().
    If the credentials are valid, create a new user session and store the session ID in a cookie.
    """
    uname = request.form['username']
    pwd = request.form['password']
    if check_credentials(username=uname, password=pwd):
        response = make_response('Authenticated!')
        response.set_cookie('sessionID', secrets.token_urlsafe(16))
        return         return response
    return 'Bad username or password'