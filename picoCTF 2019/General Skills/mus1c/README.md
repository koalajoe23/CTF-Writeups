# plumbing

## Problem

I wrote you a [song](https://2019shell1.picoctf.com/static/8ee6e9a249f17d091862d587e678f34b/lyrics.txt). Put it in the picoCTF{} flag format

## Hint

Do you think you can master rockstar?

## Solution

I had no luck using py-rockstar and various online rockstar interpreters *except* the [official reference implementation in JS](https://codewithrockstar.com/online). Paste lyrics.txt into the input field and run it in browser.

The script prints a couple of integers, whose ASCII code appended gives us the flag (don't forget to surround it with picoCTF{})

Alternatively, use the [official docs](https://codewithrockstar.com/online) to learn rockstar syntax and determine the solution by hand, or convert the code to a more familiar language (see [lyrics_with_comments.rocks](lyrics_with_comments.rocks).

## Flag

picoCTF{rrrocknrr0113r}
