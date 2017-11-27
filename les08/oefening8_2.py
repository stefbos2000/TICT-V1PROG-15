set1 = set()
set2 = set()
set3 = set()
for i in range(1,1000):
    if i % 3 == 0:
        set1.add(i)
for j in range(1, 1000):
    if j % 7 ==0:
        set2.add(j)
for f in range(1, 1000):
    if f % 7 == 0:
        set3.add(f)
print(set1&set2)
print(set1|set2)
print(set1-set2)
print(set3 - set1 - set2)