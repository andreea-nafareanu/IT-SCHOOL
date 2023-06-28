import_numbers = "today we had 280 clients."
user_name = "andreea.nafareanu"
job = "PROGRAMMER"

#prima litera mare din string
print(import_numbers.capitalize())

#face toate literele mici
print(job.lower())

#face toate literele mari
print(user_name.upper())

#face fiecare litera de la inceputul fiecarui cuvant litera mare
print(user_name.title())

#inlocuieste toate aparitiile stringului cu noua valoare
new_numbers = import_numbers.replace("clients", "customers")
print(new_numbers)

#exercitiu
extra_numbers = import_numbers.replace("280", "300")
print(extra_numbers.title())
for i in extra_numbers:
    print (i)