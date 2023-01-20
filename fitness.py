# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat
pituus_teksti = input('Kuinka pitkä olet (cm):') # Kysytään käyttäjältä
paino_teksti = input('Kuinka paljon painat (kg):') # Kysytään käyttäjältä
pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
paino = float(paino_teksti) # Muutetaan liukuluvuksi

'''
pituus_metreina = pituus / 100

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)

'''
# Määritellään funtio painoindeksin laskentaan
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

