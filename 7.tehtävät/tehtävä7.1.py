vuoden_ajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("anna kuukausi:" ))

if kuukausi in (12, 1, 2):
    indeksi = 0
elif kuukausi in (3, 4, 5):
    indeksi = 1
elif kuukausi in (6, 7, 8):
    indeksi = 2
else:
    indeksi = 3

print(f"vuodenaika on {vuoden_ajat[indeksi]} ")
