#Chapter 2 2.1
#finding mean

a,b,c = [float(e) for e in input().split()]
if b>= a >= c :
    print(a)
else:
    if c>= a >= b:
        print(a)
    else:
        if a >= b >= c:
            print(b)
        else:
            if c >= b >= a:
                print(b)
            else:
                print(c)
    