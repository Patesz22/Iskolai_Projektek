import random
print(f"1. Feladat\n")

list = []
lista = []
lista1 = []
lista20 = []
mettol = int(input("Mettől generáljunk számokat: "))
meddig = int(input("Meddig generáljunk számokat: "))

for i in range(50):
    list.append(random.randint(mettol, meddig))

print(f"\nGenerált számok: \n {list}")


print(f"\n2. Feladat\n")

list.sort()
lista = [i for n, i in enumerate(list) if i not in list[:n]]
print(f"Rendezett számok: \n {lista}")


print(f"\n3. Feladat\n")
print(f"{min(lista)} a legkisebb szám, {max(lista)} a legnagyobb.")


print(f"\n \n4. Feladat\n")
for i in range(len(lista)):
    if lista[i] < 20:
        lista20.append(lista[i])
print(f"20-nál kisebb számok: \n {lista20}")


print(f"\n5. Feladat\n")
for i in range(len(lista)):
    if lista[i] % 3 == 0:
        lista1.append(1)
print(f"{sum(lista1)} db szám osztható 3-mal")


print(f"\n6. Feladat\n")
szam = int(input("Melyik számot keressük: "))
if lista.__contains__(szam):
    print(f"Benne van a {szam} és megtalálható a {lista.index(szam)} helyen.")
else:
    print(f"Nincs benne a(z) {szam} !")


print(f"\n7. Feladat\n")
sum = sum(lista)
print(f"Az összeg: {sum}")
