luvut = []

while True:
    syöte=(input("anna uusi luku (tyhjä lopettaa ohjelman!): "))

    if syöte == "":
        break

    luku = int(syöte)
    luvut.append(luku)

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print(f"5 suurinta lukua on {viisi_suurinta}")