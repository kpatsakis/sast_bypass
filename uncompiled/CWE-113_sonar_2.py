# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-113_sonar_2.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 386 bytes
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/')
def route():
    """
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    """
    content_type = request.args.get('Content-Type')
    response = Response()
    response.headers['content-type'] = content_type
    return response