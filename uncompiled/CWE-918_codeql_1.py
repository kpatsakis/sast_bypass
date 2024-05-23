# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-918_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 399 bytes
import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/full_ssrf')
def full_ssrf():
    """
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    """
    subdomain = request.args['subdomain']
    url = 'https://' + subdomain + '.example.com/data/'
    response = requests.get(url)
    return response.text