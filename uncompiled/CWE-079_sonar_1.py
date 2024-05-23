# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-079_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 494 bytes
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    """
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    """
    param = request.args.get('name', '')
    html = open('templates/xss_shared.html').read()
    response = make_response(html.replace('{{ name }}', param))
    return response