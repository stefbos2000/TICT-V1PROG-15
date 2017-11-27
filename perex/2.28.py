lst = [2, 5, 7, 8, 1, 7, 22, 44, 9]
mid = len(lst)/2 + 0.5
print(mid)
kek = lst.index(5)
print(kek)
lst.sort()
print(lst)
eerste = lst[0]
lst.remove(lst[0])
lst.append(eerste)
print(lst)