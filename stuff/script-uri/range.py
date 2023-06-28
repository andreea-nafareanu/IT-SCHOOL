r1 = range(10) #incepe de la 0 pana la 10-1=9
r2 = range(45, 90) #45 este inclus, 90 nu este inclus
r3 = range(20, 40, 2) #numara din 2 in 2 in range-ul indicat ATENTIE fara 40
        #start, stop, pas
r4 = range(50, 24, -5) # scade 5 incapand de la 50 pana la 24 (care nu e inclus)

for i in r1:
    print(i)

for i in r2:
    print(i)

for i in r3:
    print(i)

for i in r4:
    print(i)

#Afisati multiplii de 3 in range-ul 3-100:

for i in range(3, 100, 3):
    print(i)

# Sa se afiseze suma multiplilor de 5 din intervalul 0-1000
counter = 0
for i in range (1, 1001, 5):
    counter += i
print(counter)



