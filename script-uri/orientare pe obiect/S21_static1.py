class UserAccount:
    def __init__(self, email) -> None:
        self.email = email
        self.__favorites_products = []

    @property 
    def favorites(self):
        return self.__favorites_products

    def add_fav(self, products):
        self.__favorites_products.append(products)

class Product:

    count = 0 #atribut de clasa / atribut static

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        Product.count +=1

    def add_to_favorites(self, user_account):
        user_account.add_fav(self)
    def __str__(self) -> str:
        return f"<Product name: {self.name}>"
    def __repr__(self) -> str:
        return self.__str__()
    
if __name__ == "__main__": #main guard

user1 = UserAccount("mihai@test.com")
prod1= Product("Masline", 34)
prod2= Product("Bulion", 5)
products = [Product("Ulei de masline", 45), Product("Ceapa", 3)]

products[-1].add_to_favorites(user1)
#print(user1.favorites)

#print(f"Valoarea atribut static prin nume clasa: {Product.count}")
#print(f"Valoarea atribut static prin obiect: {prod1.count}")
#Product.count = 45
#print(f"Valoarea atribut static prin nume clasa: {Product.count}")
#print(f"Valoarea atribut static prin obiect: {prod1.count}")
#print(f"Valoarea atribut static prin obiect: {prod2.count}")