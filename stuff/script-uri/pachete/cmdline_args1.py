import sys
if sys.version_info.major < 3:
    print(f"Versiunea {sys.version_info.major} nu este suportata!")

print("Hello")

#sys.exit(1) #ne opreste executia

try:
    print(sys.argv[1] * int(sys.argv[2]))
except IndexError:
    print("Argumentul nu exista")
    sys.exit(1)
except ValueError:
    print("Tip argument nu exista")
    sys.exit(1)
print("Bye!")

#user_input = input("Introdu string: ")

#print(user_input[::-1])
