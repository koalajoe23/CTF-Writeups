# plumbing

## Problem

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21550.

## Hint

- Remember the flag format is picoCTF{XXXX}
- What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution

Use Unix pipes to feed the output of the netcat command to grep looking for picoCTF

## Flag

picoCTF{digital\_plumb3r\_8f946c69}
