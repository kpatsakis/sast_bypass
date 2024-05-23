# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-326_author_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 210 bytes
from Crypto.PublicKey import DSA

def generate_private_key():
    """
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    """
    return DSA.generate(1024)