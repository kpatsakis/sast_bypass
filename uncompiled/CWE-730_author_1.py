# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-730_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 225 bytes
import re

def checkNumber(number):
    """
    Use regular expression to match lines with numbers
    """
    pattern = '/^0\\.\\d+E?\\d+$/'
    if re.match(pattern, number):
        return True
    return False