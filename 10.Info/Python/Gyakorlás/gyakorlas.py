import random

# i = 1
# for i in range(20):
#     if i % 2 == 1:
#         print(i, end="\t")

# while i <= 20:
#     if i % 2 == 0:
#         i += 1
#         print(i)
#     else:
#         i += 1



# lista = []
#
# for h in range(25):
#     r = random.randint(1, 100)
#     if r not in lista: # if not lista.__contains__(r):
#         lista.append(r)
#         lista.sort()
#
# for h in lista:
#     print(h, end="\t") # leszedi a listáról a []-et és , -t

import random

penz = int(input("Mennyi egyenleget szeretnél? (Ft) "))

pont = 0
yn = ""
igne = ""
kor = 0

tet = int(input(f"Mennyi pénzzel szeretnél játszani? "))
sad = input(f"FIGYELEM! Csak 10 körönként tudsz kivenni! - Enter")


while penz >= tet:
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    kor += 1

    if kor == 10:
        kordes = input(f"Ki szeretnéd venni a pénzed ({penz}Ft), vagy játszol tovább? (\"kiveszem\" ha meg szeretnél állni!)")
        if kordes == "kiveszem":
            break
        else:
            continue

    input(f"\nENTER az dobáshoz!\n Pénzed: {penz}Ft")

    penz -= tet

    if kocka1 + kocka2 == 7:
        print(f"Nyertél! Ügyes vagy!")
        print(f"Dobott számok: {kocka1} és {kocka2} ({kocka1 + kocka2})\n")
        pont += 1
        # print(pont, yn)
        if pont == 3:
            print(f"\n{pont}-od van, megnyerted a főnyereményt!! \n")

        yn = ""
        while yn not in ["igen", "nem"] and 0 < pont <= 2:
            yn = input(f"Jelenleg {pont}/3 pontod van. Szeretnél tovább próbálkozni a nagyobb nyereményért? (igen/nem) ")



    else:
        print(f"Vesztettél! Béna vagy!")
        print(f"Dobott számok: {kocka1} és {kocka2} ({kocka1 + kocka2})\n")
        pont = 0


    if pont == 1 and yn == "nem":
        penz += tet * 5
        print(f"Nyereményed {tet * 5}Ft!")
        pont = 0
        yn = ""

    elif pont == 2 and yn == "nem":
        penz += tet * 50
        print(f"Nyereményed {tet * 10}Ft!")
        pont = 0
        yn = ""

    elif pont == 3 and yn == "igen":
        penz += tet * 500
        print(f"Nyereményed {tet * 500}Ft! \n Megnyerted a főnyereményt!!")
        pont = 0
        yn = ""

if tet < penz:
    print("El fogyott a pénzed!")

else:
    print(f"Kiszálltál! Egyenleged: {penz}Ft")











