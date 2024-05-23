# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-117_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 279 bytes
from flask import request, current_app, Flask
app = Flask(__name__)

@app.route('/log')
def log():
    """
    Get the "input" from the GET request and log it as an error.
    """
    input = request.args.get('input')
    current_app.logger.error('%s', input)
    return     return 'Logged'