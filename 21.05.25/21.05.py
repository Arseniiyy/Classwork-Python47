# инкапсуляция
class Person:
    def __init__(self, name, age):
        self.__name = name;
        self.__age = age;

    def get_age(self):
        return self.__age
    def setAge(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимое значение")

    def print(self):
        print(f"{self.__name},{self.__age}")

object = Person("Имя", 10)
object.print()
object.setAge(19)
object.print()
# object.__age = 18
# object.__name = "Регина"
# object.print()

# инкапсуляция
class Person:
    def __init__(self, name, age):
        self.__name = name;
        self.__age = age;
    property
    def get_age(self):
        return self.__age
    @age.setter 
    def setAge(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимое значение")

    def print(self):
        print(f"{self.__name},{self.__age}")

object = Person("Имя", 10)
object.print()
object.setAge(19)
object.print()
# object.__age = 18
# object.__name = "Регина"
# object.print()



