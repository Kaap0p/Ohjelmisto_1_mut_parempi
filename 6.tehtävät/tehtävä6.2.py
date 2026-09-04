import random
def luvut(tahkot):
    silmäluku = random.randint(1, tahkot)
    return silmäluku
tahkot = int(input("Monta tahkoa on?: "))

maksimisilmäluku = tahkot

tulos = luvut(tahkot)

print(f"silmäluvuksi tuli: {tulos}")

while tulos != tahkot:
        tulos = luvut(tahkot)
        print(f"silmäluvuksi tuli: {tulos}")
