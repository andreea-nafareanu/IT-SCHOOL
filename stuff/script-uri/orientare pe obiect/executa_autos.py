from autos import Car
from autos import Person
from autos import GasStation

gas1 = autos.GasStation(1234)

gas1.set_price(6.55, 1234)
ford = Car()
print(f"Aveti de plata: {gas1.fill(ford, 10)}")

#ford.start_engine()
#ford.drive(50)

p1 = Person()
p2 = Person()

print(ford.get_consumption())
ford.add_person(p1)
ford.add_person(p2)
print(ford.get_consumption())