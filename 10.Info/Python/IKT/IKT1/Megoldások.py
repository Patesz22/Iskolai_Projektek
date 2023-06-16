# 1.Feladat

import random

lista, ujlista = [], []

mettol, meddig = int(input("Mettől generáljuk a számokat? ")), int(input("Meddig generáljuk a számokat? "))

for i in range(50):
    lista.append(random.randint(mettol, meddig))

for elem in lista:
    if elem not in ujlista:
        ujlista.append(elem)

ujlista.sort()

print(f"""
Régi lista:
{lista}
\nRendezett lista:
{ujlista}""")

# 2.Feladat

beker = int(input("Adjon meg egy számot: "))

for x in range(len(ujlista)):
    if beker == ujlista[x]:
        print(f"Benne van a {beker} szám a listában és megtalálható a(z) {ujlista.index(beker)+1}. helyen.\n")
        break
else:
    print(f"A(z) {beker} nincs benne a listában.")

# 3.Feladat

osszeg, beker2 = [], int(input("1-es vagy 2-es számot írjon be: "))

if beker2 == 1:
    for y in range(len(ujlista)):
        if ujlista[y] % 2 == 0:
            osszeg.append(ujlista[y])
elif beker == 2:
    for y in range(len(ujlista)):
        if ujlista[y] % 2 == 1:
            osszeg.append(ujlista[y])
else:
    print("Nem 1-es vagy 2-es a megadott szám!")

print(f"Az összeg: {sum(osszeg)}")