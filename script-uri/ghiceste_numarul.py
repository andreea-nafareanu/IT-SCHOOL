from random import randint
ran_nr = randint (1 , 99)

print("Incepe jocul!")
n = int(input("Introduceti un numar intre 1 si 99: "))
while n != ran_nr:
    if n < ran_nr:
        print("Incearca un numar mai mare!")
    else:
        print("Incearca un numar mai mic")
    n = int(input("Introduceti un numar intre 1 si 99: "))
print("Ai ghicit numarul. Felicitari!")
print("Numarul generat a fost", ran_nr,".")
        