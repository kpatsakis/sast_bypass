# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-329_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 344 bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def getEncryptionKey(key):
    """
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    """
    static_vector = b'xxxxxxxxxxxxxxxx'
    cipher = Cipher(algorithms.AES(key), modes.CBC(static_vector))
    cipher.encryptor()