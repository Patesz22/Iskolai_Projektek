class Beolvas:
    adatok = []
    file = open("adatok.txt", "r", encoding="utf8")

    for sor in file:
        adatok.append(sor.strip().split(";"))


beolvas = Beolvas()
szorp = Beolvas.adatok

print(f"A raktáron lévő {len(szorp)} fajta szörp található.")

maxi, maxnev = 0, ""

for i in szorp:
    if float(i[0]) > maxi:
        maxi = float(i[0])
        maxinev = i[1]

print(f"A legtöbb szörp a {maxinev} méghozzá {maxi/10} literrel.")

avg = 0

for i in szorp:
    avg += int(i[2])

print(f"A termékek átlagos ára {avg / len(szorp)} Ft.")

ossz = 0

for i in szorp:
    ossz += float(i[0]) * int(i[2])

print(f"A készlet értéke: {round(ossz / 1000000, 2)} millió forint.")

print("Átlag feletti termékek:")
for i in szorp:
    if int(i[2]) > (avg / len(szorp)):
        print(f"{i[2]} Ft \t-\t{i[1]}")