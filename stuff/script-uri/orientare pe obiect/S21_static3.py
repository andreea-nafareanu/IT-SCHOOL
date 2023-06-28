class Factura:

    nr_crt = 1 

    def __init__(self, valoare_totala) -> None:
        self.__numar = Factura.nr_crt
        self.valoarea_totala = valoare_totala
        Factura.nr_crt +=1

    @property
    def numar(self):
        return self.__numar
    
f1 = Factura(100)
f2 = Factura(200)
print(f2.numar)