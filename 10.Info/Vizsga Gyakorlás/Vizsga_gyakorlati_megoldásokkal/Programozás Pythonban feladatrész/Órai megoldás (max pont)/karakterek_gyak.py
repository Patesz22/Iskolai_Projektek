input("Adjon meg mondatot, vagy szót. Az ENTER lenyomásával tud továbbhaladni!")
szoveg = input("Szöveg: ")
lista = []

while szoveg != "":
    lista.append(szoveg)
    szoveg = input("Szöveg: ")


def buta(lista):
    hossz = 0
    maxi = ""
    for elem in lista:
        if len(elem) > hossz:
            hossz = len(elem)
            maxi = elem

    return maxi, hossz


kiir = buta(lista)

if kiir[1] < 15:
    print(f'A(z) "{kiir[0]}" mondat vagy szó kevesebb, mint 15 karakterből áll. Karakterei száma: {kiir[1]}')
if kiir[1] > 15:
    print(f"A(z) \"{kiir[0]}\" mondat vagy szó több, mint 15 karakterből áll. Karakterei száma: {kiir[1]}")


