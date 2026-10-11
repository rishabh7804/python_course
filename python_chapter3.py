# # ''' string is data type that stores a sequence of characters. it is used to store text data. string is immutable data type.'''

" concatenation "

# # # str1 = "rishabh"
# # # str2 = "masram"
# # # len1 =len(str1)
# # # len2 = len(str2)
# # # final_str = str1 + " " + str2
# # # print(final_str)
# # # print("length of str1:", len1)
# # # print("length of str2:", len2)

'''indexing '''

# # str = "rishabh masram"

# # print(str[3])  # prints the character at index 3
# # print(str[0])  # prints the character at index 0


 ''' slicing '''

# # str = "rishabh masram"

# # print(str[0:7])  # prints the characters from index 0 to 6
# # print(str[8:14])  # prints the characters from index 8 to 13
# # print(str[0:14:2])  # prints the characters from index 0 to 13 with a step of 2

# # print(str[-5:-1])  # prints the characters from index -5 to -2


# ''' practice '''

# name = "rishabh masram"
# print(name)
# print(len(name))

# str="rishabh masram"
# print(str.count("a"))  # counts the number of occurrences of "a" in the string


 ''' CONDITIONAL STATEMENTS '''

# '''if - elif - else''' #statements are used to perform different actions based on different conditions.
 '''Q -1'''
# light = input("Enter the color of the traffic light (red/yellow/green): ")

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("get ready")
# elif(light == "green"):
#     print("go")

 '''Q -2'''
# age = int(input("enter your age:"))
# if(age >= 18):
#     print("you can vote")
# else:
#     print("you cannot vote")

 '''Q - 3'''

# marks = int(input("enter your marks:"))
# if (marks >=90):
#     print("A grade")
# elif (marks >=80):
#     print("B grade")
# elif (marks >=70):
#     print("C grade")
# elif(70>marks):
#     print("D grade")
# else:
#     print("fail")


 '''Q - 4'''
# marks = int(input("enter your marks:"))
# if (marks >=90):
#     print("A grade")
# elif (90 > marks >=80):
#     print("B grade")
# elif (70 < marks < 80):
#     print("C grade")
# elif(70 > marks):
#     print("D grade")
# else:
#     print("fail")


 '''Q - 5'''

# num = int(input("enter a number:"))

# if(num % 2 == 0):
#     print("even number")
# else:
#     print("odd number")