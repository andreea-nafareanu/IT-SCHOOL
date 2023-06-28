
#matrice

matrix = [
    ["Ionel", [4, 5, 6 , 7, 8]],
    ["Ionut", [4, 7, 7, 8, 9]],
    ["Andrei", [7, 7, 8, 9, 10]],
    ["Sandu", [4, 5, 5, 3, 5]],
]
print(matrix[0][1][0])

print(sorted(matrix))

#sa se afiseze cea mai mare nota a fiecarui student

for i in matrix:
    print(i[0], "cea mai mare nota", max(i[1])) 
    print(i[0], "media este", sum(i[1])/len(i[1])) #media aritmetica

#cum citim o lista de la tastatura

input_list = []
n = int(input("nr elemente: "))
for i in range (n):
    input_list.append(int(input()))
print(input_list)