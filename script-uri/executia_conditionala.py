# Executia conditionala - IF-ELSE
var1 = 135
if var1 % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

if True:
    print("Se executa.")

varsta = 17
if varsta >= 18:
    print("Acces permis!")
else:
    print("Acces respins!")
# == inseamna este egal cu 
# != inseamna diferit

print('')
print('')
print('')
#cand avem mai mult de 2 optiuni se foloseste combinatia if-elif-else
# operatori logici:
#and => si
#or => sau
#not => negare

ora = 22
if ora >= 5 and ora < 10: #[5,10)
    print("Buna dimineata!")
elif ora >=10 and ora < 19: #[10,19)
    print("Buna ziua!")
else:
    print("Buna seara!")
#se pot pune oricate elif iar else nu este obligatoriu
#if se poate folosi si singur, fara elif si else