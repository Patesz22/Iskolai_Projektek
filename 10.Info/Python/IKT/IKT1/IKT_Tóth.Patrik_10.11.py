# Csoport 3

# Csoport tagok - Tóth Patrik, Szőke Simon, Kronome Zsolt

# VICCI LESZ :P +10pont

import random
mettol = int(input("Mettől generáljunk számokat? "))
meddig = int(input("Meddig generáljunk számokat? "))
list = []
lista = []

for i in range(50):
    list.append(random.randint(mettol, meddig))

print(f"Régi lista: \n {list}\n")

lista = [i for n, i in enumerate(list) if i not in list[:n]]
lista.sort()
print(f"Rendezett lista: \n {lista} \n")

benne = int(input("Adjon meg egy számot: "))
hol = lista.index(benne)+1


if lista.__contains__(benne):
    print(f"Benne van a \"{benne}\" szám a listában és megtalálható {hol}. helyen.")
else:
    print(f"Nincs ilyen elem! {benne}")

dontes = int(input("1-es vagy 2-es számot írjun be: "))

eredmeny = 0
lista_vegleges = []

if dontes == 1:
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            lista_vegleges.append(lista[i])


elif dontes == 0:
    for i in range(0,len(lista)):
        if lista[i] % 2 == 1:
            lista_vegleges.append(lista[i])

print(sum(lista_vegleges))


