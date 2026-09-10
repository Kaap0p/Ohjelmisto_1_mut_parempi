import mysql.connector

yhteys = mysql.connector.connect(

    host = "127.0.0.1",
    port = 3306,
    user = "PYTHONDUMMY",
    password = "MEOW",
    database = "flight_game",
    autocommit = True
)
kursori = yhteys.cursor()

icao = input("Anna lentoaseman icao-koodi: ")

sql = "SELECT name, municipality from airport where ident = %s"
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print(f"Lentokentän nimi: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")

else: print("Lentoasemaa ei löytynyt annetulla icao-koodilla")
kursori.close()
yhteys.close()