# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-094_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 333 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    """
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    """
    module = request.args.get('module')
    exec('import urllib%s as urllib' % module)
    return     return 'Module imported'