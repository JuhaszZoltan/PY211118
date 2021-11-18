fogyasztas = float(input('autó fogyasztása (l/100km): '))
benzin_ar = float(input('benzin ára (ft/l): '))
ut_hossza = float(input('út hossza (km): '))
utasok_szama = int(input('utasok száma: '))

koltseg = fogyasztas / 100 * ut_hossza * benzin_ar

print(f'teljes költség: {koltseg} Ft')
print(f'egy főre jutó utiköltség: {koltseg / utasok_szama} Ft')