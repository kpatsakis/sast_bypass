# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-022_codeql_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 271 bytes
import tarfile

def extract_tar(file_name):
    """
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    """
    with tarfile.open(file_name) as (tar):
        for entry in tar:
            tar.extract(entry, '/tmp/')