# oops :) -
#-----------------------------------------------
# 1
#---------------------------------------------------
# class student:
#     def __init__(self,Name,Class,Rollno,year):
#         self.Name= Name
#         self.Class= Class
#         self.Rollno = Rollno
#         self.year = year
# Student1= student("Krishna Vaid","L",61,1)
# Student2= student("Karan Sharma","L",62,1)
# print(Student2.Name) 
# print(Student2.Class)  
# print(Student2.Rollno)  
# print(Student2.year)  
#-----------------------------------------------------
# 2 
#-----------------------------------------------------
# class cars:
#     def __init__(self,Model,year,color,is_available):
#         self.Model= Model
#         self.year= year
#         self.color= color
#         self.is_available= is_available
# car_1= cars("BMW",2025,"black",True)
# car_2=cars("Alto",2020,"White",False)
# print(f"Model of car is {car_2.Model}")        
# print(f"Year of Released {car_2.year}")
# print(f"Color is  {car_2.color}")
# print(f"Available ? {car_2.is_available}")
#-----------------------------------------------
# 3- Class variables :
#-----------------------------------------------------l

# class student:
#     class_year = 2028
#     num_of_students= 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         student.num_of_students += 1

# student1= student("Krishna Vaid ", 18)
# student2= student("Karan Sharma ",20)

# print(f"Number of students graduating in {student.class_year} are {student.num_of_students}")
# print(f"Name : {student1.name}, Age : {student1.age}")
# print(f"Name : {student2.name}, Age : {student2.age}")

#-----------------------------------------------
#4 - Inheritence (parent class)
#----------------------------------------------------

# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating ")
#     def sleep(self):
#         print(f"{self.name} is asleep  ")

# class Dog(Animal):
#     def speak(self):
#         print("Bouu")
# class cat(Animal):
#     def speak(self):
#         print("Meaow")

# dog= Dog("Sandy")
# Cat= cat("Billi")

# print(Cat.name)
# Cat.eat()
# Cat.sleep()
# Cat.speak()
# print()
# print(dog.name)
# dog.eat()
# dog.sleep()
# dog.speak()
#-----------------------------------------------
# 5 
#-----------------------------------------------
# class Father:
#     def __init__(self,name):
#         self.name = name
#     def hair(self):
#         print(f"{self.name} has good hair !")
#     def height(self):
#         print(f"{self.name} is 6 ft tall !")

# class son1(Father):
#     pass
# class son2(Father):
#     pass

# Kv= son1("Krishna vaid ")
# vv= son2("Varun vaid ")

# print(Kv.name)
# print(vv.name)
# Kv.hair()
# Kv.height()
# vv.hair()
# vv.height()
#-----------------------------------------------
#6
#-----------------------------------------------
# class Father:
#     def __init__(self,name):
#         self.name = name
#     def hair(self):
#         print(f"{self.name} has good hair !")
    

# class son1(Father):
#     def height(self):
#         print(f"{self.name} is 6 ft tall ! ")

# class son2(Father):
#     def height(self):
#         print(f"{self.name} is 5.8 ft tall !")

    

# kv= son1("Krishna vaid ")
# vv= son2("Varun vaid ")

# print(kv.name)
# print(vv.name)
# kv.hair()
# kv.height()
# vv.hair()
# vv.height()

#-----------------------------------------------------
# 7 - Multiple inheritance and multilevel inheritance 
#-----------------------------------------------------
# class human:
#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating ")

#     def sleep(self):
#         print(f"{self.name} is sleeping ")
    
# class male(human):
#     def love(self):
#         print(f"{self.name} loves Ambica sharma ")
# class female(human):
#     def love(self):
#         print(f"{self.name} do not love Krishna vaid ")

# krishna = male("Krishna vaid ")
# ambica = female("Ambica Sharma ")
# print(krishna.name)
# krishna.love()
# print(ambica.name)
# ambica.love()

#-------------------------------------------------------------
# Multilevel inheritance 
#-------------------------------------------------------------
# class monkey:
#     def __init__(self,name):
#         self.name= name
#     def walk(self):
#         print(f"{self.name} can walk ")

# class human(monkey):
#     def eat(self):
#         print(f"{self.name} is eating ")

#     def sleep(self):
#         print(f"{self.name} is sleeping ")
    
# class male(human):
#     pass
# class female(human):
#     pass

# krishna = male("Krishna vaid ")
# ambica = female("Ambica Sharma ")
# h= human("All humans ")
# krishna.walk()
# ambica.walk()
# h.walk()
#-----------------------------------------------
# super() method
#-----------------------------------------------

# class shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
#     def describe(self):
#         print(f"It is {self.color} and {"filled" if self.is_filled else "not filled "}")

# class circle(shape):
#     def __init__(self, color, is_filled,radius):
#         super().__init__( color, is_filled)
#         self.radius = radius
#     def describe(self):
#         super().describe()
#         print("I am Circle")    
# class square(shape):
#     def __init__(self, color, is_filled,side):
#         super().__init__(color, is_filled)
#         self.side= side
        

