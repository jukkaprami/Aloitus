# KUNTOILIJAN TIEDOT JA OLIO-OHJELMOINTINA
# ----------------------------------------

# Kirjastot ja modulit (libraries and modules)
# -------------------

import fitness

# Luokkamääritykset (class of definitons)
# -----------------

# Kuntoilija luokka yliluokka JunioriKuntoilijalle (super fitness)
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
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi rasvaprosentin laskemiseen (Yleinen / Aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

# JunioriKuntoilija luokka Kuntoilija luokan yliluokka (subclass)
class JunioriKuntoilija(Kuntoilija):
    ###Luokka nuoren kuntoilijan tiedoille###
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään, periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)
    

     # Metodi rasvaprosentin laskemiseen (Ylikirjoitettu )
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti



if __name__ == "__main__":
    
    # Luodaan olio luokasta Kuntolija
    kuntoilija = Kuntoilija('Kalle kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg' )
    # print('painoindeksi on ', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija(' aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg' )
    # print('painoindeksi on ', kuntoilija.painoindeksi())
    rasvaprosentti = juniorikuntoilija.rasvaprosentti()
    print('rasvaprosentti on', rasvaprosentti)
