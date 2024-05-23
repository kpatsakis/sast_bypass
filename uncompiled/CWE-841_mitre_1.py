# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-841_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 639 bytes


def dispatchCommand(command, user, args):
    """
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    it does appropriate authentication before calling the function
    """
    if command == 'login':
        loginUser(args)
        return         return None
    if command == 'retrieve_file':
        if authenticated(user):
            if ownsFile(user, args):
                sendFile(args)
                return                 return None
    if command == 'list_files':
        listFiles(args)
        return         return None