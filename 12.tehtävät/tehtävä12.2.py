import requests

kaupunki = input("Anna paikkakunnan nimi: ")

api_avain = "OMA_API_AVAIN_TAHAN"

url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"

vastaus = requests.get(url)

if vastaus.status_code == 200:
    data = vastaus.json()

    sää = data["weather"][0]["description"]
    lämpötila_kelvin = data["main"]["temp"]
    lämpötila_celsius = lämpötila_kelvin - 273.15

    print(f"Säätila: {sää}")
    print(f"Lämpötila: {lämpötila_celsius:.1f} °C")
else:
    print("Paikkakuntaa ei löytynyt tai pyyntö epäonnistui.")