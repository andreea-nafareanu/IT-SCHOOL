user_ids = [324, 345, 536, 64]

print ("Lungime lista: " , len(user_ids)) #functia len() ne arata lungimea listei
print ("Ultimul element: ", user_ids[len(user_ids)-1]) #afiseaza ultimul element din lista
print("Ultimul element: " , user_ids[-1]) #afiseaza ultimul element din lista
print("Primul element: ", user_ids[0]) #afiseaza primul element
 
index_dorit = 10
if len(user_ids) > index_dorit: 
    print ("Elementul de pe pozitia " , index_dorit , "este ", user_ids[index_dorit])
else:
    print("Indexul", index_dorit, " nu exista.")    

print("END")