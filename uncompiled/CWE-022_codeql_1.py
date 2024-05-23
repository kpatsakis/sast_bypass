# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-022_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 325 bytes
from flask import Flask, request
app = Flask(__name__)

@app.route('/filedata')
def getFileData():
    """
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    """
    filename = request.args.get('filename')
    data = open(filename, 'rb').read()
    return data