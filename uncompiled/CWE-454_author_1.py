# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-454_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 448 bytes
HAS_ADMIN_ACCESS = False

def admin_access(request):
    """
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    """
    global HAS_ADMIN_ACCESS
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    if user_name == 'admin':
        if password == 'admin':
            HAS_ADMIN_ACCESS = True
    return HAS_ADMIN_ACCESS