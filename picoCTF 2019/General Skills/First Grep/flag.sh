#!/bin/env sh
curl -s -o file https://2019shell1.picoctf.com/static/5f3d01c1753f29c50640a903bd6ec5e6/file
grep "picoCTF" file
rm file


