students = ["Mihai" , "Andrei" , "Maria"] #minimul si maximul din 
print(max(students)) #le calculeaza dupa ASCII

print('')

temp = [33, 22, 34, 21, 22, 0]
temp_sorted = sorted(temp) # trebuie sa luam o variabila cu care sa egalam lista sortata ascendent
print (temp)
print(temp_sorted)

print('')

temp = [33, 22, 34, 21, 22, 0]
temp_sorted = sorted(temp, reverse=True) # trebuie sa luam o variabila cu care sa egalam lista sortata DESCENDENT
print (temp)
print(temp_sorted)

print('')

temp.sort() #sortare crescatoare cu METODA

print(temp)

print('')

temp.sort(reverse=True) #sortare descrescatoare cu METODA

print(temp)