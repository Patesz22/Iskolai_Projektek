szamlalo = int(input("Kérem a számlálót: "))
nevezo = int(input("Kérem a nevezőt: "))

if szamlalo > nevezo:
    print("Ez a tört nagyobb, mint egy egész.")
elif szamlalo < nevezo:
    print("Ez a tört kisebb, mint egy egész.")
elif szamlalo == nevezo:
    print("Ez a tört egész.")
