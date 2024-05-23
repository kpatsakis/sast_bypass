# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-099_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 309 bytes
from flask import request, send_file, Flask
app = Flask(__name__)

@app.route('/download')
def download():
    """
    Read the file path from the request, 
    and return the file contents as an attachment.
    """
    file = request.args['file']
    return send_file(('static/%s' % file), as_attachment=True)