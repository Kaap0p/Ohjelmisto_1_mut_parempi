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


auto = Auto("ABC-123", 142 )

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

auto.kulje(1.5)


print(f"Auton rekisteritunnus on {auto.rekisteritunnus}.")
print(f"Auton huippunopeus on {auto.huippunopeus} km/h.")
print(f"Auton tämänhetkinen nopeus on {auto.nopeusnyt} km/h.")
print(f"Auton matka on {auto.matka} km.")
