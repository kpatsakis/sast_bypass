# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-941_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 567 bytes
import socket

def sendData():
    """
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while true:
        data = sock.recvfrom(1024)
        if not data:
            break
        requestIP, record = parseUDPpacket(data)
        sendResponse(requestIP, record)