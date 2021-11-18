import math

euro_arfolyam = float(input('ennyi az euro árfolyma: '))
euro_van = int(input('ennyi EURO-t akarok átváltani: '))

ft = euro_arfolyam * euro_van

# kerekít:
ft_01 = round(ft)
# . utáni rész levág:
ft_02 = math.floor(ft)

print(f'ennyi HUF-ot ér: {ft}')
print(f'ennyi HUF-ot ér: {ft_01}')
print(f'ennyi HUF-ot ér: {ft_02}')