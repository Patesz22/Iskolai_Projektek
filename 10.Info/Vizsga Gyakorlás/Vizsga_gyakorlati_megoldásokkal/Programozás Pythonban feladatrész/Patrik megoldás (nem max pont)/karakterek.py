lista = []


def eldont(lista):
    input("Adjon meg egy mondatot, vagy szót. Az ENTER lenyomásával tud továbbhaladni! \n")
    hossz = 0
    szoveg = "None"
    tobbkevesebb = ""
    while szoveg != "":
        szoveg = input("Szöveg: ")

        if len(szoveg) > hossz:
            hossz = len(szoveg)
            lista.clear()
            lista.append(szoveg)
            # print(hossz)

            if hossz > 15:
                tobbkevesebb = "több"
            elif hossz < 15:
                tobbkevesebb = "kevesebb"

    print(
        f"A(z) \"{', '.join(lista)}\" mondat vagy szó {tobbkevesebb} mint 15 karakterből áll. Karakterei száma: {hossz}")

    return lista

eldont(lista)
