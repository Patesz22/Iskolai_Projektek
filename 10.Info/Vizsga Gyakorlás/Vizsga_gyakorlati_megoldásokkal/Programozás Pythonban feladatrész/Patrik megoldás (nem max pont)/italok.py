class Beolvas:
    adatok = []
    file = open("adatok.txt", "r", encoding="utf8")

    for sor in file:
        adatok.append(sor.strip().split(";"))


beolvas = Beolvas()
szorp = Beolvas.adatok

a = 0
for sor in szorp:
    a += 1
print(f"A raktáron {a} fajta szörp található.")

mennyiseg = 0
nev = ""
for sor in szorp:
    if float(sor[0]) > mennyiseg:
        mennyiseg = float(sor[0])
        nev = sor[1]
print(f"A legtöbb szörp a {nev} méghozzá {mennyiseg} literrel.")

osszea = 0
for sor in szorp:
    osszea += int(sor[2])
print(f"A termékek átlagos ára {osszea / a} Ft.")  # az "a"-t már meghatároztuk előbb

keszlet = 0
for sor in szorp:
    keszlet += float(sor[0]) * float(sor[2])
print(f"A készlet értéke: {round(keszlet / 1000000, 2)} millió forint.")

atlag = osszea / a
for sor in szorp:
    if float(sor[2]) > atlag:
        print(f"{sor[2]} Ft  -  {sor[1]}")



