text1 = '1 2 3 4 5 6 7 8'.split()
text2 = '4 6 8 10 12'.split()

set1 = set(text1)
set2 = set(text2)

#print(set1)
#print(set2)

set1_2 = list(map(int, set1.difference(set2)))
set1_2.sort()
print(set1_2)

