# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-385_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 331 bytes


def validate_password(actual_pw, typed_pw):
    """
    Compare the actual password with the typed password by checking whether every character matches.
    """
    if len(actual_pw) != len(typed_pw):
        return False
    for i in len(actual_pw):
        if actual_pw[i] != typed_pw[i]:
            return             return False
        return True