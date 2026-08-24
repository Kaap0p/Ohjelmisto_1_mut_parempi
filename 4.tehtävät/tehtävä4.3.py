eka = True
pienin = 0
suurin = 0

while True:

    syote = input("anna luku (tyhjä lopettaa): ")

    if syote == "":
        print("lopettaa!")
        break

    luku = float(syote)

    if eka:

        pienin = luku
        suurin = luku
        eka = False

    else:
        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

    print("pienin: ", pienin)
    print("suurin: ", suurin)






