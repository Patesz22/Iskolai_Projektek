# bemenet, koszont_e, felhaszn = "", False, "Idegen"
# 
# print("Segítségért írja be, hogy: help")
# 
# while True:
#     bemenet = input(f'{felhaszn}>'.lower())     # idegen
#     if bemenet == "help":
#         print("""
# 
#     szia        - üdvözli az AI.
#     időjárás    - Megnyitja nekünk a köpönyeg.hu/budapest-weboldalt
#     viszlát     - Elköszön az AI-tól és kilép
#     játék       - Játék az AI-al    
#         """)
# 
#     elif bemenet == "szia":
#         if not koszont_e:
#             print("Szia, én vagyok az az AI aki ....... téged!")
#             felhaszn = input("Téged hogy hívnak? ")
#             print(f"Szia {felhaszn}! Parancsolj...")
#             koszont_e = True
#         else:
#             print("Már bemutatkoztál.")
# 
#     elif bemenet == "viszlát":
#         if koszont_e:
#             print(f'Viszlát {felhaszn}! Várlak vissza..')
#             break
#         else:
#             print("Még nem mutatkoztál be, így nem tudok elengedni.")
# 
#     elif bemenet == "játék":
#         titkos_szam = int(input("Írja be a titkos számot: "))
#         tipp_limit = int(input("Mennyiszer szeretnél próbálokozni?: "))
#         eddigi_tippek = 0
# 
#         while eddigi_tippek <= tipp_limit:
#             tipp = int(input("A tipped?: "))
#             eddigi_tippek += 1
# 
#             if tipp > titkos_szam + 3 or tipp < titkos_szam -3:
#                 print("Hideg!")
#             elif tipp > titkos_szam + 2 or tipp < titkos_szam -2:
#                 print("Langyos!")
#             elif tipp > titkos_szam + 1 or tipp < titkos_szam - 1:
#                 print("Meleg!")
#             elif tipp == titkos_szam + 1 or tipp == titkos_szam -1:
#                 print("Forró!")
#             else:
#                 print("Eltaláltad!")
#                 eddigi_tippek = tipp_limit
#                 break
# 
#         else:
#             print("Szép játék volt! (Noob shit!)")
# 
#     elif bemenet == "időjárás":
#         if not koszont_e:
#             print("Nem dolgozok idegeneknek!")
#         else:
#             import webbrowser
#             print("Igen, mester!")
#             webbrowser.open_new("https://koponyeg.hu/elorejelzes/Budapest")
#     else:
#         print("Nincs ilyen parancsol! Próbálkozz a 'help' paranccsal!")




