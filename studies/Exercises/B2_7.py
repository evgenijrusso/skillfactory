# 7/9  B2.7. Идентичность

# L = ['a', 'b', 'c']
# print(id(L))
#   Идентичность осталась прежней
# L.append('d')
# print(id(L))

a = 5
b = 3+2

print('a:', id(a), 'b:', id(b))

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
print('shopping_center[-1]: ', id(shopping_center[-1]))
list_id_before = id(shopping_center[-1])

print('list_id_before', id(list_id_before))
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print('list_id_after', id(list_id_after))
print(id(list_id_after) == id(list_id_before))

# решение list_id_before == list_id_after


