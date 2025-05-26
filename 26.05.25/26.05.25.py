# class Person:
#     default_name = "Undefined"

#     def __unit__(self,name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name

# person1 = Person("Имя")
# person2 = Person("")
# print(person1.name)
# print(person.name)

# class Person:
#     __type = "Person"

#     @staticmethod
#     def print():
#         print(Person.__type)
#         person1 = Person()
#         person1.print()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self. age = age
#     def display(self):
#         print(f"Name {self.name}")

#     def __str__(self):
#         return f"Name": {self.Name}, {self.age}

# person1 = Person("Имя"20)
# print(person1)

# class Counter:
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other)
#         return Counter(self.value + other.value)

# counter1 =  Counter(50)
# counter2 =  Counter(10)
# counter3 = counter1 + counter2
# print(counter3.value)

# class Vector:
#     def __init__(self,a,b)
#         self.a = a
#         self.b = b
#     def __add__(self,value):
#         return Vector(self.a + value.a,self.b + value.b)
#     def __sub__(self,value):
#         return Vector(self.a + value.a,self.b + value.b)
#     vect1 = Vector(10,300)
#     vect2 = Vector(200,100)
#     фотка с дописанием в телефоне

# import abc
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area (self): pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self): return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self): return self.radius * self.radius * 3.14

# def displayArea(shape):
#     print("Area:", shape.area())

# rect = Rectangle(150, 40)
# circ = Circle(90)
# displayArea(rect)
# displayArea(circ)



# Квадрат
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def area(self):
        return self.a1 * self.a2

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = Square(40, 40)
displayArea(rect)
import abc


# ромб
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class rhombus(Shape):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return self.d1 * self.d2 /2

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = rhombus(40, 40)
displayArea(rect)
import abc


# Трапеция
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class trapezoid(Shape):
    def __init__(self, a1, a2, h):
        self.a1 = a1
        self.a2 = a2
        self.h = h

    def area(self):
        return self.a1 * self.a2 * self.h / 2

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = trapezoid(40, 40, 30)
displayArea(rect)

# Пятиугольник
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class pentagon(Shape):
    def __init__(self, a1, a2, a3, a4, a5 ):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5

    def area(self):
        return self.a1 * self.a2 * self.a3 * self.a4 * self.a5

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = pentagon(40, 40, 40, 40, 40)
displayArea(rect)
import abc

# Треугольник
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class triangle(Shape):
    def __init__(self, a1, a2, h):
        self.a1 = a1
        self.a2 = a2
        self.h = h

    def area(self):
        return self.a1 * self.a2 * self.h / 2

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = triangle(20, 20, 30)
displayArea(rect)

# Сфера
import abc
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class sphere(Shape):
    def __init__(self, r):
        self.r = r
       
    def area(self):
        return self.r * self.r * 4 * 3,14

def displayArea(shape):
    print(f"The area is: {shape.area()}")

rect = sphere(40)
displayArea(rect)
import abc