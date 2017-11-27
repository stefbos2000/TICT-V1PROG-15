set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {1, 2}
print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)

print(set3.issubset(set1))
print(set3 < set1)

print(set1.issubset(set3))
print(set3 > set1)