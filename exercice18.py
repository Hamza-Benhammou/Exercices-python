# Tri à partir du premier argument

tuple_L = [("Pomme", 15), ("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Peche", 2)]
result = sorted(tuple_L)
print(result)

# Tri à partir du deuxième argument

tuple_L = [("Pomme", 15), ("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Peche", 2)]
result = sorted(tuple_L, key=lambda x: x[1])
print(result)

