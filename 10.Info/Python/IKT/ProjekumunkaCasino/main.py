from colorama import Fore
from colorama import Style
from colorama import Back
import time
import random
from datetime import datetime


FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


print(f"""{Fore.LIGHTMAGENTA_EX}
╔════╦╗     ╔═══╦╗                ╔═══╗
║╔╗╔╗║║     ║╔══╣║                ║╔═╗║
╚╝║║╚╣╚═╦══╗║╚══╣║╔╗ ╔╦══╦╦╗╔╦╗╔╗ ║║ ╚╬══╦══╦╦═╗╔══╗
  ║║ ║╔╗║║═╣║╔══╣║║║ ║║══╬╣║║║╚╝║ ║║ ╔╣╔╗║══╬╣╔╗╣╔╗║
  ║║ ║║║║║═╣║╚══╣╚╣╚═╝╠══║║╚╝║║║║ ║╚═╝║╔╗╠══║║║║║╚╝║
  ╚╝ ╚╝╚╩══╝╚═══╩═╩═╗╔╩══╩╩══╩╩╩╝ ╚═══╩╝╚╩══╩╩╝╚╩══╝
                  ╔═╝║
                  ╚══╝{Fore.WHITE}""")

# TODO Slot színek a süti alapján, playtest, gambling (skin)


def main_menu(wallet, nev):
    print("\n----[Kérlek válassz játékot!]----\n")

    print(f"[1] Roulette     [4] Horses          [6] Pénzbefizetés")
    print(f"[2] Slots        [5] Scoreboard      [7] Pénzkivétel")
    print(f"[3] Blackjack                        {Fore.RED}[8] Kilépés{Fore.WHITE}" + "\n")

    print("Tárca: HUF", wallet)
    game = int(input("\nJáték választásod!: "))

    if game == 1:
        roulette(wallet, nev)

    elif game == 2:
        slots(wallet, nev)

    elif game == 3:
        blackjack(wallet, nev)

    elif game == 4:
        horses(wallet, nev)

    elif game == 5:
        scoreboardboot(wallet, nev)

    elif game == 6:
        depositPenz(wallet, nev)

    elif game == 7:
        withdrawPenz(wallet, nev)

    elif game == 8:
        print("\n" * 80)
        time.sleep(0.2)
        exit("Viszlát! Várunk vissza máskor is!")

    else:
        print("Kérlek adj meg egy érvényes értéket!")
        print("Újraindítás...")
        time.sleep(2.5)
        main_menu(wallet, nev)


def nevinput():
    while True:
        nev = input(f"{Fore.WHITE}{Style.BRIGHT}Kérlek adj meg egy játékosnevet! [2 - 9 karakter]: ")
        if 2 <= len(nev) <= 9:
            break

        elif len(nev) == 1:
            print(f"Az {len(nev)} szerinted nagyobb, mint 2???")

        elif len(nev) < 2:
            print(f"A {len(nev)} szerinted nagyobb, mint 2???")

        elif len(nev) > 9:
            print(f"A {len(nev)} szerinted kisebb, mint 9???")

    return nev


def showWallet(wallet, nev):
    print("\nTárca: HUF", wallet, "\n")


def betCheck(wallet, bet, nev):
    if bet == 0:
        main_menu(wallet, nev)

    if wallet == 0:
        print(f"\n{Fore.RED}Nincs pénzed! \nMivel kifogytál a pénzből, ezért kidobtak a kaszinóból! ;({Fore.WHITE}")
        time.sleep(1)
        exit("Csöves")

    if bet > int(wallet):
        print(f"\n{Fore.LIGHTMAGENTA_EX}Biztos van ehhez elég pénzed?{Fore.WHITE}")
        time.sleep(1.7)
        main_menu(wallet, nev)


def depositPenz(wallet, nev):

    print("----[Pénzbefizetés]----\n")
    deposit = int(input("Mennyit szeretnél befizetni? [HUF]: "))

    wallet += deposit

    print(f"Sikeresen bevizettél {Fore.LIGHTBLUE_EX}{deposit}{Fore.WHITE} HUF összeget!")
    time.sleep(2)

    main_menu(wallet, nev)


def withdrawPenz(wallet, nev):

    print("----[Pénzkivétel]----\n")
    withdrawal = int(input("Mennyit szeretnél kivenni? [HUF]: "))

    if withdrawal > wallet:
        print(f"{Fore.RED} Nincs elég pénzed!{Fore.WHITE}")
    else:
        wallet -= withdrawal
        print(f"Sikeresen kivettél {Fore.LIGHTBLUE_EX}{withdrawal}{Fore.WHITE} HUF összeget!")

    time.sleep(2)
    main_menu(wallet, nev)


