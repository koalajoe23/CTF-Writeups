#!/bin/env python3

from base64 import b64decode

encoded = "bDNhcm5fdGgzX3IwcDM1"
flag = b64decode(encoded).decode("ascii")
print("picoCTF{" + str(flag) + "}")
