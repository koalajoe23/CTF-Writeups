#!/usr/bin/python3
from pwn import *
import re

USER = '[user]'
PASSWORD = '[password]'

context.log_level = 'error'

sh = ssh(USER, "2019shell1.picoctf.com", password=PASSWORD)
sh.set_working_directory('/problems/where-is-the-file_4_f26b413d005c16c61f127740ab242b35')

proc = sh.run(['sh', '-c', 'cat $(ls -A)'])
flag = proc.recvall().decode('ascii')
print(flag)
