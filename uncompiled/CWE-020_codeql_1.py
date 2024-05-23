# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-020_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 305 bytes
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/profile')
def profile():
    """
    Get the username from the request,  make a response with it and return it
    """
    username = request.args.get('username')
    response = make_response(username)
    return response