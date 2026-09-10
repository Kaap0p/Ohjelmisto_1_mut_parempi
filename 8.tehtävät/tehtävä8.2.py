import mysql.connector
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="PYTHONDUMMY",
    password="MEOW",
    database="flight_game",
    autocommit=True
)

kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi: ")

sql = """ SELECT type, COUNT(*)
FROm airport
WHERE iso_country = %s
GROUP BY type
"""

kursori.execute(sql, (maakoodi,))
tulokset = kursori.fetchall()

if tulokset:
    print(f"Lentokenttiä maassa {maakoodi} tyypeittäin:")
    for tyyppi, maara in tulokset:
        print(f"{tyyppi}: {maara} kpl")
else:
    print("Kyseisellä maakoodilla ei löytynyt lentokenttiä.")

kursori.close()
yhteys.close()