class AirplaneTicket:
    pass
#instantie
tk1 = AirplaneTicket ()
tk2 = AirplaneTicket ()

print(tk1)
print(tk2)
print (type(tk1))
print (type(tk2))
print (type(AirplaneTicket))

print (isinstance(tk1, AirplaneTicket))
print (isinstance(tk2, AirplaneTicket))
print (isinstance(AirplaneTicket, AirplaneTicket))

del tk1 #stergere obiect



