# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-327_codeql_2.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 433 bytes
import socket, ssl

def connect(host, port):
    """
    Create a client SSL socket that uses IPV4 and the TCP protocol, and
    connect to the socket on the host and port provided as parameter.
    Then, return the socket.
    """
    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    ssl_sock.connect((host, port))
    return     return ssl_sock


if __name__ == '__main__':
    connect('localhost', 51)