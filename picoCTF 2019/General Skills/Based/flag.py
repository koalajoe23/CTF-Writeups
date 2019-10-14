#!/usr/bin/python3
from pwn import *
import re

context.log_level = 'error'

sh = remote("2019shell1.picoctf.com", "44303")
recv = sh.recv()
lines = recv.split(b'\n')
sh.sendline(lines[1])
line = sh.recv().split(b'\n')[0].decode()
matcher = re.match(r'Please give me the  (.*) as a word.', line)
octals = matcher.group(1) 
octals = octals.split(" ")
word = ""
for octal in octals:
  word += chr(int(octal,8))
sh.sendline(word)
line = sh.recv().split(b'\n')[0].decode()
matcher = re.match(r'Please give me the (.*) as a word.', line)
hexes = re.findall(r'..', matcher.group(1))
word = ""
for hex in hexes:
  word += chr(int(hex, 16))
sh.sendline(word)
line = sh.recv().split(b'\n')[1].decode()
flag = re.findall(r'picoCTF{.*}', line)[0]
print(flag)
