# DEf  a laptop class that gives discounted price
class Laptop:
    def __init__(self,model_name,brand,price):
        self.model_name=model_name
        self.brand=brand
        self.price=price

    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price-off_pricel
lap1=Laptop("HPala","HP",20)
lap2=Laptop("Dellala","Ddell",12)
print(lap1.apply_discount(10))




# Polymorphism

class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"


a = A()
b = B()
print(b.special, b.var1, b.classvar1)




#poly method 1) Overloading

class A:
    # def Show(self):
    #     print("welcome")
    # def Show(self,first_name=''):
    #     print("Welcome",first_name)
    def Show(self,first_name='',last_name=''):
        print("Welcome",first_name,last_name)

obj=A()
obj.Show()
obj.Show("Saurabh")
obj.Show("Saurabh","Kuche")


# # # poly method 2) overriding

class A:
    def Disp(self):
        print("This is a parent class method")

class B(A):                                                    # Parent class ke function ko ham call kr skte hai
    def Disp(self):
        super().Disp()
        print("This is child class method")

obj=B()
obj.Disp()


# # Encapsulation
# class A:
#     _a=10                               # protected
#     __b=20                              # private
#     def Show(self):
#         print("a=",self._a)
#         print("b=",self.__b)

# obj=A()
# obj.Show()
# print("Outside of class",A._a)
# print("Outside of class ",A.__b)



# Class methods
@classmethod
def sau(cls,p1,p2):
    # code

 @property

 class employee:
    @property
    def name(self):
        e=employee()
        return self.ename

    @name.setter
    def name(self,value):
       self.ename=value

# Super method

# super__init__()     # it is used to access the methods of a super class in derived class

# Inheritance

class employee:
    # code

 class programmer(employee):
     # code



# Static method  -> Jiska relation class or instance se nhi hota

@staticmethod
def hello():
  print("Hello,static called")

print(hello())


# Class method as a constructor  -> class se sambandh

class Person:
    cont_instance=0
    def__init__(self,first_name,last_name,age):
Person.count_instance+=1
self.first_name=first_name
self.last_name=last_name
self.age=age

@classmethod
def from_string(cls,string):
   first,last,age=string.split(',')
   return cls(first,last,age)

p3=Person.from_string('Saurabh,kuche,26')
print(p3)

# Class methods

class Person:
   count_instance=0
   def __init__(self,first_name,last_name,age):

# Count the number of instance

class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p4=Person('mala','suri',34)
p2=Person('kala','maroi',2)
p1=Person('jkas','jghf',3)
print(Person.count_instance)        
