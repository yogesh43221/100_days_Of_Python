# #IF ELSE LOOP and Logical Operator
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))

# if height>100:
#     print("You can ride the rollercoaster")

# else:
#     print("You can't ride the rollercoaster.")

# Logical Operators
# < less than
# > grrater than
# >= greater than equal to
# =< less than equal to
# == equal to
# != no equal to
# = Assignement Operator

#Modulo Operator % = Remainder
# 10 % 5 = 2 -answer=0
# 10 % 3 = 3.3333333333 -3 with 1 remaining -answer=1

# # Check Odd or Even
# num = int(input("Enter any integer number"))
# if num%2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# #ROLLERCOASTER TICKET FAIR PROBLEM

# # MANUAL WAY SOLUTION

# print("Welcome to the rollercoaster")
# height = int(input("Enter you height in cm: "))

# if height >= 120:
#     print("You cam ride.")
#     age = int(input("Enter you age in years: "))
#     want_photos = bool(int(input("Enter 1 if you want photos else 0.")))
#     if age > 18:
#         if want_photos == True:
#             print("Your ticket fair is $12+$3=$15.")
#         else:
#             print("Your ticket fair is $12.")
#     elif 12 <= age <= 18:
#         if want_photos == True:
#             print("Your ticket fair is $7+$3=$10.")
#         else:
#             print("Your ticket fair is $7.")
#     else:
#         if want_photos == True:
#             print("Your ticket fair is $5+$3=$8.")
#         else:
#             print("Your ticket fair is $5.")
# else:
#     print("You can't ride.")


# # DYNAMIC WAY SOLUTION
    
# print("Welcome to the rollercoaster")
# height = int(input("Enter you height in cm: "))

# bill = 0

# if height >= 120:
#     print("You can ride.")
#     age = int(input("Enter your age in years: "))
    
#     if age > 18:
#         bill = 12
#         print(f"Your ticket fair is ${bill}.")
      
#     elif 12 <= age <= 18:
#         bill = 7
#         print(f"Your ticket fair is ${bill}.")
        
#     else:
#         bill = 5
#         print(f"Your ticket fair is ${bill}.")

#     want_photos = input("Do you want to have photo take? Type Yes for yes and No for no: ")
#     if want_photos == "Yes":
#         bill += 3
#     #     print(f"Your ticket fair with photo take is now ${bill}")
#     # elif want_photos == "No":
#     #     bill = bill
#     #     print(f"Your ticket fair is ${bill}")
#     # else:
#     #     print("Please enter valid input!")
#     print(f"Your final ticket fair is ${bill}")

# else:
#     print("You can't ride")

# ## BEST SOLUTION AS PER GEMINI

# def get_rollercoaster_ticket():
#     print("Welcome to the rollercoaster")
#     height = int(input("Enter your height in cm: "))
    
#     if height < 120:
#         print("Sorry, you can't ride.")
#         return

#     print("You can ride!")
#     age = int(input("Enter your age in years: "))
    
#     # 1. Use a Dictionary for pricing (Easy to update)
#     # Keys represent the maximum age for that price bracket
#     # Use float('inf') for the "adult" catch-all category
#     if age <= 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12

#     # 2. Simplified boolean check for extras
#     want_photos = input("Do you want photos? (Yes/No): ").lower()
#     if want_photos == "yes":
#         bill += 3
        
#     print(f"Your final ticket price is ${bill}.")

# get_rollercoaster_ticket()


# # PYTHN PIZZA CHALLENGE
# # My Solution
# print("Welcome to the Python Pizza Deliveries!")
# size = input("What sizepizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("Your types the wrong input! Please type correct input.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is {bill}.")


# # Best Soltion by Gemini

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ").upper()
# pepperoni = input("Do you want pepperoni? Y or N: ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# # 1. Data Store: All prices in one place
# prices = {
#     "S": 15,
#     "M": 20,
#     "L": 25
# }

# # 2. Logic: Start with the base price
# # .get() helps handle invalid inputs safely
# bill = prices.get(size, 25) 

# # 3. Add-ons: Simple and clean
# if pepperoni == "Y":
#     bill += 2 if size == "S" else 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")



# Logical Operators 
# and operator - A and B
# or operator - A or B
# not operator - not A

# a=10
# print(not a > 10) # it means not of false that is true

# Day 3: PROJECT : Treasure Island

print("Welcome to Treasure Island. Your mission is to find the treasure.")
death = 0
a = input("Where do you want to go? left or right: ").lower()
if a == "right":
    death += 1
    print("Game over! You fell in hole.")
elif a == "left":
    print("There is river infront of you.")
    b = input("What you want to do next? swim or wait").lower()
    if b == "swim":
        print("You entered into the ice cold river.")
        print('''You covered 50 km, but now you got hypothermia and you are converting into ice.
              But but.. someone saw you and got you out of ice.
              After getting back to normal temp. you woke up in an Cruise.
              You won and living luxurious life now! Cheers!''')
        death -= 1

    elif b == "wait":
        print("Boat came over and you seat in it. Boat took you to a island.")
        c = input("What door you choose? Red or Blue: ").lower()
        if c == "red":
            death += 1
            print("Game over! You were eaten by monster.")
        elif c == "blue":
            print("You are heading into a cave.")
        elif c == "yellow":
            print("You got captured by tribal's group.")
        else:
            print("Enter a valid input!")
    else:
        print("Enter valid input!")

else:
    print("Please enter valid input!")

print(f"Your total deaths are {death}")