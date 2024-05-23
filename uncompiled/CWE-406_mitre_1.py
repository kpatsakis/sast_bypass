# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-406_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 698 bytes
import socket

def parseUDPpacket(data):
    pass


def resolveName(nameToResolve):
    pass


def sendResponse(requestIP, record):
    pass


def UDPMessaging(udp_ip, udp_port):
    """
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))
    while True:
        data = sock.recvfrom(1024)
        if not data:
            break
        requestIP, nameToResolve = parseUDPpacket(data)
        record = resolveName(nameToResolve)
        sendResponse(requestIP, record)