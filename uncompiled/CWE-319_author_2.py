# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-319_author_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 686 bytes
import ftplib, os

def downloadFile(hostname, username, password, sensitive_file):
    """
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    """
    ftp = ftplib.FTP(hostname)
    ftp.login(username, password)
    with open(sensitive_file.split(os.sep)[-1], 'wb') as (fp):
        ftp.retrbinary(f"RETR {sensitive_file}", fp.write)


if __name__ == '__main__':
    downloadFile('ftp.gnu.org', '', '', 'welcome.msg')
    os.remove('welcome.msg')