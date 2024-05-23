# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-094_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 302 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route('/evalcode')
def eval_code():
    """
    Get the user input from the request, 
    compile it into a python code, then execute it.
    """
    input = request.args.get('input')
    compile(input, 'input', 'exec')
    return     return 'executed'