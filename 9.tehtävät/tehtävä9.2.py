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
auto = Auto("ABC-123", 142 )

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"{auto.nopeusnyt} km/h")

auto.kiihdytä(-200)

print(f"Hätäjarrutuksen jälkeen auton nopeus on {auto.nopeusnyt} km/h")



