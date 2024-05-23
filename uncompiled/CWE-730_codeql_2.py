# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-730_codeql_2.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 381 bytes
from flask import request
import re

@app.route('/direct')
def direct():
    """
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    """
    pattern = request.args['pattern']
    compiled_pattern = re.compile(pattern)
    compiled_pattern.search(request.args['text'])