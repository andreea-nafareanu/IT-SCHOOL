#scrieti o functie care verifica daca un nr este par. 
#daca este par returneaza True, altfel False. Functia are un singur argument. 


def is_even(number):
    if number % 2 ==0:
        return True
    else:
        return False
    
def add_one (number):
    number += 1

a = 3
a_even = is_even(a)
print (f"Variabila a este numar par? {a_even}")

print (f"a = {a}")
add_one (a)
print (f"a = {a}")