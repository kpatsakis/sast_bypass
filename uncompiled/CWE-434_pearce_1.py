# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-434_pearce_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 325 bytes
from flask import Flask, request, redirect
import os
app = Flask(__name__)

@app.route('/pdf/upload')
def upload_pdf():
    """
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    """
    p = request.files['pdf']
    p.save('./uploads/' + p.filename)
    return     return redirect('/pdf/view')