class Beolvas():
    adatok = []
    beolvas = open("adatok.txt", "r", encoding="utf8")

    for sor in beolvas:
        adatok.append(sor.strip().split(";"))


beolvas = Beolvas()
szorp = beolvas.adatok

# Hány fajta található

a = 0
for sor in szorp:
    a += 1
print(f"A raktáron {a} fajta szörp található.")

# Melyik a legtöbb
maxi = 0
maxnev = ""

for sor in szorp:
    if float(sor[0]) > maxi:
        maxi = float(sor[0])
        maxnev = sor[1]
print(f"A legtöbb szörp a {maxnev} méghozzá {maxi / 10} literrel.")

# Átlag
atlag = 0
for sor in szorp:
    atlag += int(sor[2])
asd = atlag / a
print(f"A termékek átlagos ára {round(asd, 1)} Ft")

# Összérték

ossz = 0
for sor in szorp:
    ossz += float(sor[0]) * int(sor[2])
print(f"A készlet értéke: {round(ossz / 1000000), 2} millió forint.")


# Átlag feletti termékek

print(f"Átlag feletti termékek:")
for sor in szorp:
    if int(sor[2]) > asd:
        print(f"{sor[2]} Ft\t-\t{sor[1]}")

