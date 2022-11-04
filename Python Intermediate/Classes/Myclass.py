########### ----------Following is simple class declaration and access

class MyClass:
    x = 5


p1 = MyClass()  #####---Accessed using object
print(p1.x)


###---- Everytime object of class is called init method is called
# _ It is always good for assigning values to the properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person("John", 36)
#
# print(p1)
# ------Above code  can't print the values
# so we need a string object returned it is similar to toString() in java


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


####_----acesssing data using the methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

################----------Some operation om classes-------------############

p1.age = 40
del p1.age

del p1


#####-The pass statement can allow to even have it empty

class Person:
    pass
