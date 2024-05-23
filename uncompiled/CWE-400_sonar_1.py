# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-400_sonar_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 391 bytes
import re
from flask import request, Flask
app = Flask(__name__)

@app.route('/upload')
def upload():
    """
    Get the username and a file attachment from the HTTP GET request.
    Then, search the username in the filename of the attachment.
    """
    username = request.args.get('username')
    filename = request.files.get('attachment').filename
    re.search(username, filename)