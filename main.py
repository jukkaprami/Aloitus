from microbit import *

def heart():
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART)

weather = ""

while True:


#Mitataan sataako vettä
    if pin0.logo_touched():
        weather='vetta'
        

#Ensimmäinen ehto
    if weather == 'vetta':
        # print('Muista sateenvarjo!')
        display.scroll('muista sateenvarjo!')
        
#Toinen ehto
    elif weather == 'lunta' :
        #print('Muista hanskat')
        display.scroll('muista hanskat')
        
#Kolmas ehto
    elif weather == 'aurinkoista':
        #print('Muista aurinkolasit')
        display.scroll('Muista aurinkolasit')
        
#Muutoin
    # else:
        #print('Etsi sopivat varusteet, ei vettä, lunta, eikä aurinkoista')
        display.scroll('Etsi sopivat varusteet, ei vettä, lunta, eikä aurinkoista')
        