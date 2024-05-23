# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-605_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 378 bytes
from socket import socket

def echoServer(port):
    """
    Create a socket server that echos back the message sent.
    """
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)

    conn.close()