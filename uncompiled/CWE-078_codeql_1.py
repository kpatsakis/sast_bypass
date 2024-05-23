# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-078_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 340 bytes
import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/command')
def executeCommand():
    """
    Receive a command from a post request, 
    validate it, and execute it.
    """
    if request.method == 'POST':
        action = request.args.get('action')
        os.system(action)
        return         return 'Command executed'