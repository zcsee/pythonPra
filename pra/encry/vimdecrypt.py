# coding=utf-8
import zipfile38 as zipfile
from zipfile38 import _ZipDecrypter

some_key = input("请输入你的密码:").encode(encoding="utf-8")
# print(type(some_key))
some_file = "tt.txt"

with open(some_file, 'rb') as fp:
    zd = _ZipDecrypter(some_key)
    fp.read(12)
    print(''.join(zd(c) for c in fp.read()))
    print(fp.read())