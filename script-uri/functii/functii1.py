# functie cu side-effect 

def greet(name, header_len):
    """Say formatted greet message for user."""
    print("*"*header_len)
    print(f"Hello {name}!")
    print("*"*header_len)

greet ("Andreea", 30)

greet("Mihai", 30)

greet("Razvan", 30 )