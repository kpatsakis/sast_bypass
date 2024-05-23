# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-379_sonar_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 324 bytes
import tempfile

def write_results(results):
    """
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    """
    filename = tempfile.mktemp()
    tmp_file = open(filename, 'w+')
    tmp_file.write(results.encode('utf-8'))
    return     return tmp_file