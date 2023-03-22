import argparse

print("hello")
argparser = argparse.ArgumentParser()

argparser.add_argument("symbol", type = str)
argparser.add_argument ("mul", type = int)

args = argparser.parse_args()

print(args.symbol * int(args.mul))

print("bye")

#de adaugat scriptului inca un argument care se va numi separator si in loc sa afiseze simbol langa simbol, sa afiseze simbol separator simbol separator etc
#de adaugat un argument optional "-v" = verbose = afiseaza mesajele hello si bye daca este setat la true (adica scriptul se apeleaza din cmd la final cu -v)
