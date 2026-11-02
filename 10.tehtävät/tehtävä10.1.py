import time


class Hissi:

    def __init__(self, ylin_kerros, alin_kerros):
        self.ylin_kerros = 6
        self.alin_kerros = 1
        self.nykyinen_kerros = self.alin_kerros



    def ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1
        print(f"hissi on kerroksessa {self.nykyinen_kerros}.\n")
        time.sleep(1)


    def alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}.\n")
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

h = Hissi(6, 1)
h.siirry(6)
h.siirry(h.alin_kerros)









