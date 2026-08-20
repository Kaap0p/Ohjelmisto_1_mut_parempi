sukupuoli = input("Anna sukupuolesi: ")
hemoglobiini  = float(input("Anna hemoglobiini arvosi: "))

if sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("hemoglobiini arvot ovat kunnossa")
elif sukupuoli == "mies" and 134 <= hemoglobiini <= 195:
    print("hemoglobiini arvot ovat kunnossa")
else:
    print("Hemoglobiini arvot eivät ole kunnossa")