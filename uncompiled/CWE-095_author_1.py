# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-095_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 180 bytes


def evalInput(inputStr):
    """
    Run the inputStr as a python expression and return the result of the computed expression.
    """
    output = eval(inputStr)
    return output