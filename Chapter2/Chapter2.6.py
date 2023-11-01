#Chapter 2 Practice 2.6
import math
a = int(input())
x = int(round(a**(1/3),0))
if x == a:
    print(x)
else:
    print('Not found')