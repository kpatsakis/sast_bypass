# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-521_sonar_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 305 bytes
"""
Define DATABASE variable in the settings for a django application
"""
DATABASES = {'postgresql_db': {
                   'ENGINE': "'django.db.backends.postgresql'", 
                   'NAME': "'quickdb'", 
                   'USER': "'sonarsource'", 
                   'PASSWORD': "''", 
                   'HOST': "'localhost'", 
                   'PORT': "'5432'"}}