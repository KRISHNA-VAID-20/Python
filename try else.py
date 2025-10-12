try:
    n= int(input("Enter number :"))
    print(1/n)
except ZeroDivisionError:
    print("Divivding by zero !")
except ValueError:
    print("Divide by numbers only !")
except Exception:
    print("Something went wrong !")
finally:
    print("Done :)")