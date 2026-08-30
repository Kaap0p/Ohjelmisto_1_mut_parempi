import random

määrä = int(input("Anna arpojen määrä: "))

summa = 0

for _ in range(määrä):
    silmäluku = random.randint(1, 6 )
    summa += silmäluku

print(f"silmälukujen summa on {summa}")

