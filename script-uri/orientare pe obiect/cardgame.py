from typing import Self, List 

s1 = "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"

CARD_SYMBOLS = ["♠", "♥", "♦", "♣"]
CARD_VALUE_MAP = {
    "2" : 2,
    "3" : 2,
    "4" : 2,
    "5" : 2,
    "6" : 2,
    "7" : 2,
    "8" : 2,
    "9" : 2,
    "10" : 10,
    "A" : 11,
    "J" : 12,
    "Q" : 13,
    "K" : 14
}

class Card:

    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number!")
        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol!")
        
        self.__symbol = symbol
        self.__number = number
    
    def __str__(self) -> str:
        #trebuie sa returneze string
        return f"<Card {self.__number}{self.__symbol}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def get_number(self) -> int:
        return CARD_VALUE_MAP[self.__number]
    
    def get_symbol (self) -> str:
        return self.__symbol
  
    def __eq__(self, other):
        # operator overloading
        # returneaza boolean
        #if self.number == other.number:
            #if self.symbol == other.symbol:
                #return True
        #return False
        return self.get_number() == other.get_number()
#__lt__<
#__le__<=
#__gt__>
#__ge__>=
    def __lt__ (self, other):
        return self.get_number() < self.get_number()
    def __le__ (self, other):
        return self.get_number() <= self.get_number()
    def __gt__ (self, other):
        return self.get_number() > self.get_number()
    def __ge__ (self, other):
        return self.get_number() >= self.get_number()
    def __add__(self, other):
        #returneaza acelasi tip , dar un obiect nou
        return self.get_number() + other.get_number()

class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """
    def __init__(self) -> None:
        self.__cards = []

    def get_size(self):
        return len(self.__cards)
    
    def __len__(self):
        #trebuie sa returneze int sau float
        return len(self.__cards)
    def get_cards(self, number) -> List[Card]:
        """Return n cars"""
    def shuffle(self):
        """Shuffles the desk"""

d1 = Deck()

c1 = Card("2", CARD_SYMBOLS[0])
c2 = Card("A", CARD_SYMBOLS[1])

print(c1==c2)
print(c1>c2)
print(c1>=c2)
print(c1<c2)
print(c1<=c2)
print(c1!=c2)
print(c1+c2)

print(f"Carti in pachet: {len(d1)}")
print(c1)
#print(f"Exception happened for object: {c1}")
#print(c1.__str__())

#c1_str = str(ca)
#c1_str = c1.__str__()

#atunci cand se creeaza un deck nou, sa fie initializat cu cele 52 de carti - se face in deck init cu 2 for-uri si faci append in lista
#si de implementat metoda get_cards si shuffles
#de implementat metodele magice pentru a sorta o lista de carti