from autos import Car

class GasStation:
    def __init__(self, pin):
        self.__price = 0
        self.__busy = False
        self.__pin = pin

    def is_busy(self):
        return self.__busy
    
    def get_price(self):
        return self.__price
    
    def set_price(self,price,pin):
        if pin != self.__pin:
            raise ValueError("Wrong pin!")
        self.__price = price

    def fill(self, car: Car, litters):
        if self.__busy:
            raise ValueError ("Busy!")
        for x in range(1, litters + 1):
            try:
                car.refill(1)
            except ValueError:
                break
        return x * self.__price
        