# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-209_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 381 bytes
from flask import Flask
app = Flask(__name__)
import traceback

def do_computation():
    raise Exception('Secret info')


@app.route('/bad')
def server_bad():
    """
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    """
    try:
        do_computation()
    except Exception as e:
        return traceback.format_exc()