def maximum(lista):
    maxhossz = 0
    max = ""
    for elem in lista:
        if len(elem) > maxhossz:
            maxhossz = len(elem)
            max = elem
    return [max, maxhossz]


lista = []
input("Adjon meg egy mondatot, vagy szót. Az ENTER lenyomásával tud továbbhaladni!")
szoveg = input("Szöveg: ")

while szoveg != "":
    lista.append(szoveg)
    szoveg = input("Szöveg: ")

eredmeny = maximum(lista)
if eredmeny[1] > 15:
    print(f"A(z) \"{eredmeny[0]}\" mondat vagy szó több mint 15 karakterből áll. Karakterei száma: {eredmeny[1]}")
elif eredmeny[1] < 15:
    print(f"A(z) \"{eredmeny[0]}\" mondat vagy szó több mint 15 karakterből áll. Karakterei száma: {eredmeny[1]}")

