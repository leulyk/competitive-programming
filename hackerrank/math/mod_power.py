# https://www.hackerrank.com/challenges/python-power-mod-power/problem

import math

a = int(input())
b = int(input())
m = int(input())

print(math.pow(a, b))
print(math.pow(a, b) % m)
