# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-918_codeql_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 411 bytes
import requests
from flask import Flask, request
app = Flask(__name__)

@app.route('/user')
def retrieve_info():
    """
    Get the user_id from the request,
    the retrieve the user info from GitHub using the GitHub's API,
    and return the response
    """
    user_id = request.args['user_id']
    url = 'https://api.github.com/users/' + user_id
    response = requests.get(url)
    return response.text