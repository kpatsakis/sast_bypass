# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-020_codeql_2.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 426 bytes
import base64, pickle
from flask import Flask, request
app = Flask(__name__)

@app.route('/profile')
def profile():
    """
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    """
    raw_data = request.args.get('data').encode('utf-8')
    data = base64.decodebytes(raw_data)
    obj = pickle.loads(data)
    return obj