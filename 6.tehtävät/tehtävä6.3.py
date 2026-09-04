def määrä(gallonaa):
    litrat = gallonaa * 3.785
    return litrat


gallonaa = float(input("kuinka monta gallonaa bensaa?: "))


while gallonaa >= 0:
    litrat = määrä(gallonaa)
    print(f"{gallonaa} gallonaa on {litrat} litraa")

    gallonaa = float(input("kuinka monta gallonaa bensaa?: "))

print("ohjelma lopetettu! negatiivinen arvo annettu.")