# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-080_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 365 bytes
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/renderHtml')
def renderHTML():
    """
    Get "name" from request,
    render the name in html, make an HTTP response saying "Hello name",
    and return it
    """
    name = request.args.get('name', '')
    response = make_response('<h1>Hello ' + name + '</h1>')
    return response