def slots(wallet, nev):


    print("====[Üdv a slotoknál!]====\n")

    print("\n[0] Fő menü \n")
    print(f"[1]{Fore.RED} Tycoon Mania{Fore.WHITE}\n")
    print(f"[2]{Fore.GREEN} Fire Joker{Fore.WHITE}\n")
    print(f"[3]{Fore.BLUE} Sweet Bonanza{Fore.WHITE}\n")


    slot_choice = int(input("Választásod: \n"))

    if slot_choice == 1:
        tycoon(wallet, nev)
    elif slot_choice == 2:
        fire_joker(wallet, nev)
    elif slot_choice == 3:
        sweet_bonanza(wallet, nev)
    elif slot_choice == 0:
        main_menu(wallet, nev)
    else:
        print(f"A {Fore.RED}'{slot_choice}' érvénytelen adat! ")
        main_menu(wallet, nev)


def roulette(wallet, nev):
    print("\n----[Roulette]----\n")
    showWallet(wallet, nev)

    print(f"Ha {Fore.CYAN}'vissza' {Fore.WHITE}írsz be, visszalépsz a főmenübe!")

    red = False
    red_szamok = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
    black = False
    black_szamok = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
    paros = False
    paros_szamok = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    paratlan = False
    paratlan_szamok = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    nulla = False
    kicsi = False
    nagy = False
    szamok = False
    sor = False
    red_bet = 0
    black_bet = 0
    paros_bet = 0
    paratlan_bet = 0
    nulla_bet = 0
    kicsi_bet = 0
    nagy_bet = 0
    szamok_bet = 0
    sor_bet = 0
    sor_val = 0
    szamok_val = 0

    while True:
        print(f"""
{Fore.BLUE}EGYRE CSAK 1-SZER LEHET TÉTET RAKNI!{Fore.WHITE}
Az alábbiakra rakhatsz tétet:
    {Fore.RED}Pi{Fore.WHITE}ros
    {Fore.BLACK}Fe{Fore.WHITE}kete
    {Fore.GREEN}Pá1{Fore.WHITE}ros
    {Fore.GREEN}Pá2{Fore.WHITE}ratlan
    {Fore.CYAN}0{Fore.WHITE}
    {Fore.MAGENTA}Ki{Fore.WHITE}csi (1 - 18)
    {Fore.MAGENTA}Na{Fore.WHITE}gy (19 - 36)
    {Fore.BLUE}Sz{Fore.WHITE}ámok (1 - 36)
    {Fore.BLUE}Os{Fore.WHITE}zlop (1.sor : 2.sor : 3.sor)
    Enter gomb lenyomásával tudsz továbbmenni!: """)
        mire = input("")

        if mire.lower() == "vissza":
            main_menu(wallet, nev)

        elif mire.lower() == "pi":
            red_bet = int(input("Kérlek rakj tétet!: "))
            red = True

        elif mire.lower() == "fe":
            black_bet = int(input("Kérlek rakj tétet!: "))
            black = True

        elif mire.lower() == "pá1":
            paros_bet = int(input("Kérlek rakj tétet!: "))
            paros = True

        elif mire.lower() == "pá2":
            paratlan_bet = int(input("Kérlek rakj tétet!: "))
            paratlan = True

        elif mire.lower() == "0":
            nulla_bet = int(input("Kérlek rakj tétet!: "))
            nulla = True

        elif mire.lower() == "ki":
            kicsi_bet = int(input("Kérlek rakj tétet!: "))
            kicsi = True

        elif mire.lower() == "na":
            nagy_bet = int(input("Kérlek rakj tétet!: "))
            nagy = True

        elif mire.lower() == "sz":
            szamok_val = int(input("Melyik számra? (1 - 36): "))
            while szamok_val not in range(1, 36):
                print("Érvénytelen adat!")
                szamok_val = int(input("Melyik számra? (1 - 36): "))
            szamok_bet = int(input("Kérlek rakj tétet!: "))
            szamok = True

        elif mire.lower() == "os":
            sor_val = int(input("Melyik oszlopra? (1 - 2 - 3): "))
            while True:
                if sor_val not in range(1, 3):
                    print("Érvénytelen adat!")
                    sor_val = int(input("Melyik oszlopra? (1 - 2 - 3): "))
                else:
                    break
            sor_bet = int(input("Kérlek rakj tétet!: "))
            sor = True

        elif mire == str():
            break

        else:
            print(f"A '{mire}' szerinten benne van a felsorolásban???")

    bet = red_bet + black_bet + paros_bet + paratlan_bet + nulla_bet + kicsi_bet + nagy_bet + szamok_bet + sor_bet
    time.sleep(0.5)
    betCheck(wallet, bet, nev)
    wallet -= bet

    win_szam = random.randint(0, 36)
    # win_szam = 10

    bet2 = 0
    nyert = ""
    redw = False
    blackw = False
    parosw = False
    paratlanw = False
    nullaw = False
    kicsiw = False
    nagyw = False
    szamokw = False
    sorw = False

    if red is True and red_szamok.__contains__(win_szam):
        red_bet *= 2
        bet2 += red_bet
        nyert += "Piros, "
        redw = True

    if black is True and black_szamok.__contains__(win_szam):
        black_bet *= 2
        bet2 += black_bet
        nyert += "Fekete, "
        blackw = True

    if paros is True and paros_szamok.__contains__(win_szam):
        paros_bet *= 2
        bet2 += paros_bet
        nyert += "Páros, "
        parosw = True

    if paratlan is True and paratlan_szamok.__contains__(win_szam):
        paratlan_bet *= 2
        bet2 += paratlan_bet
        nyert += "Páratlan, "
        paratlanw = True

    if nulla is True and 0 == win_szam:
        nulla_bet *= 36
        bet2 += nulla_bet
        nyert += "Nulla, "
        nullaw = True

    if kicsi is True and win_szam in range(1, 18):
        kicsi_bet *= 2
        bet2 += kicsi_bet
        nyert += "Kicsi, "
        kicsiw = True

    if nagy is True and win_szam in range(19, 36):
        nagy_bet *= 2
        bet2 += nagy_bet
        nyert += "Nagy, "
        nagyw = True

    if sor is True and sor_val == win_szam:
        sor_bet *= 3
        bet2 += sor_bet
        nyert += "Sor, "
        sorw = True

    if szamok is True and szamok_val == win_szam:
        szamok_bet *= 2
        bet2 += szamok_bet
        nyert += str(win_szam) + ", "
        szamokw = True

    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Számok kisorsolása!{Fore.WHITE} \n")
    time.sleep(5)

    if redw is True or blackw is True or parosw is True or paratlanw is True or nullaw is True or kicsiw is True or nagyw is True or sorw is True or szamokw is True:
        print(f"{Fore.LIGHTGREEN_EX}Gratulálok! Nyertél: {bet2}HUF{Style.BRIGHT}{Fore.WHITE}")
        print(f"Nyerő szám: {win_szam}")
        print(f"Az alábbiakkal nyertél: {nyert}")
        wallet += bet2
        scoreboardsave(gameData="Roulette", winData=bet2, szorzoData=round(bet2 / bet, 3), betData=bet, wallet=wallet, nev=nev)
        time.sleep(2.5)
        roulette(wallet, nev)
    else:
        print(f"{Style.DIM}{Fore.RED}Vesztettél!{Style.BRIGHT}{Fore.WHITE}")
        print(f"{Fore.RED}{win_szam} kellet volna eltalálni!{Style.BRIGHT}{Fore.WHITE}")
        time.sleep(2.5)
        roulette(wallet, nev)

    return wallet


