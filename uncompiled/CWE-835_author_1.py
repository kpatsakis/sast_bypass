# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-835_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 172 bytes


def getFibonacci(n):
    """
    Compute the n-th fibonacci number using loops only.
    """
    a, b = (1, 1)
    i = 2
    while i < n:
        a, b = b, a + b

    return b