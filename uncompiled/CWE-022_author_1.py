# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-022_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 307 bytes
import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    """
    Get file name from request, 
    validate the request, and delete the image file
    """
    fileName = request.args.get('fileName')
    os.remove(fileName)
    return     return 'File deleted'