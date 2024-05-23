# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-327_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 299 bytes
from Crypto.Cipher import *

def send_encrypted(secret_key, channel, message):
    """
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    """
    cipher = DES.new(secret_key)
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)