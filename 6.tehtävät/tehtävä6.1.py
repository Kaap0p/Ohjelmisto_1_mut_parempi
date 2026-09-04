import random
def luvut():
    silmäluku = random.randint(1, 6)
    return silmäluku

tulos = luvut()
print(f"silmäluvuksi tuli: {tulos}")

while tulos < 6:
        tulos = luvut()
        print(f"silmäluvuksi tuli: {tulos}")
