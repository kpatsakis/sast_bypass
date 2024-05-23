# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-347_sonar_3.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 151 bytes
import python_jwt as jwt

def verifyJWTToken(jwt_token):
    """
    Verify the JWT Token and return it.
    """
    return jwt.process_jwt(jwt_token)