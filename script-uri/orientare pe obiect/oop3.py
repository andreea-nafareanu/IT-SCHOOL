class Car:
    """Representation of a virtual car."""
    def __init__(self): #constructor
        self.__cmc = 0
        self.__doors = 4 # prin dublu undersquare s a facut atributul privat (nu mai e public si nu mai poate fi iterat mai jos)
        self.__tank_capacity = 45
        self.__gas_in_tank = 20
        self.__passengers = []
        self.__engine_running = False

    def get_gas_percentage(self):
        """Get current gas level in tank"""
        return self.__gas_in_tank / self.__tank_capacity * 100
        
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def drive(self):
        pass

    def refill(self):
        pass

    def get_doors(self):
        return self.__doors 

vw = Car ()
ford = Car ()

#print (f"CMC VW: {vw.cmc}")
#print (f"CMC FOrd: {ford.cmc}")

#vw.cmc = 3000
#print (f"CMC VW: {vw.cmc}")
#print (f"CMC FOrd: {ford.cmc}")
print (vw.get_doors())
print(f"Combustibil ramas {vw.get_gas_percentage():2f}%")


class Person:
    def __init__(self):
        self.__weight = 0
        self.__height = 187

    def get_height_cm(self):
        return self.__height 
    
    def get_height_m(self):
        return self.__height / 100
    
vlad = Person()
maria = Person()  

print(f"Inaltimea Mariei in cm este: {maria.get_height_cm()}")
print(f"Inaltimea Mariei in m este: {maria.get_height_m()}")