def osztolapok():
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
    if charszam == "A":
        charszam = "1"

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
    if charszam == "A":
        charszam = "1"

    return charszam, val_lap1, val_lap2, val_lap3, val_lap4, val_lap5, val_lap6, val_lap7, val_lap8, val_lap9, val_lap10, val_lap11, val_lap12, val_lap13


def blackjack(wallet, nev, totalDealer=0, totalPlayer=0, game_continued=False):

    if game_continued == False:
        print("\n----[Blackjack]----")
        print("[*] !Új játék! [*]")
        print(f"\nEgyenleged: {wallet}HUF")
        print(f"Ha {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")


    else:
        print("\n----[Blackjack]----")
        print("Játék folytatása...")
        print(f"\nEgyenleged: {wallet}HUF")
        print(f"Ha {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")

    bet = int(input("Kérlek rakj tétet! [HUF]: "))

    betCheck(wallet, bet, nev)

    if bet == 0:
        main_menu(wallet, nev)
    else:
        wallet -= bet
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

        osztosave1 = ""
        osztosave2 = ""
        osztosave3 = ""
        osztosave4 = ""
        osztosave5 = ""
        osztosave6 = ""
        osztosave7 = ""
        osztosave8 = ""
        osztosave9 = ""
        osztosave10 = ""
        osztosave11 = ""
        osztosave12 = ""
        osztosave13 = ""

    print(f"\n{Fore.LIGHTBLUE_EX}A Dealer lapokat oszt...{Fore.WHITE}")
    time.sleep(3)
    s = playerlapok()

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
    szamp2 = int(s[0])

    s = playerlapok()

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
    szamp2 += int(s[0])

    f = osztolapok()

    osztosave1 = osztosave1 + " " + f[1]
    osztosave2 = osztosave2 + " " + f[2]
    osztosave3 = osztosave3 + " " + f[3]
    osztosave4 = osztosave4 + " " + f[4]
    osztosave5 = osztosave5 + " " + f[5]
    osztosave6 = osztosave6 + " " + f[6]
    osztosave7 = osztosave7 + " " + f[7]
    osztosave8 = osztosave8 + " " + f[8]
    osztosave9 = osztosave9 + " " + f[9]
    osztosave10 = osztosave10 + " " + f[10]
    osztosave11 = osztosave11 + " " + f[11]
    osztosave12 = osztosave12 + " " + f[12]
    osztosave13 = osztosave13 + " " + f[13]
    szamo = int(f[0])

    osztosavex1 = osztosave1 + " " + " ------------- "
    osztosavex2 = osztosave2 + " " + "|* * * * * * *|"
    osztosavex3 = osztosave3 + " " + "| * * * * * * |"
    osztosavex4 = osztosave4 + " " + "|* * * * * * *|"
    osztosavex5 = osztosave5 + " " + "| * * * * * * |"
    osztosavex6 = osztosave6 + " " + "|* * * * * * *|"
    osztosavex7 = osztosave7 + " " + "| * * * * * * |"
    osztosavex8 = osztosave8 + " " + "|* * * * * * *|"
    osztosavex9 = osztosave9 + " " + "| * * * * * * |"
    osztosavex10 = osztosave10 + " " + "|* * * * * * *|"
    osztosavex11 = osztosave11 + " " + "| * * * * * * |"
    osztosavex12 = osztosave12 + " " + "|* * * * * * *|"
    osztosavex13 = osztosave13 + " " + " ------------- "

    totalDealer += szamo
    totalPlayer += szamp2
    print(f"\n{osztosavex1}\n{osztosavex2}\n{osztosavex3}\n{osztosavex4}\n{osztosavex5}\n{osztosavex6}\n{osztosavex7}\n{osztosavex8}\n{osztosavex9}\n{osztosavex10}\n{osztosavex11}\n{osztosavex12}\n{osztosavex13}")
    print("------------------------------------------------------------------------------------------------")
    print(f"\n{lapsave1}\n{lapsave2}\n{lapsave3}\n{lapsave4}\n{lapsave5}\n{lapsave6}\n{lapsave7}\n{lapsave8}\n{lapsave9}\n{lapsave10}\n{lapsave11}\n{lapsave12}\n{lapsave13}")
    print(f"Dealer lapjainak értéke: {totalDealer}\nLapjaid érteke: {totalPlayer}")

    stbet = input(f"\n{Fore.RED}K{Fore.WHITE}érsz lapot vagy {Fore.RED}M{Fore.WHITE}egállsz??: ")
    while stbet.lower() == "k":
        if stbet.lower() == "m":
            break

        if stbet.lower() == "k":
            print("\nLapot kértél. A dealer most lapot oszt neked.")
            time.sleep(1)
            s = playerlapok()

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
            szamp1 = int(s[0])
            szamp2 = int(s[0])
            print(f"\n{osztosavex1}\n{osztosavex2}\n{osztosavex3}\n{osztosavex4}\n{osztosavex5}\n{osztosavex6}\n{osztosavex7}\n{osztosavex8}\n{osztosavex9}\n{osztosavex10}\n{osztosavex11}\n{osztosavex12}\n{osztosavex13}")
            print("------------------------------------------------------------------------------------------------")
            print(f"\n{lapsave1}\n{lapsave2}\n{lapsave3}\n{lapsave4}\n{lapsave5}\n{lapsave6}\n{lapsave7}\n{lapsave8}\n{lapsave9}\n{lapsave10}\n{lapsave11}\n{lapsave12}\n{lapsave13}")

            totalPlayer += szamp2
            print(f"A dealer {Fore.MAGENTA}{szamp1}{Fore.WHITE} értékű lapot osztott neked.")
            print(f"Ezzel az összes lapod értéke: {totalPlayer}")

            time.sleep(1.5)
            if totalPlayer <= 21:
                stbet = input(f"\n{Fore.RED}K{Fore.WHITE}érsz lapot vagy {Fore.RED}M{Fore.WHITE}egállsz??: ")
            else:
                print(f"\n{Fore.RED}Túlmentél! Ezért automatikusan megállsz!{Fore.WHITE}\n")
                time.sleep(2)
                break

    winnings = bet * 2
    winningsbj = bet * 2.5

    if stbet.lower() == "m":
        if totalPlayer <= 21:
            print("\nMegálltál.\n")

        time.sleep(1)
        print(f"\n{Fore.LIGHTBLUE_EX}A Dealer felfordítja a felhúzott lapját!{Fore.WHITE}")
        time.sleep(1)

        f = osztolapok()

        osztosave1 = osztosave1 + " " + f[1]
        osztosave2 = osztosave2 + " " + f[2]
        osztosave3 = osztosave3 + " " + f[3]
        osztosave4 = osztosave4 + " " + f[4]
        osztosave5 = osztosave5 + " " + f[5]
        osztosave6 = osztosave6 + " " + f[6]
        osztosave7 = osztosave7 + " " + f[7]
        osztosave8 = osztosave8 + " " + f[8]
        osztosave9 = osztosave9 + " " + f[9]
        osztosave10 = osztosave10 + " " + f[10]
        osztosave11 = osztosave11 + " " + f[11]
        osztosave12 = osztosave12 + " " + f[12]
        osztosave13 = osztosave13 + " " + f[13]

        print(f"\n{osztosave1}\n{osztosave2}\n{osztosave3}\n{osztosave4}\n{osztosave5}\n{osztosave6}\n{osztosave7}\n{osztosave8}\n{osztosave9}\n{osztosave10}\n{osztosave11}\n{osztosave12}\n{osztosave13}")
        print("------------------------------------------------------------------------------------------------")
        print(f"\n{lapsave1}\n{lapsave2}\n{lapsave3}\n{lapsave4}\n{lapsave5}\n{lapsave6}\n{lapsave7}\n{lapsave8}\n{lapsave9}\n{lapsave10}\n{lapsave11}\n{lapsave12}\n{lapsave13}")
        totalDealer += int(f[0])
        print(f"Dealer lapjainak értéke: {totalDealer}\nLapjaid érteke: {totalPlayer}")
        time.sleep(2)

    while totalDealer <= 17:
        print("\nA dealernek kevesebb, mint 17-e van, ezért új lapot húz!")
        time.sleep(1)
        f = osztolapok()

        osztosave1 = osztosave1 + " " + f[1]
        osztosave2 = osztosave2 + " " + f[2]
        osztosave3 = osztosave3 + " " + f[3]
        osztosave4 = osztosave4 + " " + f[4]
        osztosave5 = osztosave5 + " " + f[5]
        osztosave6 = osztosave6 + " " + f[6]
        osztosave7 = osztosave7 + " " + f[7]
        osztosave8 = osztosave8 + " " + f[8]
        osztosave9 = osztosave9 + " " + f[9]
        osztosave10 = osztosave10 + " " + f[10]
        osztosave11 = osztosave11 + " " + f[11]
        osztosave12 = osztosave12 + " " + f[12]
        osztosave13 = osztosave13 + " " + f[13]

        print(f"\n{osztosave1}\n{osztosave2}\n{osztosave3}\n{osztosave4}\n{osztosave5}\n{osztosave6}\n{osztosave7}\n{osztosave8}\n{osztosave9}\n{osztosave10}\n{osztosave11}\n{osztosave12}\n{osztosave13}")
        print("------------------------------------------------------------------------------------------------")
        print(f"\n{lapsave1}\n{lapsave2}\n{lapsave3}\n{lapsave4}\n{lapsave5}\n{lapsave6}\n{lapsave7}\n{lapsave8}\n{lapsave9}\n{lapsave10}\n{lapsave11}\n{lapsave12}\n{lapsave13}")
        totalDealer += int(f[0])
        print(f"Dealer lapjainak értéke: {totalDealer}\nLapjaid érteke: {totalPlayer}")
        time.sleep(2)

    print("\n")
    time.sleep(0.5)

    if totalPlayer == 21 and totalDealer == 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"\nDöntetlen!\nVisszakaptad a pénzed!")
        wallet += bet
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalPlayer > 21 and totalDealer > 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"\nDöntetlen!\nVisszakaptad a pénzed!")
        wallet += bet
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalPlayer == 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.YELLOW}BLACKJACK! Nyereményed: {bet * 2.5}HUF{Fore.WHITE}")
        wallet += winningsbj
        scoreboardsave(gameData="Blackjack", winData=winningsbj, szorzoData=round(winnings / bet, 3), betData=bet,
                       wallet=wallet, nev=nev)
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalDealer == 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.YELLOW}Dealer BLACKJACK! Béna! Vesztettél!{Fore.WHITE}")
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalPlayer > 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalDealer > 21:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.LIGHTGREEN_EX}Nyertél! Nyereményed: {bet * 2}HUF{Fore.WHITE}")
        wallet += winnings
        scoreboardsave(gameData="Blackjack", winData=winnings, szorzoData=round(winnings / bet, 3), betData=bet,
                       wallet=wallet, nev=nev)
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    elif totalPlayer < totalDealer:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
        time.sleep(2)
        blackjack(wallet, nev)

    elif totalPlayer > totalDealer:
        print("Neked:", totalPlayer)
        print("Dealernek:", totalDealer)
        print(f"{Fore.LIGHTGREEN_EX}Nyertél! Nyereményed: {bet * 2}HUF{Fore.WHITE}")
        wallet += winnings
        scoreboardsave(gameData="Blackjack", winData=winnings, szorzoData=round(winnings / bet, 3), betData=bet,
                       wallet=wallet, nev=nev)
        time.sleep(2)
        blackjack(wallet, nev, game_continued=False)

    else:
        blackjack(wallet, nev, totalPlayer, totalDealer, game_continued=True)




