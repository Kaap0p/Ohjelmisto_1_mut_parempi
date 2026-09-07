nimet = set()
while True:
    nimi = input("anna nimi:")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimi = nimet.add(nimi)
        print("syötetyt nimet")
        for n in nimet:
            print(n)

