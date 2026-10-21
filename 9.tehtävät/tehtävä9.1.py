
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeusnyt = 0
        self.matka = 0


auto = Auto("ABC-123", 142 )

print(auto.rekisteritunnus)
print(f"{auto.huippunopeus} km/h")
print(auto.nopeusnyt)
print(auto.matka)








