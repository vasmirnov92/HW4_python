# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


print('Введите количество элементов первого множества:')
firstSetQuantity = input()
firstSetQuantity = int(firstSetQuantity)
print('Вводите элементы первого множества через клавишу Enter: ')
firstSet = set()
for i in range(firstSetQuantity):
    n = input()
    n = int(n)
    firstSet.add(n)



# print(firstSet)
# print(type(firstSet))
# print(type(firstSetQuantity))

print('Введите количество элементов второго множества:')
secondSetQuantity = input()
secondSetQuantity = int(secondSetQuantity)
print('Вводите элементы второго множества через клавишу Enter: ')
secondSet = set()
for i in range(secondSetQuantity):
    n = input()
    n = int(n)
    secondSet.add(n)

# print(secondSet)
# print(type(secondSet))
# print(type(secondSetQuantity))


diffSet = firstSet.intersection(secondSet)
# print(diffSet)

diffList = list()
diffList = list(diffSet)
# print(diffList)
diffList.sort()
print(diffList)