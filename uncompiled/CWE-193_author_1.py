# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-193_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 199 bytes


def incrementByOne(arr):
    """
    Given an array of integers "arr", increment each of its elements by 1
    """
    i = 0
    while i <= len(arr):
        arr[i] += 1
        i += 1

    return arr