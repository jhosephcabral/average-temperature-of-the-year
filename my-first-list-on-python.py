list = []

item = input("Build your list: ")
while item != "":
    list.append(item)
    item = input("Build your list: ")

for indice, elemento in enumerate(list):
    print("Item ", (indice+1), " - ", elemento)