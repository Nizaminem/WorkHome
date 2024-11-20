#Первое упражнение
my_dict = {'Низами' : 1994, 'Максим' : 2000, 'Ваня' : 1990, 'Саня' : 2001}
print(my_dict)
print(my_dict['Низами'])
my_dict['Ден'] = 1992
print(my_dict['Ден'])
my_dict.update({'Толя': 2002,
               'Алекс': 2003})
del my_dict ['Максим']
print(my_dict.pop('Низами'))
print(my_dict)

# #2 упражнение
my_set = {1,2,2,1,'n','a','n', True, (8,8,0)}
print(my_set)
print(my_set.add(4))
print(my_set.add(7))
print(my_set)
print(my_set.discard(2))
print(my_set)