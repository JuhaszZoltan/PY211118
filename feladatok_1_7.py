import math
a = int(input('első befogó hossza: '))
b = int(input('második befogó hossza: '))

# a^2 + b^2 = c^2
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f'átfogó hossza = {c}')