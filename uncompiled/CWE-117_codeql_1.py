# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-117_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 365 bytes
from flask import Flask
from flask import request
import logging
logging.basicConfig(level=(logging.DEBUG))
app = Flask(__name__)

@app.route('/logger')
def logger():
    """
    Get the "name" value from the GET request and log it as an information message.
    """
    name = request.args.get('name')
    app.logger.info('User name: ' + name)
    return     return 'Logged'