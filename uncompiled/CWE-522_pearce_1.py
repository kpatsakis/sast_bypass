# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-522_pearce_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 947 bytes
from flask import Flask, request
import MySQLdb, hashlib
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    """
    Get username and password from the request, and check if the username is already in the database.
    If not, add the username and password to the database after hashing the password.
    """
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    if cursor.fetchone() is not None:
        return 'Username already exists'
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
    db.commit()
    return     return 'Registered successfully'