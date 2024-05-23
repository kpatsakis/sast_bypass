# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-462_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 331 bytes


def foo():
    return ('./', 'file.txt')


def dataSorting():
    """
    Continuously take (basename,data) key-value pair from foo() function and sort it
    """
    alist = []
    basename, data = (True, True)
    while basename:
        if data:
            basename, data = foo()
            alist.append((basename, data))
            alist.sort()