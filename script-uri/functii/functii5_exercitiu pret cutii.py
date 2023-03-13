#Managerul de la fabrica de cutii are nevoie de un program care calculeaza pretul
#cutiilor in functie de dimensiunea si grosimea lor. Pentru o cutie cu volumul de 1000 de litri
#de gorsime 1, pretul este de 25 de lei.
#Pentru gorosimile 2 si 3, pretul creste cu 10 respectiv 20 la suta.
#Scrieti o functie care primeste 4 parametrii:
#- inaltimea cutiei
#- latimea cutiei
#- lungimea cutiei
#- tipul de carton (1, 2 sau 3)
#Functia returneaza pretul.

def pret_cutie(inaltime_cutie, latime_cutie, lungime_cutie, tip_carton):
    """Returneaza pretul cutiei in functie de volum si tip carton"""
    if not isinstance (inaltime_cutie, float):
        return 0
    if not isinstance (latime_cutie, float):
        return 0
    if not isinstance (lungime_cutie, float):
        return 0
    if not isinstance (tip_carton, float):
        return 0
    pret_brut = inaltime_cutie * latime_cutie * lungime_cutie * 25
    if tip_carton ==1:
        return pret_brut
    if tip_carton == 2:
        return pret_brut * 1.1
    if tip_carton == 3:
        return pret_brut * 1.2
    return -1

inaltime_cutie = float (input("Inaltime cutie: "))
latime_cutie = float (input("Latime cutie: "))
lungime_cutie = float (input("Lungime cutie: "))
tip_carton = float (input("Tip carton: "))
print (f"Pretul pentru cutie este: {pret_cutie (inaltime_cutie, latime_cutie, lungime_cutie, tip_carton):.2f} RON.")

#Scrieti o functie care genereaza o oferta de pret pentru managerul de la fabrica 
#de cutii. Functia trebuie sa aplice un discount de cantitate. Pentru fiecare 100 de cutii se
#aplica 1% reducere. Functia primeste toti parametrii necesari pentru calculul pretului cutiei si
#inca un parametru care reprezinta numarul de cutii.

def oferta_pret(inaltime_cutie, latime_cutie, lungime_cutie, tip_carton, cantitate):
    """Calculeaza pretul per cutie oferind un discount de 1% pentru fiecare 100 cutii"""
    pret_per_cutie = pret_cutie(inaltime_cutie, latime_cutie, lungime_cutie, tip_carton)
    discount = cantitate // 100
    pret_final =  pret_per_cutie * (cantitate * (100-discount) / 100)
    return pret_final
cantitate = float (input("Cantitate solicitata: "))
print (f"Oferta de pret cu discount este: {oferta_pret(inaltime_cutie, latime_cutie, lungime_cutie, tip_carton, cantitate):.2f} RON.")
