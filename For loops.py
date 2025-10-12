
#table
n= int(input("Enter Your NUmber :"))
i=1
while i<=10:
    print(n*i)
    i+=1
n= int (input("Enter your number :"))
fact=1
for i in range (1,n+1):
    fact= fact *i
print(f"Factorial is : {fact}")    
import time
Varun = 0 
Krishna = 0
for i in range (1,11):
    print("Game will start in :",i)
    time.sleep(1)
time.sleep (1)
print("Game started :)")
def fun(age,score):
    if age <= 18:
        print(f"Hello Varun :)")
    else:
        print(f"Hello Krishna :)")
fun(19,90)
print(fun)       
     
# [expression for in iterable if condition]:

list= [x *3 for x in range (1,11)]
print(list)     



