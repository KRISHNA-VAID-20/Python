class Student:
    total_std=0
    class_yr=2028
    def __init__(self,name,age):
        self.name= name
        self.age=age
        Student.total_std +=1
student1= Student("Krishna",18)
student2= Student("varun",15)
print(f"My class is graduating in {Student.class_yr} with {Student.total_std} students ")
print(student1.name)
print(student2.name)

class animal:
    def __init__(self,name):
        self.name= name
    def speak(self):
        print(f" {self.name} can speak")
    
    def sleep(self):
        print(f"{self.name} can sleep")

class Dog(animal):
        def speak(self):
             print("Woof")
    
class Cat(animal):
        def speak(self):
             print("meow")

dog = Dog("sandy")
cat = Cat("pussy")
print(dog.name)
dog.speak()
cat.speak()

# # Super function -

class shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
    
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius }cm^2")
        

class square(shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width
    
    def describe(self):
        super().describe()
        print(f"It is a square with an area of { self.width * self.width }cm^2")

class triangle(shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
    
    
    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height/2 }cm^2")

Circle=circle("red",True,10)
Square=square("blue",False,5)
Triangle=triangle("Yellow",True,7,10)

Circle.describe()
Square.describe()
Triangle.describe()


# polymorphism

# from abc import ABC,abstractmethod
class shape:
    # @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self,radius):
        self.radius = radius 
    
    def area(self):
        return 3.14*self.radius**2

class square(shape):
    def __init__(self,side):
        self.side = side 
    def area(self):
        return self.side**2

class pizza(circle):
    def __init__(self,topping,radius):
        self.topping=topping
        super().__init__(radius)

        
        

shapes= [circle(1),square(5),pizza("kv",10)]

for shape in shapes:
    print(f"{shape.area()}cm²")
class student:
    count= 0
    total_cgpa=0
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa= cgpa
        student.count+=1
        student.total_cgpa+=cgpa
    @classmethod
    def get_info(cls):
        return(f"Total no. of students :{cls.count}")
    @classmethod
    def _total_cgpa(cls):
        return(f"Total cgpa : {cls.total_cgpa}")

student1= student("Krishna",9)
student2= student("Karan",10)

print(student.get_info())        
print(student._total_cgpa()
numbers = [x for x in range(5)]  # [0, 1, 2, 3, 4]  
print(numbers)

square = lambda x:x*x
print(square(5))

def fun(*args,**kwargs):
    print(args)
    print(kwargs)
fun(1,2,3,4,"krishn

try:
    x=1/0
except ZeroDivisionError:
    print("Cant divide")

n=int(input ("number :"))
def is_prime(n):  
    if n < 2:  
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  


def reverse_string(s):  
    return s[::-1]  # Reverse using slicing  

print(reverse_string("krishna"))  # Output: olleh  

def is_prime(n):  
    if n < 2:  
        return False  # Numbers < 2 are not prime  
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility  
        if n % i == 0:  
            return False  # If divisible, not prime  
    return True  # If not divisible, it's prime  

print(is_prime(2))  # Output: True (Prime)  
print(is_prime(10)) # Output: False (Not Prime)  
