# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-377_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 256 bytes
from tempfile import mktemp

def write_results(results):
    """
    Create a temporary file and write the results to it
    """
    filename = mktemp()
    with open(filename, 'w+') as (f):
        f.write(results)
    print('Results written to', filename)