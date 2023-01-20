# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat

#Kysytään käyttäjältä
pituus_teksti = input('Kuinka pitkä olet (cm): ')
paino_teksti = input('Kuinka paljon painat (kg): ')
ika_teksti = input('Kuina vanha olet: ')
Sukupuoli = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')

#Muutetaan vastaukset liukuluvuiksi
pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
paino = float(paino_teksti) # Muutetaan liukuluvuksi
ika = float(ika_teksti)
sukupuoli = float


# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laske painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        _float: painoindeksi desimaalin tarkkuudella_
    """
    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi= round (bmi, 1)
    return bmi

bmi = laske_bmi(75, 172)

print('laskin painoindeksin se on', bmi)

def aikuisen_rasvaprosentti(bmi,ikä,sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ikä (float): henkilon ika
        sukupuoli (float): 1 > mies, 0 > nainen
    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti =round(rasvaprosentti)
    return aikuisen_rasvaprosentti
    
oma_bmi = laske_bmi (paino, pituus)
oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, Sukupuoli)

print('Painoindeksisi on', oma_bmi, 'ja kehon rasvaprosentti on', oma_rasvaprosentti)

