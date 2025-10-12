#q5
tup = (1,4,9,25,36,49,64,81,100)
x= 25
idx = 0
while idx< len(tup):
    if (tup[idx]== x):
        print("Found at idx",idx)
    idx +=1


#q4
i= [1,4,9,25,36,49,64,81,100]
idx = 0
while idx< len(i):
    print(i[idx])
    idx +=1

# Making of calculator
operator= input("Enter your Operator (+ - * /) :")
n1= float(input("Enter the 1st number :"))
n2= float(input("Enter the 2nd number :"))

if operator == "+":
    Result = n1+n2
    print("Answer =",Result)
elif operator== "-":
    Result = n1-n2
    print("Answer =",Result)
elif operator== "*":
    Result = n1*n2
    print("Answer =",Result)
elif operator== "/":
    Result = n1/n2
    print("Answer =",round(Result,3))
else:
    print(f'Operator not valid')        

    #Weight converter
weight = float(input("Enter your weight :"))
unit= input("Enter the Unit (Kg or Lbs):")
if unit== "Kg":
    weight= weight*2.20
    print(f"Your Weight is {weight} Lbs")
elif unit== "Lbs":
    weight= weight/2.20
    print(f"Your Weight is {weight} Kgs")
else :
    print("weight not valid ")   

    #Temperature converter
temp = float(input("Enter the Temperature :"))
unit= input("Enter the unit ? (C/F) :") 
if unit== "C":
    temp=(temp*9/5)+32
    print(f"Your Temperature is {temp} F")    
elif unit== "F":
    temp== (32*temp-32)*5/9
    print(f"Your Temperature is {temp} C")
else :
    print(" Invalid Temperature Baby")    


    #Grade question
sub_1 = float(input("Enter your marks :"))
sub_2 = float(input("Enter your marks :"))
sub_3 = float(input("Enter your marks :"))
sub_4 = float(input("Enter your marks :"))
sub_5 = float(input("Enter your marks :"))
avg= (sub_1+sub_2+sub_3+sub_4+sub_5)/5
print(avg)
if avg>=90:
    print(" Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=60:
    print("Grade C")
elif avg>=40:
    print("Just Passed")
elif avg<=40:
    print("Failed")


    #ques 
pre = int(input("Enter your marks :"))
mains= int ( input("Enter your marks :"))
if pre >= 75:
    if mains >= 85:
        print(" Selected Bro !")
else:
    print("Not slected !")
print(" Better luck next time !!")        
 
 #Use of strings 
username = input("Enter your username :")
if len(username) >12:
    print("Username must less than 12 characters !")
elif not username.find(" ")==-1:
    print("username can't contain spaces !!")
elif not username.isalpha():
    print("Username can't contain digits !!")
else:
    print(f"Welcome {username} !")  

    # Compound interest calculator 

principle = 0
rate=0
time=0
while principle <=0:
    principle = float(input("Enter your principle amount :"))
    if principle <=0:
        print("Principle can't be negative or zero ")

while rate <=0:
    rate = float(input("Enter your interest rate:"))
    if rate <=0:
        print("Principle can't be negative or zero ")

while time <=0:
    time = float(input("Enter your time period :"))
    if time <=0:
        print(" Time  can't be negative or zero ")

Total = principle *pow((1+rate/100),time)
print(f"Your Balance is Rupee : {Total:.2f}")             


#Countdown timer
import time


kv_time = int(input("Enter your time :"))
for x in range (kv_time,0,-1):
    seconds= x %60
    minuetes= int(x/60)%60
    hours=int(x/3600)%60

    print(f"{hours:02}:{minuetes:02}:{seconds:02}")
    time.sleep(1)

print("Time over")


#Python program matrix
#from sympy import *
#A= Matrix([[2,-1,-3,-1],[1,2,3,-1],[1,0,1,1],[0,1,1,-1]])
#display("the given matrix is ",A)
#R=A.rank()
#print("the rank is:",R)

#nested loops 
for x in range (2):
    for y in range(1,10):
        print(y,end="")
    print()
#
rows = int(input("Enter rows:"))
columns = int(input("Enter columns :"))
symbol= input("Enter your symbol :")
for x in range (rows):
    for y in range (columns):
        print(symbol,end="")
    print()    


#Shopping cart program 

foods = []
prices= []
total= 0

while True:
    food= input("Enter your Food (press q to quit) :")
    if food.lower()=="q":
        break
    else:
        price= float(input(f"Enter the price of {food}:$"))
        foods.append(food)
        prices.append(price)

print("-----Your cart is here <)-----") 

for food in foods:
    print(food,end="-")
for price in prices:
    total+=price
print()
print(f"Your Total is {total}")


krishna = []
karan =[]
varun=[]
while True:
    marks = int(input("Enter your marks:"))
    if marks <=40:
        print(f"Failed{marks}")
    else:
        print(f"Passed with : {marks} marks")
        krishna.append(marks)
    print()
    print("Whats up krishna ")    
    break
for marks in krishna :
    print(f"Your total marks are {marks}")


#2D LISTS
fruits=["mango" , "papaya","guava"]
vege=["tomato","potato","brinjal"]
drinks=['cocacola','limca','fanta']

groceries=[fruits,vege,drinks]

for collection in groceries:
    for num in collection:
        print(num,end=" ")
    print()    


#num pad
num_pad=[(1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#")]
for row in num_pad:
    for num in row:
        print(num,end=" ")   
    print()


a= ["*","*","*"]
b= ["*","*","*"]
c= ["*","*","*"]

collections = [a,b,c]

for rows in collections:
    for k in rows:
        print(k,end=" ")
    print()    


#QUIZ GAME 
questions =("Who is Narendra modi ?:",
            "Population of India ?:",
            "City of temples ?:",
            "National Game of India ?:")

options = (("A. PM","B. CM" ,"C. HM","D. M"),
           ("A. 130 C","B. 140 C","C. 150 C","D. 160 C"),             
           ("A. Jammu","B. Jaipur","C. Rajasthan","D. Delhi"),
           ("A. Kabaddi","B. Cricket","C. Football","D. Hockey"),)

answers = ("A","B","C","D")
guesses= []

score = 0
question_num=0

for question in questions :
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
           score+=1
           print("Correct ")
    else:
        print("Incorrect ")  
    print(f" {answers[question_num]} is the correct answer")          

    question_num += 1



import random
def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
            
# Run the game
guess_the_number()



import time
rows = int(input("Enter no. of rows :"))
columns = int(input("Enter no. of columns :"))
symbol = input("Enter your symbol :")

for x in range (rows):
    for y in range (columns):
        print(symbol,end=" ")
    time.sleep(1)
    print()    

print("Good bye ")

# le bc star pattern 
import time
rows = int(input("Enter rows :"))
symbol = input("Enter symbol :")
for x in range (rows):
    for y in range (x+1):
        print(symbol,end="")
    time.sleep(1)    
    print()
time.sleep (2)
print()    
print("Dar Gya Kya :)")    