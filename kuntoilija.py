# KUNTOILIJAN TIEDOT JA OLIO-OHJELMOINTINA
# ----------------------------------------

# Kirjastot ja modulit (libraries and modules)
# -------------------

import fitness

# Luokkamääritykset (class of definitons)
# -----------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    #Olionmuodostin elin konstruktio
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field) 
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    # Metodi painoindeksin laskemiseen
    def painoindeksi(self):
        bmi = fitness.laske_bmi(self.paino, self.pituus)
        print(bmi)

if __name__ == "__main__":
    
    # Luodaan olio luokasta Kuntolija
    kuntoilija = Kuntoilija('Kalle kuntoilija', 175, 77, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg' )
    kuntoilija.painoindeksi()

