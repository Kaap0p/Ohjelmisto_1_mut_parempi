import random

N = int(input("anna arvottavien pisteiden määrä:"))

n = 0

for _ in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*x + y*y < 1:
        n += 1

piin_likiarvo = 4 * n / N

print(f"piin likiarvo: {piin_likiarvo}")
