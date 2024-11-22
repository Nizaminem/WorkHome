grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) #превратили в список множество students
students.sort() #првоели сортировку списка students
# d = dict(((students[0], round(sum(grades[0])/len(grades[0]),2)),
# (students[1], round(sum(grades[1])/len(grades[1]),2)),
# (students[2], round(sum(grades[2])/len(grades[2]),2)),
# (students[3], round(sum(grades[3])/len(grades[3]),2)),
# (students[4], round(sum(grades[4])/len(grades[4]),2))))
# # dict - функция создания неупорядоченных коллекций с доступом по ключу
# # round - позволяет убрать значения после запятой на заданное количество (2)
# print(d)

# второй вариант с циклом
print(students)
d = {}
for i in range(5): #0,1,2,3,4 (до 5!)
    d[students[i]] = round(sum(grades[i]) / len(grades[i]), 2)
print(d)
