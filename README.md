# python
# variable = a reusable container for storing a value
#                   a variable behaves as if it were the value it contains

# INTEGER
#age = 21
#players = 2
#quantity = 5

#print(f"You are {age} years old")
#print(f"There are {players} players online")
#print(f"You would like to buy {quantity} items")

# FLOAT
#gpa = 3.2
#distance = 2.5
#price = 10.99

#print(f"Your gpa is {gpa}")
#print(f"You ran {distance}Km")
#print(f"The price is ${price}")

# STRING
#name = "Bro"
#food = "pizza"
#email = "Bro123@gmail.com"

#print(f"Hello {name}")
#print(f"You like {food}")
#print(f"Your email is: {email}")

# BOOLEAN
#online = True
#for_sale = False
#running = False

#print(f"Are you online?: {online}")
#print(f"Is the item for sale?: {for_sale}")
#rint(f"Game running: {running}")

# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

#name = "Bro"
#age = 21
#gpa = 1.9
#student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student)) 

#age = float(age)
#print(age)

#gpa = int(gpa)
#print(gpa)

#student = str(student)
#print(student)

#ame = bool(name)
#print(name)

#user input
#name=input("what is your name?:")
#age=int(input("how old are you?:"))
#height=float(input("how tall are you?:"))

#print("hello"+name)
#print("you are"+str(age)+"years old")
#print("your"+str(height)+"cm tall")

#math functions
#import math
#i=3.14
#print(round(pi))=3
#print(math.ceil(pi))=4
#print(math.floor(pi))=3
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))


#slicing=create a substring by extracting elements from another stringindexing or slicing
#[start:stop:step]
#name="bro code"
#first_name=name[::3]
#last_name=name[2:3:]
#funky_name=name[::1]
#reversed_name=name[::-1]
#print(reversed_name)
#website1="http://google.com"
#website2="http://google.com"
#slice=slice(7,-4)
#print(website1[slice])
#print(website2[slice])

# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# —---------------------
#   EXAMPLE 1
# —---------------------
#age = int(input("Enter your age: "))

#if age >= 100:
#   print("You are too old to sign up")
#elif age >= 18:
#   print("You are now signed up")
#elif age < 0:
   #print("You haven't been born yet")
#else:
 #  print("You must be 18+ sign up")

# —---------------------
#   EXAMPLE 2
# —---------------------
#response = input("Do you want food (Y/N)?: ")

#if response == "Y":
 #  print("Have some food")
#else:
 #  print("No food for you!")

# —---------------------
#   EXAMPLE 3
# —---------------------
#name = input("Enter your name: ")

#if name == "":
 #  print("You did not enter your name!")
#else:
 #  print(f"Hello {name}")

# —---------------------
#   EXAMPLE 4
# —---------------------
#online = False

#if online :
 #  print("You are online")
#else:
#   print("You are offline")

#whileloop = perform some code WHILE some condition remains true

# ---------------- EXAMPLE 1 ----------------

#name = input("Enter your name: ")

#while name == "":
 #  print("You did not enter your name!")
  # name = input("Enter your name: ")

#print(f"Hello {name}")


# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:

#rows = int(input("Enter the # of rows: "))
#columns = int(input("Enter the # of columns: "))
#symbol = input("Enter a symbol to use: ")

#for x in range(rows):
 #  for y in range(columns):
  #     print(symbol, end="")
  # print()

# logical operators = used on conditional statements

#              and = checks two or more conditions are True
#               or = checks if at least one condition is True
#              not = True if condition is False, and vice versa

#temp = 20
#sunny = True

#if temp <= 0 or temp >= 30:
 #   print("The temperature is bad")
#else:
 #   print("The temperature is good")

#if not sunny:
 #   print("It is cloudy")
#else:
 #   print("It is sunny")


    # STRING METHODS
# -------------------------------
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name)
# index = name.find(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count(" ")
# phone_number = phone_number.replace("-", "")

# -------------------------------
#        EXERCISE
# -------------------------------
#username = input("Enter a username: ")

#if len(username) > 12:
 #  print("Your name can't be more than 12 characters")
#elif not username.find(" ") == -1:
 #  print("Your username can't contain spaces")
#elif not username.isalpha():
 #  print("Your username can't contain digits")
#else:
 #  print(f"Welcome {username}!")


#   loop = perform some code WHILE some condition remains true

# ---------------- EXAMPLE 1 ----------------

#name = input("Enter your name: ")

#while name == "":
 #  print("You did not enter your name!")
 #  name = input("Enter your name: ")

#print(f"Hello {name}")


#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#Here are a few different 2d collection combinations:

# 2D list of lists
#num_pad = [[1, 2, 3],
 #                     [4, 5, 6],
  #                    [7, 8, 9],
   #                   ["*", 0, "#"]]

# 2D list of tuples
#num_pad = [(1, 2, 3),
 #                     (4, 5, 6),
  #                    (7, 8, 9),
   #                   ("*", 0, "#")]

# 2D list of sets
#num_pad = [{1, 2, 3},
 #                     {4, 5, 6},
  #                    {7, 8, 9},
   #                   {"*", 0, "#"}]

# 2D tuple of lists
#num_pad = ([1, 2, 3],
 #                     [4, 5, 6],
  #                    [7, 8, 9],
   #                   ["*", 0, "#"])

# 2D tuple of tuples
#num_pad = ((1, 2, 3),
 #                     (4, 5, 6),
  #                    (7, 8, 9),
   #                   ("*", 0, "#"))

# 2D tuple of sets
#num_pad = ({1, 2, 3},
 #                     {4, 5, 6},
  #                    {7, 8, 9},
   #                   {"*", 0, "#"})

# 2D set of lists (NOT VALID)
#num_pad = {[1, 2, 3],
 #                     [4, 5, 6],
  #                    [7, 8, 9],
      #                ["*", 0, "#"]}

# 2D set of tuples
#num_pad = {(1, 2, 3),
 #                     (4, 5, 6),
  #                    (7, 8, 9),
  #                    ("*", 0, "#")}

# 2D set of sets (NOT VALID)
#num_pad = {{1, 2, 3},
 #                     {4, 5, 6},
  #                    {7, 8, 9},
   #                   {"*", 0, "#"}}

#for row in num_pad:
 #   for num in row:
  #      print(num, end=" ")
   # print()

# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

#capitals = {"USA": "Washington D.C.",
 #                   "India": "New Delhi",
  #                  "China": "Beijing",
   #                 "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# values = capitals.values()
# for value in capitals.values():
# print(value)

# items = capitals.items()
# for key, value in capitals.items():
#    print(f"{key}: {value}")

#functioa block of code place() after the name to invoke it
#def display_invoice(username, amount, due_date):
 #  print(f"Hello {username}")
  # print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")



