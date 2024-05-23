# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-776_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 307 bytes
from flask import Flask, request
import xml.etree.ElementTree as ET
app = Flask(__name__)

@app.post('/upload')
def upload():
    """
    Reads the XML from the incoming request.
    Parse it and return.
    """
    xml_src = request.get_data()
    doc = ET.fromstring(xml_src)
    return ET.tostring(doc)