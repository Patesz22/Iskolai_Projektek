class Italok:
    def __init__(self,line):
        darabol = line.split(";")
        self.adat = float(darabol[0])
        self.nev = darabol[1]
        self.menny = int(darabol[2].rstrip("\n"))

italok = []
with open("adatok.txt", "rt", encoding="utf-8") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        italok.append(Italok(lines[i]))
print("A raktáron {} fajta szörp található.".format(len(italok)))


print()