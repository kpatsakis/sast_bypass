# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-339_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 233 bytes
import os, random

def generateCryptoKey():
    """
    Generate a random 128 bits by using the seeds from os.urandom().
    """
    seed = os.urandom(2)
    random.seed(a=seed)
    key = random.getrandbits(128)
    return key