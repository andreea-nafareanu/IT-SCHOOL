# Sa se scrie un program prin care in functie de anul nasterii se verifica daca varsta este 
# mai mica sau mai mare cu 18 ani pt a avea sau nu acees. 

year = int(input("Care este anul nasterii? "))
age = 2023 - year
if age >= 18:
    print("Accesul este permis!")
    print("Bun venit.")
else:
    print("Accesul este respins!")