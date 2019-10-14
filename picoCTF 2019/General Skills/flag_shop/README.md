# flag\_shop 

## Problem

There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 63894.

## Hint

Two's compliment can do some weird things when numbers get really big!

## Solution

The maximum value of a signed 32-bit is 2147483647.

By supplying an amount x -> x : 1100 - (x * 900) % 2147483648  > 100000, we can use an integer overflow to generate a negative cost which will be credited to our balance instead of deducted. The smallest x that matches this equation is 2386095.

## Flag
picoCTF{m0n3y\_bag5\_818a7f84}
