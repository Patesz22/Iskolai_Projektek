import random


def osztolapok(x):
    if x == True:
        val_lap1 = " ------------- "
        val_lap2 = "|* * * * * * *|"
        val_lap3 = "| * * * * * * |"
        val_lap4 = "|* * * * * * *|"
        val_lap5 = "| * * * * * * |"
        val_lap6 = "|* * * * * * *|"
        val_lap7 = "| * * * * * * |"
        val_lap8 = "|* * * * * * *|"
        val_lap9 = "| * * * * * * |"
        val_lap10 = "|* * * * * * *|"
        val_lap11 = "| * * * * * * |"
        val_lap12 = "|* * * * * * *|"
        val_lap13 = " ------------- "

    if x == False:
        szimbol = ["♠", "♦", "♥", "♣"]
        szam = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "K", "Q"]
        charszim = random.choice(szimbol)
        charszam = random.choice(szam)

        val_lap1 = " ------------- "
        val_lap2 = "| YX          |".replace("X", charszim)
        val_lap2 = val_lap2.replace("Y", charszam)
        val_lap3 = "|   -------   |"
        val_lap4 = "|  |       |  |"
        val_lap5 = "|  |       |  |"
        val_lap6 = "|  |       |  |"
        val_lap7 = "|  |   X   |  |".replace("X", charszim)
        val_lap8 = "|  |       |  |"
        val_lap9 = "|  |       |  |"
        val_lap10 = "|  |       |  |"
        val_lap11 = "|   -------   |"
        val_lap12 = "|          XY |".replace("X", charszim)
        val_lap12 = val_lap12.replace("Y", charszam)
        val_lap13 = " ------------- "

        if charszam == "10":
            val_lap1 = " -------------"
            val_lap2 = "| YX         |".replace("X", charszim)
            val_lap2 = val_lap2.replace("Y", charszam)
            val_lap3 = "|   -------   |"
            val_lap4 = "|  |       |  |"
            val_lap5 = "|  |       |  |"
            val_lap6 = "|  |       |  |"
            val_lap7 = "|  |   X   |  |".replace("X", charszim)
            val_lap8 = "|  |       |  |"
            val_lap9 = "|  |       |  |"
            val_lap10 = "|  |       |  |"
            val_lap11 = "|   -------   |"
            val_lap12 = "|         XY |".replace("X", charszim)
            val_lap12 = val_lap12.replace("Y", charszam)
            val_lap13 = " -------------"

        if charszam == "J":
            charszam = "10"
        if charszam == "K":
            charszam = "10"
        if charszam == "Q":
            charszam = "10"

    return charszam, val_lap1, val_lap2, val_lap3, val_lap4, val_lap5, val_lap6, val_lap7, val_lap8, val_lap9, val_lap10, val_lap11, val_lap12, val_lap13


def playerlapok():
    szimbol = ["♠", "♦", "♥", "♣"]
    szam = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "K", "Q"]
    charszim = random.choice(szimbol)
    charszam = random.choice(szam)

    val_lap1 = " ------------- "
    val_lap2 = "| YX          |".replace("X", charszim)
    val_lap2 = val_lap2.replace("Y", charszam)
    val_lap3 = "|   -------   |"
    val_lap4 = "|  |       |  |"
    val_lap5 = "|  |       |  |"
    val_lap6 = "|  |       |  |"
    val_lap7 = "|  |   X   |  |".replace("X", charszim)
    val_lap8 = "|  |       |  |"
    val_lap9 = "|  |       |  |"
    val_lap10 = "|  |       |  |"
    val_lap11 = "|   -------   |"
    val_lap12 = "|          XY |".replace("X", charszim)
    val_lap12 = val_lap12.replace("Y", charszam)
    val_lap13 = " ------------- "

    if charszam == "10":
        val_lap1 = " -------------"
        val_lap2 = "| YX         |".replace("X", charszim)
        val_lap2 = val_lap2.replace("Y", charszam)
        val_lap3 = "|   -------   |"
        val_lap4 = "|  |       |  |"
        val_lap5 = "|  |       |  |"
        val_lap6 = "|  |       |  |"
        val_lap7 = "|  |   X   |  |".replace("X", charszim)
        val_lap8 = "|  |       |  |"
        val_lap9 = "|  |       |  |"
        val_lap10 = "|  |       |  |"
        val_lap11 = "|   -------   |"
        val_lap12 = "|         XY |".replace("X", charszim)
        val_lap12 = val_lap12.replace("Y", charszam)
        val_lap13 = " -------------"

    if charszam == "J":
        charszam = "10"
    if charszam == "K":
        charszam = "10"
    if charszam == "Q":
        charszam = "10"

    return charszam, val_lap1, val_lap2, val_lap3, val_lap4, val_lap5, val_lap6, val_lap7, val_lap8, val_lap9, val_lap10, val_lap11, val_lap12, val_lap13

