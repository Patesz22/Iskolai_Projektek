# B csoport,

###########################################################


adat = int(input("Átváltandó mennyiség: "))
melyik = input("HUF / EUR: ")

if "HUF" in melyik:
    adat = adat / 360
    print(adat,"EUR")

elif "EUR" in melyik:
    adat = adat * 360
    print(adat,"HUF")

else:
    print("Érvénytelen pénznem!")

