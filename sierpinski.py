#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from turtle import *

# decoration
print(stylize("\n---- | Recursion - Sierpinski | ----\n", fg("red")))

# function
def sierpinski(l):
    if l > 20:
        for i in range(3):
            sierpinski(l/2)
            fd(l)
            rt(120)

# settings
pu()
bk(100)
pd()
ht()

# user interaction
length = int(input("Length: "))
print()

# output
sierpinski(length)
