# Lista goala:
students = []
students1 = list() #o alternativa de a apela o lista goala (cele 2 randuri sunt echivalente)

#Lista cu valori:
students = ["Marian", "Catalin", "Calin", "Ionut"]

for name in students:
    print(name)

for x in "Andreea":
    print(x)

for i in range(10):
    print(i)

for c in "Andreea Nafareanu":
    if c == "a":
        continue #keyword al lui for care da skip la o iteratie
    print(c)

for c in "Andreea Nafareanu":
    if c == "a":
        continue #keyword al lui for care da skip la o iteratie
    print(c)

students = ["Marian", "Catalin", "Calin", "Ionut"]

for student in students:
    if student == "Catalin":
        print (student)
        break #keyword care opreste o iteratie o data ce a indeplinit conditia
    else:
        print("Alt student")