
# def main(innerfunc):
#     def out():
#         print("***")
#         innerfunc()
#         print("***")
#     return out
# main
# def myFunc():
#     print("Моя функция а вокруг декоратор")

# myFunc()

# def check(input_function):
#     def output_func(*args):
#        name = args[0]
#        age = args[1]
#        if age < 0: age = 1
#        input_function (name,age)
#     return output_func
    
# @check
# def print_person(name,age):
#     print(f"{name} {age}")
# print("Name",50)

# print_person("Regina", -9)

class Person:
    def_init_(self,name,age):
    self.name - name
    self.age - age

    def namemetod(self)
        print(f"Мой первый метод на пайтоне.Я студент группы пайтон 47 {self.name},{self.age}")

robert = Person("Роберт" 70)
robert.namemetod()