# whats-the-difference

## Problem

Can you spot the difference? [kitters](https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg) [cattos](https://2019shell1.picoctf.com/static/473cf765877f28edf95140f90cd76b59/kitters.jpg). They are also available at /problems/whats-the-difference\_0\_00862749a2aeb45993f36cc9cf98a47a on the shell server

## Hint

- How do you find the difference between two files?
- Dumping the data from a hex editor may make it easier to compare.

## Solution

Compare the two files bytewise. For every byte that differs, append the byte from cattos.jpg as ascii value to the flag

## Flag

picoCTF{th3yr3\_a5\_d1ff3r3nt\_4s\_bu773r\_4nd\_j311y\_aslkjfdsalkfslkflkjdsfdszmz10548}
