user_info = {
    "first_name": "andreea",
    "last_name": "nafareanu",
    "address": "Bucharest",
    "country": "ro"
}

USER_TEMPLATE = "Nume: {} Prenume: {} Country:{}"
print (USER_TEMPLATE.format(
    user_info["last_name"], user_info["first_name"], user_info["country"]))

#exercitiu
auto = {
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}

AUTO_TEMPLATE = "Detin o masina marca {2}, model {1} si are {0} usi." 
print ( AUTO_TEMPLATE.format(
    auto["usi"], auto["model"], auto["marca"]
))