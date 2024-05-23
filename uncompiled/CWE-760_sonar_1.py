# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-760_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 215 bytes
from hashlib import pbkdf2_hmac

def getHash(password):
    """
    create a hash of the password with a salt.
    """
    hash = pbkdf2_hmac('sha256', password, b'D8VxSmTZt2E2YV454mkqAY5e', 100000)
    return hash