# I. Ex1. Sa se converteasca in binar (baza 2) urmatoarele numere: 16, 32, 64, 128, 100, 10, 54, 33
print (bin(16)) 
print (bin(32)) 
print (bin(64)) 
print (bin(128)) 
print (bin(100)) 
print (bin(10)) 
print (bin(54)) 
print (bin(33)) 

print('')

# I. Ex2. Sa se converteasca in decimal (baza 10) urmatoarele numere: 1010 0101, 1111 1111,  0010 0001, 1000 0000
print(int('10100101',2))
print(int('11111111',2))
print(int('00100001',2))
print(int('10000000',2))

print('')

# II. Ex1. Definiti 2 variabile; prima reprezinta varsta voastra iar a 2-a numele.
age = 33
name = "Andreea"

print('')
# II. Ex2. Definiti o variabila care reprezinta totalul cosului de cumparturi; valoarea initiala este 0;
    #a. verificati tipul variabilei
    #b. alocati valoarea 34.56
    #c. verificati tipul variabilei
    #d. convertiti valoarea variabilei la numar intreg
val_cos = 0
print (type (val_cos))
val_cos = 34.56
print (type (val_cos))
print (int (val_cos))

print('')

# Ex3. Definiti o variabila cu valoarea None
    #a. alocati valoarea True
    #b. alocati valoarea "True"
    #c. convertiti valoarea in numar real
var = None
var = 1.5
print ( bool(var))
print ( int (var))

print('')

# Ex4. Definiti o variabila care are valoarea "00001010"
    #a. sa se salveze intr-o noua variabila, valoarea in baza 10
    #b. as se afiseze valoarea decimala obtinuta
var = '00001010'
new_var = int (var, 2)
print (new_var)
