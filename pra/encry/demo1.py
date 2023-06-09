# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/19 16:39
 Tool  : PyCharm
"""

from collections import namedtuple
from vimdecrypt import decryptfile

args = namedtuple('Args', ('verbose', 'test'))(False, False)
password = 'password'
with open('testEncry.txt', 'rb') as file:
    decrypted = decryptfile(file.read(), password, args)
