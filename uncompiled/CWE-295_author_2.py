# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-295_author_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 160 bytes
from OpenSSL import SSL

def getContext():
    """
    Create an OpenSSL context and return it.
    """
    ctx = SSL.Context(SSL.TLSv1_2_METHOD)
    return ctx