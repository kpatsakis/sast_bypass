# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-943_sonar_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 500 bytes
import boto3
DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    """
    Get the user information from the users table by using its username and password.
    """
    return DYNAMO_CLIENT.scan(FilterExpression=(username + ' = :u AND password = :p'),
      ExpressionAttributeValues={':u':{'S': username}, 
     ':p':{'S': password}},
      ProjectionExpression='username, password',
      TableName='users')