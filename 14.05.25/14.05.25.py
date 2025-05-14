
# def print_aboutme(name="Значение по умолчанию,age=18"):
#     print("Меня зовут",name,age)
# print_aboutme("age=16,name="Yan")

# def print_aboutme(name, age ,city):
#     print("Меня зовут", name, age , city)
# print_aboutme("Yan","Age",city="Sochi",city1="sochi11")


# def get_info():
#     return 'My Info'
# info - get_info()
# print(info)

# def get_info():
#     return 2+2
# info - get_info()
# print(info * 6)

# def speed_limt(speed):
#     if speed > 150:
#         print("Вы нарушаете")
#         return
#     else:
#         print("Все ок")
# speed_limt(300)

# def say_hello(): print("hello")
# def say_goodbye(): print("goodbte")

# def math_operation(a,b,operation):
#     result = operation(a,b)
#     print(f"result = {result}")

# def sum(a,b): return a + b
# def multiply(a,b): return a * b

# math_operation(555,111,sum)
# math_operation(12,2 multiply)


# def sum(a,b):  return a + b
# def subtract(a,b): return a - b
# def multiply(a,b): return a * b

#  def select(choice):
#  if choice ==1:
#     return sum
# elif choise == 2:
#     return subtract:
#     else:
#     return multiply
# #фотка в телефоне

# square = lambda n: n * n
# print(square(4))
# print(square(5))

# def kvadtrar(n):
#     return n * n
# print(kvadtrar(4))

# number1 = 60
# number2 = 12.5
# result = number1 + number2
# print(result)
# print(type(result))

# sercet = 123

# def test2():
#     sercet=1234
#     print("Секретная переменная", sercet)
# test2()
# print(sercet)

# def outher():
#     n = 5

#     def inner():
#          nonlocal n
#          n = 25
#         print(n)

#     inner()
# print(n)
# outher()

# def outher(): внешняя функция
#     n - 5

#     def  inner():
#         nonlocal n 
#         n += 1
#         print(n)
#     return inner

# plus = outher()
# # 
# plus()
# plus()
# plus()


def createCounter():
    count = 0
    def counter():
        nonlocal count
        count +=1 
        return count
    return counter

counter = createCounter()
print(counter()) 
print(counter())
print(counter())
print(counter()) 


