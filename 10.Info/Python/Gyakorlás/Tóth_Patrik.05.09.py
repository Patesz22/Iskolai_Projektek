# --------- Adattípusok / Változótípusok ---------

#Tóth Patrik 05.09

asd = ""  # string
# qwe = 2  # int
# ewq = 2.5  # float
# lkj = []  # list
# hgf = True  # bool / boolean
# beker = input(f"Kérek valamit")  # érték bekérése | int(input) | str(input) ...


# -------- Elágazások --------


# if beker < 30:  # ha....
#     a = 1
# elif beker > 30:  # ha másik feltétel....
#     a = 2
# else:  # bármelyik másik esetben....
#     a = 3


# Példa: 15-nél kisebb számokat * 10
#        15-nél nagyobb számokat / 3

# beker = int(input(f"Adj meg egy számot: "))
#
# if beker < 15:
#     szam = beker * 10
#     print(szam)
#
#     if szam % 2 == 0:
#         print("Páros")
#
#     elif szam % 2 != 0:
#         print("Páratlan")
#
# elif beker > 15:
#     szam = beker / 3
#     print(szam)
#
#     if szam % 2 == 0:
#         print("Páros")
#
#     elif szam % 2 != 0:
#         print("Páratlan")


# -------- Ciklusok --------


# beker = 0
# i = 0
#
# print("testasd", end="\t")  # Amikor lefut hozzácsapja ezt
#
# print("\n")
#
# while beker < 15:   # while ciklus
#     beker += 1
#     print(beker, end="\t")
#
# print("\n")
#
# for i in range(1, 16):  # for ciklus
#     print(i, end="\t")


# -------- Random számok --------


# Két random szám összeszorzása
import random
#
# print(random.randint(10, 50) * random.randint(10, 50))  # egysoros megoldás
#
# a = random.randint(10, 50)
# b = random.randint(10, 50)  # többsoros megoldás
# print(a * b)

# Példa:
# rszamok = []
#
# for i in range(50):
#     elem = random.randint(0, 100)
#
#     if not rszamok.__contains__(elem):
#         rszamok.append(elem)
#     else:
#         continue
#
# rszamok.sort()
# print(rszamok)
#
# beker = int(input("Írjon be egy számot: "))
#
# if rszamok.__contains__(beker):
#     print(f"{beker} szám szerepel a listában! A(z) {rszamok.index(beker) + 1} helyen")  # + 1, mert a lista nem 1,2,3,4,5 hanem 0,1,2,3,4,5
#     rszamok.remove(beker)  # törlés
#     # rszamok.pop(rszamok.index(beker))  # ez is kitörli
#
# else:
#     print(f"{beker} szám nem szerepel a listában!")
#
# print(rszamok)

# Emberes példa:
#

vezeteknev = ["Kovács", "Takács", "Schneider", "Szőke", "Bolla", "Tőzsér"]
keresztnev = ["Simi", "Tamás", "Tamara", "Abigel", "Tibor", "Zsolt"]
kor = [20, 42, 9, 10, 31, 60]
hobby = ["Foci", "Játék", "Tanulás", "Jégkorong", "Python", "Vezetés"]

emberek = []

for i in range(5):
    emberek.append([random.choice(vezeteknev), random.choice(keresztnev), random.choice(kor), random.choice(hobby)])

print(emberek)

for i in emberek:
    if i[2] >= 20:
        print(i[0], i[1])




