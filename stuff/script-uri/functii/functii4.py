
#sa se afiseze toate numerele impare din intervalul (0, 50)
def is_even(number):
    if number % 2 ==0:
        return True
    else:
        return False
    
for i in range (0,51):
    if not is_even(i):
        print(i)

#scrieti o functie care returneaza volumul unui cilindru in litri. 
#Acesta va primi doua argumente reprezentand inaltimea si raza bei in metri. 
#raza cilindrului = pi x rpatrat x h

PI = 3.14

def cylinder_volume (r, h):
    volume = PI * (r*r) * h / 1000 
    return volume

print (f"Volumul cilindrului este: {cylinder_volume(1,1)} litri")


