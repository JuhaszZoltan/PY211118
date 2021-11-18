max_pont = int(input('max pont: '))
akt_pont = int(input('elért pont: '))

szazalek = akt_pont / max_pont * 100

if   szazalek < 51: print(f'{szazalek}%, elégtelen')
elif szazalek < 65: print(f'{szazalek}%, elégséges')
elif szazalek < 80: print(f'{szazalek}%, közepes')
elif szazalek < 90: print(f'{szazalek}%, jó')
else:               print(f'{szazalek}%, jeles')

# homerseklet = -3
# if homerseklet < 0: print('fagy')

