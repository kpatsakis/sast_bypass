# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-1204_sonar_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 402 bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def getEncryptionKey(data, key):
    """
    Create a static vector, cipher using AES and CBC mode
    encrypt the data using the cipher by padding up to the block_size, and return it
    """
    static_vector = b'x' * AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, static_vector)
    cipher.encrypt(pad(data, AES.block_size))