''' COMMENTS IN PYTHON'''

# This is a single line comment

# """ This is a multi line comment"""


'''INPUT IN PYTHON'''

# '''input () statement is used to accept values (using kryboard) form user'''

''' strinng input'''

# name = input("Enter your name:")
# print("Hello,", name)

'''integer input'''

# age = int (input("enter your age :"))
# print("your age is:", age)

'''float input'''

# price = float(input("enter the price:"))
# print("the price is:", price)

'''example'''

# name = input("enter your name:")
# age = int(input("enter your age:"))
# price = float(input("enter the price:"))

# print("my name is", name, "and i am ", age," years old and the price is")


'''Conditional Statements'''

# if statement
# elif statement
# else statement

# light = input("light :")
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("wait")
# elif(light=="green"):
#     print("go")
# else:
#     print("invalid input")


'''grade calculation'''

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("A grade")

# elif marks >= 80:
#     print("B grade")

# elif marks >= 70:
#     print("C grade")

# else:
#     print("Fail")


'''single line if statement , ternary operator'''

# age = int(input("enter your age:"))
# print("eligible to vote") if age >= 18 else print("not eligible to vote")

# food = input("food :")
# eat = "yes" if food == "pizza" else "no"
# print(eat)

'''type conversion in python'''

# a = 10
# b = 3.14

# print(a+b)  # addition of int and float

# a = int("10")  # string to int
# b = 3.14
# print(a+b)  # addition of int and float
# print(type(a))  # type of a