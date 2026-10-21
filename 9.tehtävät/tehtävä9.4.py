import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.matka = 0


    def kiihdytä(self, muutos):
        self.nopeusnyt += muutos
        if self.nopeusnyt > self.huippunopeus:
            self.nopeusnyt = self.huippunopeus

        if self.nopeusnyt < 0:
            self.nopeusnyt = 0


    def kulje(self, tunnit):
        self.matka = self.matka + tunnit * self.nopeusnyt

autot = []


for i in range(1,11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100,200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_käynnissä = True

while kilpailu_käynnissä:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_käynnissä = False
def tulosta_voittaja(autot):
    voittaja = autot[0]

    for auto in autot:
        if auto.matka > voittaja.matka:
            voittaja = auto
    print(f"Voittaja on {voittaja.rekisteritunnus}")

for auto in autot:
    print(f"Rekisteritunnus: {auto.rekisteritunnus} Huippunopeus: {auto.huippunopeus} Tämänhetkinen nopeus: {auto.nopeusnyt} Kuljettu matka: {auto.matka} \n")

tulosta_voittaja(autot)




