ev = int(input('évszám: '))
# minden 4el osztható, kivéve a 100 oszthatót, de a 400al osztható mégis

# 1999 -> nem
# 2004 -> igen
# 2000 -> igen
# 2100 -> nem

# v1
if ev % 400 == 0:
    print('szökőév')
else:
    if ev % 100 == 0:
        print('nem szökőév')
    else:
        if ev % 4 == 0:
            print('szökőév')
        else:
            print('nem szökőév')

# v2
if ev % 100 == 0:
    if ev % 400 == 0:
        print('szökőév')
    else:
        print('nem szökőév')
else:
    if ev % 4 == 0:
        print('szökőév')
    else:
        print('nem szökőév')

# v3
# hf

# v1.1 (egyszerűsítve):

if ev % 400 == 0:
    print('szökőév')
elif ev % 100 == 0:
    print('nem szökőév')
elif ev % 4 == 0:
    print('szökőév')
else:
    print('nem szökőév')

# v1.2
if   ev % 400 == 0: print('szökőév')
elif ev % 100 == 0: print('nem szökőév')
elif ev %   4 == 0: print('szökőév')
else:               print('nem szökőév')