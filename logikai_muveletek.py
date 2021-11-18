A = True
B = False
#             1
#      1            0
C = (A or B) != (A and B)

print(C)
#                  1
#          1                1
D  = (not C or A) == (A and A or B)

print(f'D = {D}')