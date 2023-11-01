#chapter 2 Pratice 3
x,y =[float(k) for k in input().split()]
print(f'coordinate (x,y) is ({x},{y})')
if x and y > 0:
    print('QD1')
elif x == 0 and (y > 0  or y < 0):
    print('on y axis')
elif y == 0 and (x > 0 or x < 0):
    print('On x axis')
elif y==0 and x==0:
    print('Origin')
elif x < 0 and y > 0:
    print("QD2")
elif x <0 and y <0:
    print("QD3")
else:
    print("QD4")

print("----------END----------")