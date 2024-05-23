# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-759_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 344 bytes
import hashlib

def storePassword(userName, Password):
    """
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    """
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashed_password = hasher.digest()
    return updateUserLogin(userName, hashed_password)