"""Chapter 2 Practice 7"""
"""Create by TULYAWAT"""
size = int(input('Pls input Size in inch : '))
if size < 37:
    print('XS')
elif size >= 37 and size < 41 :
    print('S')
elif size >= 41 and size < 43 :
    print('M')
elif size >= 43 and size < 46 :
    print('L')
else:
    print('XL')