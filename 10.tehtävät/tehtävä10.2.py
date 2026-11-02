import time

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä ):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []

        for i in range(hissien_määrä):
            uusi_hissi = Hissi(ylin_kerros, alin_kerros, i + 1)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_nro, kohde_kerros ):
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry(kohde_kerros)



class Hissi:

    def __init__(self, ylin_kerros, alin_kerros, numero):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.nykyinen_kerros = alin_kerros
        self.numero = numero




    def ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1
        print(f"hissi{self.numero} on kerroksessa {self.nykyinen_kerros}.\n")
        time.sleep(1)


    def alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1
        print(f"Hissi{self.numero} on kerroksessa {self.nykyinen_kerros}.\n")
        time.sleep(1)


    def siirry(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros:
            print("Virhe. Hissi ei voi mennä korkeammalle!")
            return

        elif kohde_kerros < self.alin_kerros:
            print("Virhe. Hissi ei voi mennä alemmas!")
            return

        if kohde_kerros > self.nykyinen_kerros:
            while kohde_kerros > self.nykyinen_kerros:
                self.ylös()


        elif kohde_kerros < self.nykyinen_kerros:
            while kohde_kerros < self.nykyinen_kerros:
                self.alas()

        else:
            print("Hissi on jo kutsutussa kerroksessa!")


t = Talo(1, 6, 3)
t.aja_hissiä(2, 5)
t.aja_hissiä(3, 4)
t.aja_hissiä(1, 3)










