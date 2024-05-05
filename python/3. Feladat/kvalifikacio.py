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



# 1. Készítsen python alkalmazást a következő feladatok megoldására, amelynek projektjét kvalifikacio néven mentse el!

# 2. Olvassa be a Monaco 2023.py állomány sorait és tárolja az adatokat egy olyan adatszerkezetben, amely használatával a további feladatok megoldhatók!

# 3. Határozza meg és írja ki a képernyőre, hogy hány köridő szerepel a forrásállományban!

# 4. Készítsen metódust amely a futott köridőt másodpercre váltja, ezredmásodperc pontossággal!

# 5. Melyik versenyző érte el a legjobb eredményt a Q1-ben? A minta szerint írja ki ezen versenyző adatait! Feltételezheti, hogy nem alakul ki holtverseny.

# 6. Listázza ki a Q2-be jutott versenyzőket, valamint az ott megtett köridejüket!

# 7. Kérjen be egy köridőt, majd írja a hatarfeletti.txt állományba azon versenyzőket és köridejüket, akik a megadott időnél gyorsabban tették meg a kört! A bekért értéket nem kell ellenőriznie.

# 8. Készítsen statisztikát, melyben összegzi, hogy az egyes konstruktőrök versenyzőinek hány köre szerepel az állományban! Jelenítse meg azokat az konstruktőröket és a futott körök számát, amelyeknek több, mint 4 köridő áll a neve mellett! A kiírás sorrendje tetszőleges.