#Chapter 2.2
#Verify circle wheter or not for touch

import math
x1,y1,r1 = [float(e) for e in input().split()]
x2,y2,r2 = [float(e) for e in input().split()]
#distance between 2 circle from origin
d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
sum_r = r1+r2
if d > sum_r:
    print('Untouch')
elif d < sum_r:
    print('Intersect')
else:
    print('Touch')
