'''LIST AND TUPLES'''

# List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


''' LIST '''

marks = [90, 80, 70, 60, 50]
print(marks) # prints the list
print(len(marks)) # prints the length of the list
print(marks[0]) # prints the first element of the list
print(marks[1]) # prints the second element of the list
print(marks[2]) # prints the third element of the list


student = ["John", 95, 17, "delhi"]
print(student[0]) # prints the first element of the list
student[0] = "Rishabh" # changes the first element of the list
print(student) # prints the list after changing the first element


''' TUPLE '''
# a built in data type in Python that is used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.


tup = (1, 2, 3, 4, 5)
print(tup) # prints the tuple

print(len(tup)) # prints the length of the tuple
print(tup[1:3]) # prints the second and third elements of the tuple


'''tuple indexing and counting'''

print(tup.index(3)) # prints the index of the first occurrence of 3 in the tuple
print(tup.count(3)) # prints the number of times 3 appears in the tuple

'''PRACTICE QUESTIONS'''
'''Q - 1'''


# movies = []

# mov1=(input("Enter 1st favorite movie: "))
# mov2=(input("Enter 2nd favorite movie: "))
# mov3=(input("Enter 3rd favorite movie: "))

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies) # prints the list of favorite movies

# '''Q - 2'''

# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 5, 4, 3]

# copy_list1 = list1.copy() # creates a copy of list1
# copy_list1.reverse() # reverses the copy of list1

# if(copy_list1 == list2): # checks if the reversed copy of list1 is equal to list2
#     print("palindrome")
# else:
#     print("not palindrome")



