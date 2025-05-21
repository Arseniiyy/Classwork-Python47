
# class Samolet:
#     def __init__(self,name,model,age,power,hour):
#         self.__name = name
#         self.__model = model
#         self.age = age
#         self.power = power
#         self.hour = hour

#         def print(self):        
#             print(f"{self.__name},{self.__model},{self.__age},{self.__power},{self.__hour}")

#  airbus = Samolet("AirBus","A350","11","2 x 84 000 фунтов","3500h")
# print(airbus)   

# class Person:
#     def __init__(self, name):
#         self.__name = name;

#     @property
#     def name(self):
#         return self.__name

#     def display_info(self):
#         print(f"Имя {self.__name}")

# class Child(Person):
#     def __init__(self, name):
#         super().__init__(name)


class Father:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes

    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")


class Mother:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes

    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

class Child(Father, Mother):
    def __init__(self, surname, iq, colorEyes, height, colorHair):
        super().__init__(surname, iq, colorEyes)
        self.height = height
        self.colorHair = colorHair