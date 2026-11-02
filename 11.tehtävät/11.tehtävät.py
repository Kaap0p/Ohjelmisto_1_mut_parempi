class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot_kirja(self):
        print(f"Kirjan nimi on {self.nimi}.")
        print(f"Kirjoittaja on {self.kirjoittaja}.")
        print(f"sivumäärä on {self.sivumäärä}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
        self.nimi = nimi


    def tulosta_tiedot_lehti(self):
        print(f"Lehden nimi on {self.nimi}.")
        print(f"lehden päätoimittaja on {self.päätoimittaja}\n")

lehti = Lehti("Aku ankka", "Aku Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti.tulosta_tiedot_lehti()
kirja.tulosta_tiedot_kirja()



