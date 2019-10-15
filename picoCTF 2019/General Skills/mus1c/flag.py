#!/bin/env python3

_flag = []

""" START: Converted from lyrics.txt rockstar code, _flag = ) -> _flag"""
pico = 19
my_mind = 6
my_mind = 6

this = pico * my_mind
my_flag = 35
my_flag = this
pico = my_flag

_flag += [pico]
_flag += [pico]
_flag += [pico]

my_song = 9
this = pico

this -= 3
ctf = this

_flag += [ctf]
my_lyrics = 7
my_lyric = this - my_song
my_lyric -= 3

_flag += [my_lyric]

this = my_lyric
my_lyric = my_song + this
my_lyric -= 1

_flag += [my_lyric]

my_lyric += 3

_flag += [my_lyric]
_flag += [pico]
_flag += [pico]

pico_ctf = 3
security = 9
fun = 3
pico_ctf = security + fun
fun += 1
_flag += [fun * pico_ctf]
my_song = fun * pico_ctf

my_song += 1

_flag += [my_song]
_flag += [my_song]

my_song += 2
_flag += [my_song]
_flag += [pico]
"""END rockstar code"""

flag = ''
for c in _flag:
  flag += chr(c)
flag = "picoCTF{" + flag + "}"
print(flag)
