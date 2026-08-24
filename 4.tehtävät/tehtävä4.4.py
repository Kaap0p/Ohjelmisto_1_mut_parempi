import random

salainen = random.randint(1, 10)
arvaus = int(input("Anna luku:"))

while arvaus != salainen:
    if arvaus < salainen:
        print("Liian pieni!")
    if arvaus > salainen:
        print("Liian suuri!")

    arvaus = int(input("Arvaa uudelleen:"))

print(f"Oikein salainen numero oli {salainen}!")






