#!/bin/env sh
curl -s -o strings https://2019shell1.picoctf.com/static/d97e691ff0842819be9dfcb767c074d9/strings
strings strings | grep pico
rm strings