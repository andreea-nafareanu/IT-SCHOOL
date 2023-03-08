temp = [33, 22, 34, 21, 22, 0]
print ("22 apare de ", temp.count(22) , " ori in lista.") # numara de cate ori apare o valoare in lista
temp.remove(22) #elimina doar prima aparitie a lui 22
print(temp)

temp1 = temp.copy() #copiaza o lista 
temp.reverse() # modifica oridinea obiectelor din lista

print (temp)
print (temp1)

print("Temperatura minima este: " , min(temp))
print("Temperatura maxima este: " , max(temp))

