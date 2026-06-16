set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 ^ set2)  # Symmetric Difference
print(set1 - set2)  # Difference

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print({**dict1, **dict2})  # Merging dictionaries (dict2 values will overwrite dict1 values for duplicate keys)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatenation of lists
print(list1 * 2)  # Repetition of list1


student = {"name": "Alice", "age": 25, "grade": "A"}
while student:
    key, value = student.popitem()  # Remove and return an arbitrary key-value pair
    print(key, value)
# for key, value in student.items():
#     print(key, value)
students = [
    {"name": "Alice", "age": 25, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 23, "grade": "C"}
]
# for student in students:
#     print(student["name"], student["grade"])    
while students:
    student1 = students.pop(0)  # Remove the first student from the list
    print(student1["name"], student1["grade"])
student["name"] = "Chandan"
student["subject"] = "Math"
student["age"] = 32
student["grade"] = "A+"
print("student data") 
print(student)
del student["grade"]
print("student data after deleting grade") 
print(student)

student.pop("subject")
print("student data after popping subject")
print(student)