#Chapter 2 Practice 5
import math
x1,x2,x3,x4 = [int(e) for e in input().split()]
mx = max(x1,x2,x3,x4)
mi = min(x1,x2,x3,x4)
ans = x1+x2+x3+x4-mx-mi
print(ans)
