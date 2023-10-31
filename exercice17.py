L1 = [9, 5, 7, 14, 3, 2, "a", "p", "bonjour", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]
set_l1 = set(L1)
set_l2 = set(L2)
L3 = list(set_l1 & set_l2)
print(L3)



