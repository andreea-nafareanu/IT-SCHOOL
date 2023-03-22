# all - true daca toate valorile din lista evalueaza True
print (all([0, True]))

# any - true daca oricare element este True
print (any([False, False, True]))

# map - returneaza un map object NU O LISTA
init_lst = [4, 56, 7, 5, 45]
new_lst = map(lambda x: x**2, init_lst)

for i in new_lst:
    print(i)

# enumerate - returneaza un enumerate object -> un generator

print (enumerate(init_lst))
for i in enumerate(init_lst):
    print(f"Index: {i[0]} ... valoarea: {i[1]}")

#divmod - returneaza catul si restul impartirii

cat = 10 // 3
rest = 1 % 3

cat, rest = divmod(10,3)
print (f"Catul = {cat} si restul = cu {rest}")

#zip - ca un fermoar, din 2 valori, cupleaza si returneaza un cuplu
names = ["alex", "elena", "victor"]
ids = ["23323", "353535", "43553"]
zp = zip (names, ids)
#for i in zp:
    #print(i)

print(dict(zp))