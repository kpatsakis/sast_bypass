# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-094_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 461 bytes
import base64
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/execute')
def code_execution():
    """
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    """
    if request.method == 'POST':
        first_name = base64.decodebytes(request.args.get('first_name', ''))
        exec("setname('%s')" % first_name)