#2 Task
immutable_var = tuple_ = (1, [22,33], True, "Nizami")
print(immutable_var)

#3 Task
#tuple_[0] = 5
#print(tuple_) # ОШИБКА - 'tuple' object does not support item assignment
#Кортеж относится к неизменяемым типам данных, поэтому нельзя изменять данные  внем

#4
mutable_lst = [1,2, "N", "0"]
mutable_lst[0] = 7
mutable_lst[2] = "A"
print(mutable_lst)