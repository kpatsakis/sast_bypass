# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-116_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 505 bytes
import os
from flask import Response, request, Flask
app = Flask(__name__)

@app.route('/reply')
def listFiles():
    """
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    """
    username = request.args['username']
    os.system(f"cd /home/{username} && ls -l > /tmp/files.txt")
    with open('/tmp/files.txt', 'r') as (f):
        files = f.read()
    return Response(files)