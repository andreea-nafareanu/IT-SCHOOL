#se cere o suma din tastatura la care se va afisa TVA ul si totalul cu TVA

suma = float(input("Introdu suma: "))
vat = suma * 0.19
total = suma * 1.19
print("")
print("TVA-ul pt aceasta suma este: " + str(vat))
print("Suma cu TVA inclus este: " + str(total))
print("")
