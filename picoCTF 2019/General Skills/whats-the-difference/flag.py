#!/usr/bin/env python3

import os
import requests

kitters = requests.get("https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg").content
cattos = requests.get("https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/cattos.jpg").content

flag = ""
for i in range(len(kitters)):
  if kitters[i] != cattos[i]:
    flag += chr(cattos[i])
    
print(flag)
