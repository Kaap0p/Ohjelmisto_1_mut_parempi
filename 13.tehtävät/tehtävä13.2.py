from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/kentta/<icao>")
def hae_kentta(icao):

    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="",
        user="",
        password=,
        autocommit=True
    )

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """

    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
    else:
        vastaus = {
            "Error": "Airport not found"
        }

    kursori.close()
    yhteys.close()

    return jsonify(vastaus)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)