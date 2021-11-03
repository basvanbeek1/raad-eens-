import random
import time 

het_getal = random.randint(1,1000)
print("""welkom bij het raad spel je hebt zometeen 10 pogingen
in die pogingen moet je een getal raden tussen de 1 en 1000 succes! """)
time.sleep(7)

aantal_pogingen = 0 
while aantal_pogingen < 10:
    teraden_getal = int(input('raad het getal hier\n'))
    aantal_pogingen += 1
    if teraden_getal < het_getal:
        print('Je geraden getal is te laag')
    if teraden_getal > het_getal:
        print('Je geraden getal is te hoog')
    if teraden_getal == het_getal:
        break
if teraden_getal == het_getal:
    print('Je hebt het nummer in ' + str(aantal_pogingen) + ' pogingen!')
else:
    print('Je hebt het getal niet goed geraden het was ' + str(het_getal))




