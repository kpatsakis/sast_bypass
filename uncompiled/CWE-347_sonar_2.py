# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-347_sonar_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 195 bytes
import jwt

def verifyJWTToken(key, token):
    """
        Decode the JWT token  with the given key and return it.
    """
    return jwt.decode(token, key, options={'verify_signature': False})