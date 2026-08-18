leiviskät = float(input("Leiviskät:"))
naulat = float(input("Naulat:"))
luodit = float(input("Luodit:"))



luodit_yhteensä = (leiviskät * 20 * 32) + (naulat * 32) + luodit
grammat_yhteensä = luodit_yhteensä * 13.3
kilogrammat = int(grammat_yhteensä // 1000)
grammat = grammat_yhteensä % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat} grammaa.")



