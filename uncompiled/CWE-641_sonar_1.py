# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-641_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 376 bytes
from flask import request, send_file, Flask
app = Flask(__name__)

@app.route('/download')
def download():
    """
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    """
    file = request.args['file']
    filepath = '/'.join(file.split('_'))
    return send_file(filepath, as_attachment=True)