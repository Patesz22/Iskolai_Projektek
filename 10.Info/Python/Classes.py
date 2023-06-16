# Classes (osztályok)

# class Person:
#     def __init__(self, nev):
#         self.nev = nev
#
#     def koszonom_mindenkinek(self):
#         print(f"Köszönöm {self.nev} vagyok!")
#
# jancsi = Person("Menő Jani")
# bela = Person("Balogh Béla")
#
# jancsi.koszonom_mindenkinek()
# bela.koszonom_mindenkinek()

# #####################################################################################################################################################################################################################################################################################

# class Animal:
#     def eat(self):
#         print("Éppen eszik....")
#
# class Cat(Animal):
#     def karmol(self):
#         print("Karmol....")
#
# class Dog(Animal):
#     def harap(self):
#         print("Harap....")
#
# cat1 = Cat()
# cat1.eat()
# cat1.karmol()
# # cat1.harap() Nem fut le mert Dog(Animal) és nem Cat(Animal)
#
#
# dog1 = Dog()
# dog1.harap()

# #####################################################################################################################################################################################################################################################################################

# class Vereb:
#     merges = False
#     suly = 0.05
#     szin = "Barna"
#
#     def __init__(self, old_woman_is_near):
#         self.merges = old_woman_is_near
#         self.suly = 0.05
#
#     def repul(self):
#         if self.merges:
#             self.szin = "Zöld"
#             self.suly += 5
#             print(f"{self.szin} {self.suly} kilós mérges Huuuuuuuuullkkk Támad!!!")
#         else:
#             print(f"{self.szin} {self.suly} kilós nyugis veréb repül....")
#
# bemenet = input("Van e nyanya a közelben? (y/n): ")
#
# if bemenet == "y":
#     old_woman_is_near = True
# else:
#     old_woman_is_near = False
#
# vereb1 = Vereb(old_woman_is_near)
#
# vereb1.repul()

# #####################################################################################################################################################################################################################################################################################

# class Driver:
#     stilus = "tahó"
#     car = "sárga"
#     tag = False
#
# class TaxisNemzedek(Driver):
#     szabaly = "szabalytalan"
#
#     def __init__(self, ujonc):
#         self.tag = ujonc
#
#     def vezet(self):
#         if self.tag:
#             self.szabaly = "szabályos"
#             print(f"Tulajdonságai: Egy {self.szabaly} {self.stilus}, aki egy {self.car} kocsit vezet....")
#
#         else:
#             self.car = "fekete"
#             print(f"Tulajdonságai: Egy {self.szabaly} {self.stilus}, aki egy {self.car} kocsit vezet....")
#
# bemenet = input("Új taxis vagy-e? (y/n) ")
#
# if bemenet == "y":
#     ujonc = True
# elif bemenet == "n":
#     ujonc = False
#
# taxis1 = TaxisNemzedek(ujonc)
# taxis1.vezet()

# #####################################################################################################################################################################################################################################################################################

# class Maszk:
#     kotelezo = True
#     visel = True
#
#
#     def ellenőrzés(self, visel):
#         self.visel = visel
#         if self.visel and self.kotelezo:
#             print("Minden rendben van")
#         elif not self.visel and self.kotelezo:
#             print("A maszk kötelező, de nincs rajtad!!!!")
#         elif not self.visel and not self.kotelezo:
#             print("Nincs bünti, mert nem kötelekő a maszk!")
#
# bemenet = input("Van rajtad maszk? ")
#
# if bemenet == "y":
#     Maszk.visel = True
# elif bemenet == "n":
#     Maszk.visel = False
#
# maszk1 = Maszk()
# maszk1.ellenőrzés()

# #####################################################################################################################################################################################################################################################################################





