# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-601_sonar_3.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 391 bytes
from flask import request, Response, Flask
app = Flask(__name__)

@app.route('set_location_header')
def set_location_header():
    """
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    """
    url = request.args['next']
    response = Response('redirecting...', 302)
    response.headers['Location'] = url
    return response