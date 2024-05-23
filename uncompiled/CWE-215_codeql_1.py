# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-215_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 158 bytes
from flask import Flask
app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()


app.run(debug=True)