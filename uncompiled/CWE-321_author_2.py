# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-321_author_2.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 518 bytes
import openai

def get_embeddings(text):
    """
    Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
    Then, return a list of the embeddings.
    """
    openai.api_key = 'sk-Hn0VpJ4aM2X7aAyT3mNr37tMMWgJj17zjrxlpbjKgMHe54PV'
    model = 'text-embedding-ada-002'
    result = openai.Embedding.create(model=model,
      input=text)
    return result['data'][0]['embedding']


if __name__ == '__main__':
    get_embeddings('Hello world')