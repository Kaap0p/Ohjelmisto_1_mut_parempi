lentoasemat = {}

while True:
    print("Mitä haluat tehdä?")
    print("1.Syöttää uuden lentoaseman")
    print("2.Hakea lentoaseman tietoja")
    print("3.lopeta")
    valinta = input("Valitse toiminto:")

    if valinta == "1":
        icao = input("anna lentoaseman ICAO-koodi:")
        nimi = input("anna lentoaseman nimi:")
        lentoasemat[icao] = nimi
        print("lentoasema tallennettu", lentoasemat[icao])

    if valinta == "2":
        icao_haku = input("anna lentoaseman ICAO-koodi:")
        if icao_haku in lentoasemat:
            print (lentoasemat[icao_haku])
        else:
            print("Tietoa ei ole tallennettu")

    if valinta == "3":
        break




