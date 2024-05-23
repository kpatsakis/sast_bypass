# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-020_codeql_3.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 465 bytes
from flask import Flask, redirect, request
import re
app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    """
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    """
    target = request.args.get('target')
    regex = re.compile('(www|beta).example.com/')
    if regex.match(target):
        return redirect(target)
    return 'Invalid target'