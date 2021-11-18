x = int(input('X = '))
y = int(input('Y = '))

if x > y:
    print(f'{x} a nagyobb')
else:
    if y > x:
        print(f'{y} a nagyobb')
    else:
        print('a két szám egyenlő')