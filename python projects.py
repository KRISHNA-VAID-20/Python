#Calculator by kv

# running = True
# while running:

#     try:


#         a= int(input("Enter a number : "))
#         b= int(input("Enter a number : "))
#         c= input("Enter operand (+,-,*,/) :")
#         if c =="+":
#             print(a+b)
#         elif c=="-":
#             print(a-b)
#         elif c=="*":
#             print(a*b)
#         elif c=="/":
#             print(a/b)
#         else:
#             print("Invalid input !")
#             print("Select operand (+,-,*,/) :")
#         if not input("Try again ? (y/n) :").upper()=="Y":
#                 running = False
#                 print("shukriya pra g :)")
        
#     except ValueError:
#         print("Only numbers are allowed !")    


#Python Number guessing Game ------
# import time
# import random
# lowest_num = 1
# Highest_num = 100
# answer=random.randint(lowest_num,Highest_num)
# guesses= 0
# print("******************************************************")
# print("Let's Start Number guessing Game :) ")
# print("******************************************************")
# print(f"Select a number between {lowest_num} and {Highest_num} ")
# print("******************************************************")
# print("Game is starting in :")
# for i in range(3,0,-1):
#     time.sleep(2)
#     print(i)
# isrunning= True
# n= input("Enter your name  :" )
# while isrunning:
#     guess= input("Enter your guess :")
#     if guess.isdigit():
#         guess=int(guess)
#         guesses+=1
#         if guess < lowest_num or guess > Highest_num:
#             print("This number is out of given range ")
#         elif guess < answer:
#             print("Too low ! ")
#         elif guess > answer:
#             print("Too  high !")
#         else:
#             print("------------------------")
#             print("Correct Answer :)")
#             print("------------------------")
#             print(f"The answer was : {answer}")
#             print(f"No. of guesses you took : {guesses}")
#             if not input("Wanna play again ? (y/n) : ").upper() == "Y":
#                 isrunning= False
#             print(f"Thnx for playing {n} :)")
#     else:
#         print("Invalid Input ") 
#         print(f"Select a number between {lowest_num} and {Highest_num}  ")     

#-----------------------------------------------------------------------------------------------------------

#2- Rock paper and scissors Game ---------
# import random
# import time
# options= ("rock","paper","scissors")
# n= input("Enter your good name :) - ")
# print("Game is starting in :")

# for i in range(3,0,-1):
#     print(i)
#     time.sleep(0.1)
# running= True

# while running:
#     player= None
#     computer= random.choice(options)
#     while player not in options:
#         player = (input("Enter your choice (rock,paper,scissors) : ").lower())
#     print(f'Your choice : {player}')
#     print(f'computer choice : {computer}')

#     if player==computer:
#         print("It's a tie !")
#     elif player == "rock" and computer == "scissors":
#         print("You won !")
#     elif player == "paper" and computer == "rock":
#         print("You won !")
#     elif player == "scissors" and computer == "paper":
#         print("You won !")
#     else:
#         print("You lose !")

#     if not (input ("Wanna play again ? (y/n) : ").lower()) == "y":
#         running = False
    
# print(f"Thanks for playing {n}:)")                  

#-----------------------------------------------------------------------------------------------------

#3- Python banking program 

# def show_balance():
#     print(f"Your balance is Rs {balance:.2f} ")
# def deposit():
#     amount= float(input("Enter an amount to deposit : "))
#     if amount < 0:
#         print("Deposit can't be 0 !")
#         return 0
#     else:
#         return amount    
# def withdraw():
#     amount= float(input("Enter an amount to be withdrawn :"))
#     if amount > balance:
#         print("Insufficient Funds !")
#         return 0 
#     elif amount <= 0 :
#         print("Amount can't be 0 !")
#         return 0    
#     else:
#         return amount 
          
# balance=0
# running= True

# while running:
#     print("-----------------")
#     print("Banking Program")
#     print("-----------------")
#     print("1. Balance ")
#     print("2. Deposit ")
#     print("3. Withdraw ")
#     print("4. Exit  ")
#     print("-----------------")
#     choice = input("Enter your choice (1-4) : ")
#     print("-----------------")
#     if choice == "1":
#         show_balance()
#     elif choice == "2":
#         balance += deposit()
#     elif choice == "3":
#         balance-=withdraw()
#     elif choice == "4":
#         running = False
#         print("-----------------")
#         print("Thank you ! Have a good day :) ")
#         print("-----------------")  
#     else:  
#         print("That is not a valid choice !")

#--------------------------------------------------------------------------------------------

# Slot Machine :

# def spin_row():
#     pass
# def print_row():
#     pass
# def get_payout():
#     pass

# def main():
#     balance = 100
#     print("*************************")
#     print("Welcome to slot machine :) ")
#     print("*************************")

#     symbols= "🍒🥭🔔⭐🍉"
#     print("*************************")

#     while balance>0:
#         print(f"Current balance :Rs {balance}")
        
#         bet = input("Enter your amount to bet : ")

#         if not bet.isdigit():
#             print("Plz enter a valid Number !")
#             continue
#         bet = int(bet)    

#         if bet > balance :
#             print("Insufficient balance :(")
#             continue
#         if bet <=0 :
#             print("Bet can't be 0 ")
#             continue


#         balance-=bet



 
 
 
 
#if  __name__=="__main__":
 #   main()
    


# emails=["Imkv@gmail.com,Kv@gmail.com,krishna@yahoo.com","Karan@yahoo.com"]
# # email_users=[]
# # for email in emails:
# #     if email.endswith("@gmail.com"):
# #         email_users.append(email)
# #         print(email_users)
# email=[]
# email_users=[email for email in emails if email.endswith("gmail.com")]
