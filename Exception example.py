name = input("what is your name?")

#lets write this in a simpler way
age2= input(f"How old are you {name}")
try:
   age=int(age2) #here there can be a problem
   print(f"{name}, you were born in {2024-age}")
   7 / 0
   bunny
except ValueError:
    print("print enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("you can not divide by 0!")
except:
    print("this is another type of error")
else: #this is for no exception
    print("Thank you for playing as excepted")
finally: #this will be executed no matter what at the very end
    print("Thanks for playing the game")