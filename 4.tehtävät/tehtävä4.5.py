oikea_tunnus = "jari"
oikea_salasana = "jari123"
yritykset = 0
onnistui = False

while yritykset < 5 and not onnistui:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        onnistui = True
    else:
        yritykset += 1
        print("Väärä tunnus tai salasana!")

    if onnistui:
        print("Tervetuloa!")
    else:
        print("Pääsy evätty!")



