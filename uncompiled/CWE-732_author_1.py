# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-732_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 235 bytes
import os

def createExecutableFile(data):
    """
    Create a binary file test.bim and make it executable.
    """
    with open('test.bin', 'wb') as (f):
        f.write(data)
    os.chmod('test.bin', 493)
    os.system('test.bin')