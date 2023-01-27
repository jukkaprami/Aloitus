# KUNTOILIJAN TIEDOT JA OLIO-OHJELMOINTINA
# ----------------------------------------

# Kijastot ja modulit (libraries and modules)
# -------------------

import fitness

# Luokkamääritykset (class of definitons)
# -----------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field) 
        self.nimi = nimi
        self.pituus = pituus
        self.ika = ika
        self.sukupuoli = sukupuoli

        