# class triangle(shape):
#     def __init__(self, color, is_filled,width,height):
#         super().__init__(color, is_filled)
#         self.width= width
#         self.height= height

# Circle=circle(color="red",is_filled=True,radius =5)
# Square=square("Black",False,6)
# Triangle= triangle("Yellow",True,7,8) 
# print(f"{Circle.radius}cm")                
# print(Square.is_filled)
# print(Triangle.color)
# print(Triangle.height)
# Circle.describe()
# Square.describe()
# Triangle.describe()

#-----------------------------------------------------------
# Abstraction 
#-----------------------------------------------------------
# from abc import ABC,abstractmethod


# class vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
# class car(vehicle):
#     def go(self):
#         print("Car is going !")
#     def stop(self):
#         print("Car is stopped ")
    
# class cycle(vehicle):
#     def go(self):
#         print("Cycle has gone !")


# Car= car()
# Car.go()
# Car.stop()
# Cycle=cycle()
# Cycle.go()

#-----------------------------------------------------------
# Note : (All atributes present in parent class should be present in child class if abstraction is used)
# -----------------------------------------------------------
 


#-----------------------------------------------------------
# Polymorphism 
#-----------------------------------------------------------

# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius= radius
#     def area(self):
#         return 3.14 * self.radius*self.radius  
# class square(shape):
#     def __init__(self,side):
#         self.side = side
#     def area(self):
#         return self.side*self.side
# class triangle(shape):
#     def __init__(self,base,height):
#         self.base= base
#         self.height = height
#     def area(self):
#         return self.base* self.height * 0.5
# class pizza(circle):
#     def __init__(self,flavor,radius):
#         super().__init__(radius)
#         self.flavor= flavor
        
        
# shapes= [circle(2),square(5),triangle(6,7),pizza("Cheese",8)]       

# for shape in shapes:
#     print(f"{shape.area()} cm²")
#-----------------------
# Note : for ² use alt + 0178
#-----------------------
#-------------------------------------------------------------
# 2 - Duck Typing(polymorphism type 2)
# ------------------------------------------------------------

# class human:
#     alive = True
# class male(human):
#     def harmone(self):
#         print("Testosterone 👨")        
# class female(human):
#     def harmone(self):
#         print("Estrogen 👧")
# class car:
#     alive= False
#     def harmone(self):
#         print("Honk")

# humans= [male(),female(),car()]

# for human in humans:
#     human.harmone()
#     print(human.alive)

#---------------------------------------------------------------
# Static Methods 
#---------------------------------------------------------------

# class employee:
#     def __init__(self,name,position):
#         self.name = name
#         self.position= position

#     def get_info(self):
#         return(f"{self.name} = {self.position}")
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions= ["Manager","cashier","senior","cook"]
#         return position in valid_positions

# print(employee.is_valid_position("cashier"))
# employee1= employee("Krishna","Manager")
# employee2= employee("Karan","senior")
# print(employee1.get_info())
# print(employee2.get_info())

#------------------------------------------------------------
# Class methods 
#------------------------------------------------------------

# class student:
#     count = 0
#     total_gpa=0

#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa= gpa
#         student.count+=1
#         student.total_gpa+=gpa
#     def get_info(self):
#         return (f"{self.name} = {self.gpa}")
#     @classmethod
#     def get_count(cls):
#         return(f"Total # of students :{cls.count}")
#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return (f"{cls.total_gpa / cls.count}")

# student1= student("Krishna ",4.0)
# student2= student("Karan",4.1)

# print(student.get_count())
# print(f"Average gpa :{student.get_avg_gpa()}")

# print(student1.get_info())
# print(student2.get_info())
#-----------------------------------------------------
#example
#-----------------------------------------------------

# class animal:
#     count=0
#     total_species=0

#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#         animal.count+=1
#         animal.total_species+=species

#     def get_info(self):
#         return(f"{self.name} = {self.species}")

#     @classmethod
#     def get_count(cls):
#         return(f"Total animals = {cls.count}")
#     @classmethod
#     def get_total_species(cls):
#         if cls.count==0:
#             return 0
#         else:
#             return(f"Total species = {cls.total_species}")


# animal1=animal("Lion",4000)
# animal2=animal("Leopard",100)
# print(animal1.get_info())
# print(animal2.get_info())
# print(animal.get_count())
# print(animal.get_total_species())
#---------------------------------------------
# file handling 
#---------------------------------------------
# import os

# file_path= "C:/Users/krishna vaid/OneDrive/Desktop/test"

# if os.path.exists(file_path):
#     print(f"That location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("That is a file ")
#     elif os.path.isdir(file_path):
#         print("That is a directory")    
 
# else :
#     print(f"That location {file_path} doesn't exists")

# import os 

# txt_data= "Im krishna "
# txt_data2="Im varun"
# file_path= "C:/Users/krishna vaid/OneDrive/Desktop/output.txt"

# with open(file_path,"a") as file:
#     file.write("\n"+txt_data2)
#     print("File created ")
print ("hello")



























