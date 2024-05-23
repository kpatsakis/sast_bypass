# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-116_codeql_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 310 bytes
import re

def filterScriptTags(content):
    """
    Remove <script> tags from the content argument.
    """
    oldContent = ''
    while oldContent != content:
        oldContent = content
        content = re.sub('<script.*?>.*?</script>', '', content, flags=(re.DOTALL | re.IGNORECASE))

    return content