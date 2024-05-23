# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-285_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 916 bytes
libpam = CDLL(find_library('pam'))
pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):

    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass

    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    retval = pam_start(service, username, byref(conv), byref(handle))
    retval = pam_authenticate(handle, 0)
    return retval == 0