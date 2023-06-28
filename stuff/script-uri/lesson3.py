#operatori matematici - adunarea
result = 3+5 #adunare
print(result)

print("")

result = "IT " + "School" #concatenate
print(result)
print("")
varsta = 33
result = "Varsta mea este " + str(varsta) +" ani"
print(result)

#funtiile de mai jos transforma tipul de date si se numeste cast sau casting
int()
float()
bool()
str()

#scaderea

a=4
b=3.4
print(a-b)

#inmultirea
buc = 34
price = 3
total = buc * price
print (total)

print("")

print ("Andreea" * 3) # multiplica un string 

#impartirea
a = 2342
b = 26
print(a / b)
print ("Catul impartirii: " + str(a // b))
print ("Restul impartirii: " + str(a % b)) #modulo - foarte folosit

#Putem folosi modulo sa aflam daca un nr e par sau impar
test_number = 234
rest = test_number % 2
is_even = not bool(rest) #adaug un operator logistit "not" care neaga fct bool()
print( str(test_number) + " este par", is_even)
