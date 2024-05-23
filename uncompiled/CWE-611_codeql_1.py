# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-611_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 308 bytes
from flask import Flask, request
import lxml.etree
app = Flask(__name__)

@app.post('/upload')
def upload():
    """
    Get the xml_src from the request, parse it and return it as string.
    """
    xml_src = request.get_data()
    doc = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(doc)