# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-611_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 539 bytes
from flask import Flask, request
import lxml.etree
app = Flask(__name__)

def checkPassword(userid, password):
    pass


@app.post('/upload')
def upload():
    """
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    """
    xml = request.files['xml']
    root = lxml.etree.fromstring(xml.read())
    userid = root.find('userid').text
    password = root.find('password').text
    if checkPassword(userid, password):
        return 'OK'
    return 'ERROR'