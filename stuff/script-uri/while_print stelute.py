#Scrie un program care afiseaza urmatoarea structura, unde n = 6, folosind fct while:
#*
#**
#***
#****
#*****
#******
#END 
#b. modificati programul a.i. n sa fie introdus de la tastatura

n = int(input("Scrie un numar:"))
k = 1
while k <= n:
    print("*" * k)
    k = k + 1 #se mai poate scrie k += 1 si se numeste incrementare
print ("END")