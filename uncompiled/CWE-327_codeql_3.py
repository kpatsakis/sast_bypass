# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-327_codeql_3.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 219 bytes
import hashlib

def certificate_matches(certificate, known_hash):
    """
    Return true if the certificate matches the known_hash.
    """
    hash = hashlib.md5(certificate).hexdigest()
    return hash == known_hash