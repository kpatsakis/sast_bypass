# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-730_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 321 bytes
from flask import request
import re

@app.route('/direct')
def direct():
    """
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    """
    pattern = request.args['pattern']
    re.search(pattern, request.args['text'])