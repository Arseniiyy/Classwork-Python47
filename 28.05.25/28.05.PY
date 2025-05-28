# LIST(список)
number = ["name",85,True,False]
# print(number[1])
# print(number[-1])

# one,two,three,four = number
# print(two)

# for value in number:
#     print(value)

# i = 0
# while i <len(number):
#     print(number[i])
#     i+=1
# print(i)

# names1 = ["Regina","Artem","Ilya"]
# names2 = ["Robert 2","Anton","Egor"]
# if names1 = names2:
#     print("Списки одинаковые")
# else:
#     print("Списки имеют разные значения")

names2 = ["Robert 2","Anton","Egor","Regina","Artem","Ilya"]
# firstPart = names2[start:end:step]
# print(firstPart)

# Методы и функции по работе со списками
# Для управления элементами списки имеют целый ряд методов. Некоторые из них:

# append(item): добавляет элемент item в конец списка

# insert(index, item): добавляет элемент item в список по индексу index

# extend(items): добавляет набор элементов items в конец списка

# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

# clear(): удаление всех элементов из списка

# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

# pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

# count(item): возвращает количество вхождений элемента item в список

# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

# reverse(): расставляет все элементы в списке в обратном порядке

# copy(): копирует список

# Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

# len(list): возвращает длину списка

# sorted(list, [key]): возвращает отсортированный список

# min(list): возвращает наименьший элемент списка

# max(list): возвращает наибольший элемент списка



# numbers = {-12,-2,4,7,-10}
# def filt(numbers):
#     return numbers > 1 

# result = filter(lambda n: n > 1,numbers)

# for n in result:print(n,end="")



# class Person:
#     def __init__(self,name,age)
#         self.name = name
#         self.age = age

# people = {Person("Regina",20),Person("Regina1",21),Person("Regina2",22)}

# view = filter


# Задача 1
# name = ["Egor", "Marta", "Robert", "Vlad"]
# name.append("Robert2")
# name.append("Robert3")
# name.pop()
# print(name)

# Задача 2
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]
print("mat:",mat)

print("mat[0]:",mat[0])
print("mat[1]:",mat[1])
print("mat[2]:",mat[2])

print("mat[0][0]: ", mat[0][0])
print("mat[0][1]: ", mat[0][1])
print("mat[0][2]: ", mat[0][2])
print("mat[1][0]: ", mat[1][0])
print("mat[1][1]: ", mat[1][1])
print("mat[1][2]: ", mat[1][2])
print("mat[2][0]: ", mat[2][0])
print("mat[2][1]: ", mat[2][1])
print("mat[2][2]: ", mat[2][2])