lapsave1 = ""
lapsave2 = ""
lapsave3 = ""
lapsave4 = ""
lapsave5 = ""
lapsave6 = ""
lapsave7 = ""
lapsave8 = ""
lapsave9 = ""
lapsave10 = ""
lapsave11 = ""
lapsave12 = ""
lapsave13 = ""

szamp = 0
szamo = 0


e = osztolapok(x=False)
osztolapokx1 = e[1]
osztolapokx2 = e[2]
osztolapokx3 = e[3]
osztolapokx4 = e[4]
osztolapokx5 = e[5]
osztolapokx6 = e[6]
osztolapokx7 = e[7]
osztolapokx8 = e[8]
osztolapokx9 = e[9]
osztolapokx10 = e[10]
osztolapokx11 = e[11]
osztolapokx12 = e[12]
osztolapokx13 = e[13]

f = osztolapok(x=True)
osztolapok1 = f[1]
osztolapok2 = f[2]
osztolapok3 = f[3]
osztolapok4 = f[4]
osztolapok5 = f[5]
osztolapok6 = f[6]
osztolapok7 = f[7]
osztolapok8 = f[8]
osztolapok9 = f[9]
osztolapok10 = f[10]
osztolapok11 = f[11]
osztolapok12 = f[12]
osztolapok13 = f[13]

while True:
    s = playerlapok()
    # print(f"{s[1]}\n{s[2]}\n{s[3]}\n{s[4]}\n{s[5]}\n{s[6]}\n{s[7]}\n{s[8]}\n{s[9]}\n{s[10]}\n{s[11]}\n{s[12]}\n{s[13]}")
    lapsave1 = lapsave1 + " " + s[1]
    lapsave2 = lapsave2 + " " + s[2]
    lapsave3 = lapsave3 + " " + s[3]
    lapsave4 = lapsave4 + " " + s[4]
    lapsave5 = lapsave5 + " " + s[5]
    lapsave6 = lapsave6 + " " + s[6]
    lapsave7 = lapsave7 + " " + s[7]
    lapsave8 = lapsave8 + " " + s[8]
    lapsave9 = lapsave9 + " " + s[9]
    lapsave10 = lapsave10 + " " + s[10]
    lapsave11 = lapsave11 + " " + s[11]
    lapsave12 = lapsave12 + " " + s[12]
    lapsave13 = lapsave13 + " " + s[13]
    szamp = szamp + int(s[0])

    print(f"\n")
    print(szamo)
    print("---------------------------------------------------------------------------")
    print(f"\n{lapsave1}\n{lapsave2}\n{lapsave3}\n{lapsave4}\n{lapsave5}\n{lapsave6}\n{lapsave7}\n{lapsave8}\n{lapsave9}\n{lapsave10}\n{lapsave11}\n{lapsave12}\n{lapsave13}")
    print(szamp)

    x = input("Kilépés = igen ")
    if x.lower() == "igen":
        break

