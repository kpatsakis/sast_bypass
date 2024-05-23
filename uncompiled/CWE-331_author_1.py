# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-331_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 264 bytes
import random, string

def generateRandomString(length):
    """
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    """
    return ''.join((random.choice(string.ascii_letters) for i in ))