def fire_joker(wallet, nev):

    print(f"----[{Fore.RED}Fire Joker{Fore.WHITE}]----\n")

    lane1 = [f'{Fore.RED}Fire Joker', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']
    lane2 = [f'{Fore.RED}Fire Joker', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']
    lane3 = [f'{Fore.RED}Fire Joker', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']

    print(f"Legalább {Fore.RED}2 Fire Joker{Fore.WHITE} kell legalább a win-hez!")
    time.sleep(1)
    print(f"\nHa {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")

    showWallet(wallet, nev)
    bet = int(input("\nKérlek rakj tétet [HUF]: "))
    if bet == 0:
        main_menu(wallet, nev)

    kor = int(input("\nHány kört szertnél játszani?: "))
    bet = bet * kor

    betCheck(wallet, bet, nev)

    wallet -= bet
    winning_jackpot = bet * 12300
    winning1 = bet * 12

    winner = f"{Fore.LIGHTGREEN_EX}Gratulálok, nyertél: {winning1}HUF{Fore.WHITE}"

    jackpot = f"{Fore.YELLOW}Gratulálok, megnyerted a JACKPOT-ot! Nyereményed: {winning_jackpot}HUF{Fore.WHITE}"

    for i in range(kor):

        random_lane1 = random.choice(lane1)
        random_lane2 = random.choice(lane2)
        random_lane3 = random.choice(lane3)

        print("\n| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " |")
        time.sleep(0.5)

        if random_lane1.__contains__("Fire Joker") and random_lane2.__contains__("Fire Joker") and random_lane3.__contains__("Fire Joker"):
            print(jackpot)
            wallet += winning_jackpot
            scoreboardsave(gameData="F_Joker", winData=winning_jackpot, szorzoData=round(winning_jackpot / bet, 3), betData=bet,
                           wallet=wallet, nev=nev)
            time.sleep(2)

        elif random_lane1.__contains__("Fire Joker") and random_lane2.__contains__("Fire Joker"):
            print(winner)
            wallet += winning1
            scoreboardsave(gameData="F_Joker", winData=winning1,
                           szorzoData=round(winning1 / bet, 3), betData=bet,wallet=wallet, nev=nev)
            time.sleep(2)

        elif random_lane1.__contains__("Fire Joker") and random_lane3.__contains__("Fire Joker"):
            print(winner)
            wallet += winning1
            scoreboardsave(gameData="F_Joker", winData=winning1,
                           szorzoData=round(winning1 / bet, 3), betData=bet, wallet=wallet, nev=nev)
            time.sleep(2)

        elif random_lane2.__contains__("Fire Joker") and random_lane3.__contains__("Fire Joker"):
            print(winner)
            wallet += winning1
            scoreboardsave(gameData="F_Joker", winData=winning1,
                           szorzoData=round(winning1 / bet, 3), betData=bet,
                           wallet=wallet, nev=nev)
            time.sleep(2)

        else:
            print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
            time.sleep(1.5)

    print(f"\n{Fore.RED}Játék vége{Fore.WHITE}\n")

    time.sleep(2)

    fire_joker(wallet, nev)

    return wallet


def tycoon(wallet, nev):

    pepper = [f'{Fore.BLACK}Black Pepper', f'{Fore.RED}Red Pepper', f'{Fore.GREEN}Green Pepper{Fore.WHITE}']
    lemon = [f'{Fore.BLACK}Black Lemon', f'{Fore.RED}Red Lemon', f'{Fore.GREEN}Green Lemon{Fore.WHITE}']
    apple = [f'{Fore.BLACK}Black Apple', f'{Fore.RED}Red Apple', f'{Fore.GREEN}Green Apple{Fore.WHITE}']


    print("----[Tycoon Mania]----")
    print(f"\nHa {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")

    showWallet(wallet, nev)
    bet = int(input("\nKérlek rakj tétet [HUF]: "))
    if bet == 0:
        main_menu(wallet, nev)

    kor = int(input("\nHány kört szertnél játszani?: "))
    bet = bet * kor

    betCheck(wallet, bet, nev)

    wallet -= bet

    winnings = bet * 5

    winner = f"{Fore.LIGHTGREEN_EX}Gratulálok, megnyerted a JACKPOTOT! Nyereményed: {winnings}HUF{Fore.WHITE}"

    for i in range(kor):
        random_pepper = random.choice(pepper)
        random_lemon = random.choice(lemon)
        random_apple = random.choice(apple)

        print("\n| " + random_pepper + " | " + random_lemon + " | " + random_apple + " |")
        time.sleep(0.5)

        if random_pepper.__contains__("Black") & random_apple.__contains__("Black") & random_lemon.__contains__("Black"):
            print(winner)
            wallet += winnings
            scoreboardsave(gameData="G_Tycoon", winData=winnings,
                           szorzoData=round(winnings / bet, 3), betData=bet, wallet=wallet, nev=nev)
            time.sleep(3)
            tycoon(wallet, nev)
        elif random_pepper.__contains__("Red") & random_apple.__contains__("Red") & random_lemon.__contains__("Red"):
            print(winner)
            wallet += winnings
            scoreboardsave(gameData="G_Tycoon", winData=winnings,
                           szorzoData=round(winnings / bet, 3), betData=bet, wallet=wallet, nev=nev)
            time.sleep(3)
            tycoon(wallet, nev)
        elif random_pepper.__contains__("Green") & random_apple.__contains__("Green") & random_lemon.__contains__("Green"):
            print(winner)
            wallet += winnings
            scoreboardsave(gameData="G_Tycoon", winData=winnings,
                           szorzoData=round(winnings / bet, 3), betData=bet, wallet=wallet, nev=nev)
            time.sleep(3)
            tycoon(wallet, nev)
        else:
            print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
            time.sleep(1.5)

    print(f"{Fore.RED}Játék vége! :({Fore.WHITE}")

    time.sleep(1)

    tycoon(wallet, nev)

    return wallet



def sweet_bonanza(wallet, nev):

    lane1 = [f'{Fore.BLACK}Bonus Bomb', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']
    lane2 = [f'{Fore.BLACK}Bonus Bomb', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']
    lane3 = [f'{Fore.BLACK}Bonus Bomb', f'{Fore.MAGENTA}Grapes', f'{Fore.LIGHTYELLOW_EX}Banana', f'{Fore.YELLOW}Lemon', f'{Fore.LIGHTGREEN_EX}Pear', f'{Fore.LIGHTRED_EX}Strawberry{Fore.WHITE}']

    print("----[Sweet Bonanza]----")
    print(f"\nHa {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")

    showWallet(wallet, nev)
    bet = int(input("\nKérlek rakj tétet [HUF]: "))
    if bet == 0:
        main_menu(wallet, nev)

    kor = int(input("\nHány kört szertnél játszani?: "))
    bet = bet * kor

    betCheck(wallet, bet, nev=nev)

    wallet -= bet

    for i in range(kor):

        random_lane1 = random.choice(lane1)
        random_lane2 = random.choice(lane2)
        random_lane3 = random.choice(lane3)

        multipliers = ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '10', '10', '10', '10', '10', '25', '25', '25', '50', '50', '100']

        print("\n| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
        time.sleep(0.5)

        if random_lane1.__contains__("Bonus Bomb") & random_lane2.__contains__("Bonus Bomb") & random_lane3.__contains__("Bonus Bomb"):
            bbm = random.choice(multipliers)
            bbmPlusBet = int(bbm) * bet
            wallet += bbmPlusBet
            print(f"{Fore.LIGHTGREEN_EX}Gratulálok, nyertél!: {bbmPlusBet}HUF\n {Fore.LIGHTBLUE_EX}Szorzó: {bbm}x{Fore.WHITE}")
            scoreboardsave(gameData="S_Bonanza", winData=bbmPlusBet, szorzoData=bbm, betData=bet, wallet=wallet, nev=nev)
            time.sleep(3)
            sweet_bonanza(wallet, nev)

        elif random_lane1.__contains__("Bonus Bomb") & random_lane2.__contains__("Bonus Bomb"):
            bbm = 10
            bbmPlusBet = int(bbm) * bet
            wallet += bbmPlusBet
            print(f"{Fore.LIGHTGREEN_EX}Gratulálok, nyertél!: {bbmPlusBet}HUF\n {Fore.LIGHTBLUE_EX}Szorzó: {bbm}x{Fore.WHITE}")
            scoreboardsave(gameData="S_Bonanza", winData=bbmPlusBet, szorzoData=bbm, betData=bet, wallet=wallet,
                           nev=nev)
            time.sleep(3)
            sweet_bonanza(wallet, nev)

        elif random_lane1.__contains__("Bonus Bomb") & random_lane3.__contains__("Bonus Bomb"):
            bbm = 10
            bbmPlusBet = int(bbm) * bet
            wallet += bbmPlusBet
            print(f"{Fore.LIGHTGREEN_EX}Gratulálok, nyertél!: {bbmPlusBet}HUF\n {Fore.LIGHTBLUE_EX}Szorzó: {bbm}x{Fore.WHITE}")
            scoreboardsave(gameData="S_Bonanza", winData=bbmPlusBet, szorzoData=bbm, betData=bet, wallet=wallet,
                           nev=nev)
            time.sleep(3)
            sweet_bonanza(wallet, nev)

        elif random_lane2.__contains__("Bonus Bomb") & random_lane3.__contains__("Bonus Bomb"):
            bbm = 10
            bbmPlusBet = int(bbm) * bet
            wallet += bbmPlusBet
            print(f"{Fore.LIGHTGREEN_EX}Gratulálok, nyertél!: {bbmPlusBet}HUF\n {Fore.LIGHTBLUE_EX}Szorzó: {bbm}x{Fore.WHITE}")
            scoreboardsave(gameData="S_Bonanza", winData=bbmPlusBet, szorzoData=bbm, betData=bet, wallet=wallet,
                           nev=nev)
            time.sleep(3)
            sweet_bonanza(wallet, nev)

        else:
            print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
            time.sleep(1.5)

    print(f"{Fore.RED}Játék vége! :({Fore.WHITE}")

    time.sleep(1)

    sweet_bonanza(wallet, nev)

    return wallet


def horses(wallet, nev):

    print("----[Ló fogadás]----\n")

    print(f"\nHa {Fore.CYAN}0{Fore.WHITE} tétet raksz, visszalépsz a főmenübe!")

    showWallet(wallet, nev)

    bet = int(input("\nKérlek rakj tétet [HUF]: "))

    if bet == 0:
        main_menu(wallet, nev)

    betCheck(wallet, bet, nev)

    horses_list = ['PS', 'Xbox', 'Sprite', 'Harry Potter', 'Dominik', 'Ákos', 'Bug']

    print(horses_list, "\n")
    selected_horse = ""

    while not horses_list.__contains__(selected_horse):
        selected_horse = str(input("Kérlek válassz lovat!: "))

        if not horses_list.__contains__(selected_horse):
            print(f"Érvénytelen név! Próbáld újra!\n")
            time.sleep(1)

    winnings = bet * 6

    print(f"{Fore.LIGHTYELLOW_EX}A lovak épp futnak, szóval várnod kell...{Fore.WHITE}")
    time.sleep(5)

    random_horse = random.choice(horses_list)

    if selected_horse == random_horse:
        print(f"{Fore.LIGHTGREEN_EX}Gratulálok! A lovad ért be elsőnek, ezért nyertél {winnings}HUF{Fore.WHITE}")
        wallet += winnings
        scoreboardsave(gameData="Horses", winData=winnings, szorzoData=round(winnings / bet, 3), betData=bet, wallet=wallet, nev=nev)
        time.sleep(3)
    else:
        print(f"{Fore.RED}Béna! Vesztettél!{Fore.WHITE}")
        wallet -= bet
        print(f"A befutó ló: {Fore.MAGENTA}{random_horse}{Fore.WHITE} volt.")
        time.sleep(3)

    horses(wallet, nev)


def first_menu(nev):
    wallet = int(input("Kérlek add meg a kezdő összeget! [HUF]: "))

    if wallet <= 0:
        print(f"Nem adhaszt meg {Fore.CYAN}1{Fore.WHITE}-nél kisebb összeget!")
        first_menu(nev)
        return wallet

    else:
        # print(wallet)
        main_menu(wallet, nev)
        return wallet


def scoreboardboot(wallet, nev):
    beolvas = open("adatok.txt")
    adatok = []

    for sor in beolvas:
        adatok.append(sor.strip().split())  # sor.strip -> \n eltüntetése

    print("###### SCOREBOARD ######\n")
    for sor in adatok:
        if len(str(sor[2])) == 2:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" * 2 + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 3:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" * 2 + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 4:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" * 2 + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 5:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" * 2 + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 6:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 7:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 8:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 9:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        elif len(str(sor[2])) == 10:
            print(sor[0] + sor[1] + "\t  " + sor[2] + "\t" + sor[3] + "\t" + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t    " + sor[6] + "Ft" + "\t" + sor[7] + "x")

        # else:
        #     print(sor[0] + sor[1] + "\t" + sor[2] + "\t" + sor[3] + "\t" + sor[4] + "\t" + sor[5] + "Ft" + "\t" + sor[6] + "Ft" + "\t" + sor[7] + "x")

    f = 1
    while f != 0:
        f = int(input(f"\n{Fore.CYAN}0{Fore.WHITE}-val visszaléphetsz a főmenübe! \n"))

        if f == 0:
            main_menu(wallet, nev)
        else:
            print(f"A(z) {f} neked NULLA? [ 0 ]")
    return adatok, beolvas


def scoreboardsave(gameData, betData, winData, szorzoData, nev, wallet):
    adatok = []
    kiir = open("adatok.txt", "a")
    beolvas = open("adatok.txt", "r")  # amikor meghívjuk mindig a legújabbat kapja
    sorszam = []

    for sor in beolvas:
        adatok.append(sor.strip().split())

    for sor in adatok:
        szam = int(sor[0])
        if not int(sor[0]) > szam or not str(sor[0]) == "":
            sorszam = int(sor[0]) + 1

    current_time = datetime.today().strftime("%Y.%m.%d-%H:%M:%S")

    # print(current_time, nev, sorszam) # debug

    time.sleep(0.2)

    kiir.write("\n" + str(sorszam) + "\t" + ".hely" + "\t" + str(nev) + "\t" + current_time + "\t" + str(gameData) + "\t" + str(betData) + "\t" + str(winData) + "\t" + str(szorzoData))

    kiir.close()
    beolvas.close()
    main_menu(wallet, nev)


first_menu(nev=nevinput())
