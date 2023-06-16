# #####################################################################################################################################################################################################################################################################################
    #! Dolgozat #1 A

# kg = float(input("Testtömeg: "))
# magassag = input("Magassag (m / cm): ")
#
# if "cm" in magassag:
#     eredmeny = round(kg / int(magassag.replace("cm", "")) **2 * 1000)
#     print(f'A BMI érték: {eredmeny}')
#
# elif "m" in magassag:
#     eredmeny = round(kg / float(magassag.replace("m", ""))**2)
#     print(f'A BMI értéke: {eredmeny}')
#
# else:
#     print("HIBA!")

# #####################################################################################################################################################################################################################################################################################
    #! Dolgozat #1 B

# bemenet = input("Mennyiség és valuta típus(€ vagy Ft) ")
#
# if "€" in bemenet:
#     kimenet = int(bemenet.replace("€", "")) * 360
#     print(f'{bemenet} egyenlő {kimenet} Ft-tal')
# elif "Ft" in bemenet:
#     kimenet = int(bemenet.replace("Ft", "")) // 360
#     print(f'{bemenet} egyenlő {kimenet} €-tal')
#
# else:
#     print("HIBA!")

# #####################################################################################################################################################################################################################################################################################

# TZ#1

#1 Feladat
beolvas, palinka = open("Dogák/TZ_1/adatok.txt"), []

for sor in beolvas:
    sor = sor.strip().split()
    liter = int(sor[0])
    neve = sor[1]
    ar = int(sor[2])
    palinka.append([liter,neve,ar])

beolvas.close()

#2 Feladat
print(f"Összesen {len(palinka)}) féle pákinkát árusítanak.")

#3 Feladat

index, van, nincs, = 0, 0, 0

while index < len(palinka):
    if palinka[index][0] == 0:
        nincs += 1
    elif palinka[index][0] != 0:
        van += 1
    index += 1

print(f"Készleten: {van} db \nElfogyott: {nincs} db \n")

#4.Feladat
draga = [0, "", 0]

for adat in palinka:
    ar = int(adat[2])
    if ar > draga[2]:
        draga[0] = adat[1]
        draga[2] = ar

print(f"A legdrágább termék a {draga[0].upper()} pálinka. Ára: {draga[2]} Ft!")

#5.Feladat

mennyiseg = [0, "", 0]

for adat in palinka:
    liter = int(adat[0])
    if liter > mennyiseg[2]:
        mennyiseg[0] = adat[1]
        mennyiseg[2] = liter

print(f"A {mennyiseg[0].upper()} pálinkából van a legtöbb, {mennyiseg[2]} liter!")

#6.Feladat

bevetel = 0

for adat in palinka:
    fiz = adat[2]*adat[0]

    if fiz == 0:
        fizetendo = (fiz)
    else:
        fizetendo = ((fiz))
    bevetel += fizetendo

ossz = bevetel / 1000000

print(f"A készleten: {ossz} millió Ft-nyi áru van!")

#7.Feladat

kiir, index = open("rendel.txt", "w"), 0

old = open("adatok.txt", "r")

while index < len(palinka):
    if palinka[index][0] == 0:
        kiir.write(str(old.readline().strip()) + "\t Rendelni kell" + "\n")
    elif palinka[index][0] != 0:
        kiir.write(str(old.readline().strip()) + "\tOK" + "\n")

    index += 1

old.close()
kiir.close()

print(f"A \"{kiir.name}\" fikeresen létrehozva!")