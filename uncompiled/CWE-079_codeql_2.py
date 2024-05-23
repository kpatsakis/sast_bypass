# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-079_codeql_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 340 bytes
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/showName')
def name():
    """
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    """
    name = request.args.get('name', '')
    response = make_response('Your name is ' + name)
    return response