kuhan_pituus = int(input("kuhan pituus:"))

if kuhan_pituus < 37:
    puuttuu = 37 -kuhan_pituus
    print(f"Kuha on alamittainen, palauta se järveen broski! Kuhan pituudesta puuttuu {puuttuu} cm")
else:
    print("Hieno kuha broski!")