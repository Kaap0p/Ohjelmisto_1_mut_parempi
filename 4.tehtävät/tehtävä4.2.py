while True:
    tuumia = float(input("Anna tuuma määrä: "))

    if tuumia < 0:

        print("Ohjelma lopetettu!")
        break

    cm = tuumia * 2.54
    print(f"{tuumia} tuumaa on {cm} cm")




