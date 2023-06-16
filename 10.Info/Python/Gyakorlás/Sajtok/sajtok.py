class Sajt():
    adatok = []
    file = open("data.txt", "r", encoding="utf8")
    for sor in file:
        adatok.append(sor.strip().split(";"))

sajt = Sajt()
sajtok = sajt.adatok
# print(sajtok)

print(f"{len(sajtok)} féle sajt van raktáron")

mini = 10000
mininev = ""

for i in sajtok:
    if int(i[2]) < mini:
        mini = int(i[2])
        mininev = i[1]

print(f"A legolcsóbb sajt a(z) {mininev} és {mini}Ft kerül!")

maxdb = 0
maxnev = ""

for i in sajtok:
    if int(i[0]) > maxdb:
        maxdb = int(i[0])
        maxnev = i[1]

print(f"A sajtok közül a(z) {maxnev}-ból/ből van, {maxdb}db!")

penz = 15000
db = 0

for i in sajtok:
    if i[1] == "Trappista":
        db = penz / int(i[2])

print(f"15000Ft-ból {round(db, 2)}db Trappista sajtot tudunk venni!")
