# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-521_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 255 bytes
from flask import Flask, make_response, request
app = Flask('dummy')

def configure_app(app):
    """
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:@domain.com'