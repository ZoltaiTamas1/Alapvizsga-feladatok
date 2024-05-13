from kor import Kor

koridok: list[Kor] = []

f = open('Monaco 2023.csv', 'r', encoding='utf-8')
f.readline()
for sor in f:
    koridok.append(Kor(sor))
f.close()

print(f'3. feladat: Az állományban {len(koridok)} db köridő lett rögzítve.')

q1_leggyorsabb = None
for k in koridok:
    if q1_leggyorsabb == None and k.szakasz == 'Q1':
        q1_leggyorsabb = k
    if k.szakasz == 'Q1' and k.futott_ido_masodpercben() < q1_leggyorsabb.futott_ido_masodpercben():
        q1_leggyorsabb = k

print(f'5. feladat: A Q1-ben leggyorsabb kört futotta: {q1_leggyorsabb.versenyzo}')
print(f'\tRajtszáma: {q1_leggyorsabb.rajtszam}')
print(f'\tFutott idő: {q1_leggyorsabb.futott_ido}')

print(f'6. feladat: A Q2-ben futott egyéni legjobb körök:')
for k in koridok:
    if k.szakasz == 'Q2':
        print(f'\t{k.versenyzo} ({k.futott_ido})')

idohatar = input('7. feladat: Köridőhatár: ')
idohatar_masodpercben = int(idohatar.strip().split(':')[0]) * 60 + float(idohatar.strip().split(':')[1])
f = open('hatarfeletti.txt', 'w', encoding='utf-8')
f.write(f'{idohatar}-nál gyorsabb rögzített köridők:')
for k in koridok:
    if idohatar_masodpercben > k.futott_ido_masodpercben():
        f.write(f'{k.versenyzo} ({k.futott_ido})\n')
f.close()

print('8. feladat: Konstruktőrök 4-nél több köridővel:')
konstruktorok = {}
    
for k in koridok:
    if k.konstruktor in konstruktorok:
        konstruktorok[k.konstruktor] += 1
    else:
        konstruktorok[k.konstruktor] = 1

for konstruktor, koridok_szama in konstruktorok.items():
    if koridok_szama > 4:
        print(f'\t{konstruktor}: {koridok_szama} köridő')