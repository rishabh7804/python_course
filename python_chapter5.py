'''dictionaries'''

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# info ={
#     "name": "John",
#     "age": 30,
#     "city": "delhi",
#     "tools": ["dictionary"],
# }
# print(type(info)) # prints the type of the variable info
# print(info) # prints the dictionary

'''nested dictionary'''

# student ={
#     "name": "rishabh",
#     "age": 17,
#     "subjects":{
#         "Math": 90,
#         "Science": 85,
#         "English": 80
#     }

# }
# print(student) # prints the nested dictionary
# print(student["subjects"]["Math"]) # prints the value of the key "Math" in the nested dictionary


# print(student.keys()) # prints the keys of the dictionary
# print(list(student.keys())) # prints the keys of the dictionary as a list

# print(student.values()) # prints the values of the dictionary
# print(list(student.values())) # prints the values of the dictionary as a list

# print(student.items()) # prints the items of the dictionary as a list of tuples
# print(list(student.items())) # prints the items of the dictionary as a list of tuples

# pairs = list(student.items())
# print(pairs[0])

# print(student.get("name")) # prints the value of the key "name" in the dictionary
# print(student.get("age")) # prints the value of the key "age" in the dictionary

# print(student.update({"city": "mumbai"}))
# print(student.update({"age": 18}))

# print(student) # prints the updated dictionary


'''set in python'''

""" set is a collection of unique elements. It is unordered and does not allow duplicate values. """

collection = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(collection) # prints the set
print(type(collection)) # prints the type of the variable collection

print(collection.add(11)) # adds the value 11 to the set
print(collection) # prints the updated set

print(collection.remove(5)) # removes the value 5 from the set
print(collection) # prints the updated set

print(collection.discard(6)) # removes the value 6 from the set
print(collection) # prints the updated set

print(collection.pop()) # removes and returns an arbitrary element from the set
print(collection) # prints the updated set

print(collection.clear()) # removes all elements from the set
print(collection) # prints the empty set

print(collection.add(1)) # adds the value 1 to the set
print(collection) # prints the updated set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # prints the union of set1 and set2
print(set1.intersection(set2)) # prints the intersection of set1 and set2
print(set1.difference(set2)) # prints the difference of set1 and set2



'''Practice problems'''
'''
'''
dictionary = {
    "name": "John",

    "age": [30],
    "city": ["New York"]
}
print(dictionary) # prints the dictionary


'''2'''

subjects = {
    "python","java", "c++", "javascript","c++"

}
print(subjects) # prints the set of subjects

'''3'''
marks = {}

x = int(input("enter physics marks: "))
marks.update({"physics": x})

x = int(input("enter chemistry marks: "))
marks.update({"chemistry":x})

x = int(input("enter biology marks: "))
marks.update({"biology":x})

print(marks) # prints the marks dictionary

