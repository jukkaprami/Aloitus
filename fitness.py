# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat




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


def aikuisen_rasvaprosentti(bmi,ika,sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ikä (float): henkilon ika
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti =round(rasvaprosentti)
    return rasvaprosentti
    




def lapsen_rasvaprosentti(bmi,ika,sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): ika
        sukupuoli (sukupuoli): 1 > poika, 0 > tyttö

        Returns:
            float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi + 0.70 * 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti)
    return lapsen_rasvaprosentti

if __name__ == "__main__":

    #Kysytään käyttäjältä
    pituus_teksti = input('Kuinka pitkä olet (cm): ')
    paino_teksti = input('Kuinka paljon painat (kg): ')
    ika_teksti = input('Kuina vanha olet: ')
    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')

    #Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
    paino = float(paino_teksti) # Muutetaan liukuluvuksi
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)

    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi (paino,pituus)

    # Yli 18 vuotilailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print('painoindeksisi on', oma_bmi,
     'ja kehon rasvaprosentti on', oma_rasvaprosentti)
