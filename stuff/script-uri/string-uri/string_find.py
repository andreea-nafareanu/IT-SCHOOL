user_code = "44563-Test-0001"
print (user_code.find("-")) #afiseaza pozitia unde incepe stringul prima data
print (user_code.find("*")) #find afiseaza -1 daca stringul nu este gasit - IMPORTANT
print (user-code.find("-", 6)) #pot sa ii dau si pozitia de unde sa inceapa sa caute stringul

#exercitiu
user_code2 = "44563-anafareanu-0001"

prev = 0
while prev != -1:
    prev = user_code2.find("-", prev + 1)
    print(prev)
