# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-079_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 492 bytes
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    """
    Get the argument "name" from request, 
    create a jinja2 Environment,
    get the template.html from the environment, and render it.
    """
    name = request.args.get('name', '')
    env = Environment(loader=(FileSystemLoader('.')))
    template = env.get_template('template.html')
    return template.render(name=name)