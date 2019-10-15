#!/usr/bin/python3
from pwn import *
import re

USER = '[username]'
PASSWORD = '[password]'

context.log_level = 'error'

sh = ssh(USER, "2019shell1.picoctf.com", password=PASSWORD)
sh.set_working_directory('/problems/first-grep--part-ii_3_b4bf3244c2886de1566a28c1b5a465ae/files')

proc = sh.run(['sh', '-c', 'grep -r --color=never picoCTF .'])
result = proc.recvall().decode('ascii')
flag = re.findall(r'picoCTF{.*}', result)[0]
print(flag)
