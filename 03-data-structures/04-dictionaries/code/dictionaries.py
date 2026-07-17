"""
===========================================
PYTHON DICTIONARIES
Comprehensive Practice File
===========================================
"""

# =====================================================
# 1. Creating Dictionaries
# =====================================================

print("\n========== Creating Dictionaries ==========")

student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}

print(student)

empty = {}
print(empty)

student2 = dict(
    name="Aman",
    age=22,
    course="B.Tech"
)

print(student2)

data = [
    ("city", "Lucknow"),
    ("state", "Uttar Pradesh")
]

print(dict(data))

subjects = ["Python", "AI", "Math"]

print(dict.fromkeys(subjects, 0))

"""
Output:
{'name': 'Noor', 'age': 21, 'course': 'BCA'}
{}
{'name': 'Aman', 'age': 22, 'course': 'B.Tech'}
{'city': 'Lucknow', 'state': 'Uttar Pradesh'}
{'Python': 0, 'AI': 0, 'Math': 0}

Key Observation:
Python provides multiple ways to create dictionaries.
"""

# =====================================================
# 2. Accessing Elements
# =====================================================

print("\n========== Accessing Elements ==========")

print(student["name"])

print(student.get("age"))

print(student.get("cgpa"))

print(student.get("cgpa", "Not Available"))

print("course" in student)

"""
Output:
Noor
21
None
Not Available
True

Key Observation:
Use get() when a key may not exist.
"""

# =====================================================
# 3. Adding Elements
# =====================================================

print("\n========== Adding Elements ==========")

student["city"] = "Lucknow"

print(student)

"""
Output:
{'name':'Noor','age':21,'course':'BCA','city':'Lucknow'}

Key Observation:
Assigning a new key automatically adds it.
"""

# =====================================================
# 4. Updating Elements
# =====================================================

print("\n========== Updating Elements ==========")

student["age"] = 22

print(student)

student.update({
    "course": "MCA",
    "cgpa": 8.8
})

print(student)

"""
Output:
Age updated
Course updated
CGPA added

Key Observation:
update() can both update and insert.
"""

# =====================================================
# 5. pop()
# =====================================================

print("\n========== pop() ==========")

removed = student.pop("cgpa")

print("Removed:", removed)

print(student)

print(student.pop("salary", "Not Found"))

"""
Output:
8.8

Dictionary after removal

Not Found

Key Observation:
pop() returns the removed value.
"""

# =====================================================
# 6. popitem()
# =====================================================

print("\n========== popitem() ==========")

last = student.popitem()

print(last)

print(student)

"""
Output:
(Removes last inserted pair)

Key Observation:
Python 3.7+ preserves insertion order.
"""

# =====================================================
# 7. del
# =====================================================

print("\n========== del ==========")

del student["city"]

print(student)

"""
Output:
City removed.

Key Observation:
del removes a key permanently.
"""

# =====================================================
# 8. clear()
# =====================================================

print("\n========== clear() ==========")

temp = {
    "a": 1,
    "b": 2
}

temp.clear()

print(temp)

"""
Output:
{}

Key Observation:
clear() empties the dictionary.
"""

# =====================================================
# 9. keys()
# =====================================================

print("\n========== keys() ==========")

student = {
    "name": "Noor",
    "age": 22,
    "course": "MCA"
}

print(student.keys())

"""
Output:
dict_keys([...])

Key Observation:
Returns a dynamic view of keys.
"""

# =====================================================
# 10. values()
# =====================================================

print("\n========== values() ==========")

print(student.values())

"""
Output:
dict_values(...)

Key Observation:
Returns all values.
"""

# =====================================================
# 11. items()
# =====================================================

print("\n========== items() ==========")

print(student.items())

"""
Output:
dict_items(...)

Key Observation:
Returns key-value pairs.
"""

# =====================================================
# 12. copy()
# =====================================================

print("\n========== copy() ==========")

copy_student = student.copy()

print(copy_student)

"""
Output:
Dictionary copy

Key Observation:
Creates a shallow copy.
"""

# =====================================================
# 13. setdefault()
# =====================================================

print("\n========== setdefault() ==========")

student.setdefault("city", "Lucknow")

student.setdefault("name", "Rahul")

print(student)

"""
Output:
City added.
Name unchanged.

Key Observation:
Adds only if the key doesn't exist.
"""

# =====================================================
# 14. Iteration
# =====================================================

print("\n========== Iteration ==========")

print("Keys")

for key in student:
    print(key)

print("\nValues")

for value in student.values():
    print(value)

print("\nItems")

for key, value in student.items():
    print(key, ":", value)

"""
Output:
Keys
Values
Items

Key Observation:
items() is the preferred way when both key and value are needed.
"""

# =====================================================
# 15. enumerate()
# =====================================================

print("\n========== enumerate() ==========")

for index, (key, value) in enumerate(student.items(), start=1):
    print(index, key, value)

"""
Output:
1 name Noor
2 age 22
...

Key Observation:
Useful for numbered output.
"""

# =====================================================
# 16. Nested Dictionaries
# =====================================================

print("\n========== Nested Dictionaries ==========")

students = {
    "student1": {
        "name": "Noor",
        "age": 22
    },
    "student2": {
        "name": "Aman",
        "age": 21
    }
}

print(students["student1"]["name"])

students["student1"]["city"] = "Lucknow"

print(students)

"""
Output:
Noor

Nested dictionary updated.

Key Observation:
Access one level at a time.
"""

# =====================================================
# 17. Iterating Nested Dictionaries
# =====================================================

print("\n========== Nested Iteration ==========")

for student_id, details in students.items():

    print(student_id)

    for key, value in details.items():
        print(key, ":", value)

"""
Output:
student1
name : Noor
...

Key Observation:
Nested loops are required.
"""

# =====================================================
# 18. Dictionary Inside List
# =====================================================

print("\n========== Dictionary Inside List ==========")

employees = [
    {"name": "Noor", "role": "Developer"},
    {"name": "Aman", "role": "Designer"}
]

print(employees[0]["role"])

"""
Output:
Developer

Key Observation:
Common in API responses.
"""

# =====================================================
# 19. List Inside Dictionary
# =====================================================

print("\n========== List Inside Dictionary ==========")

person = {
    "name": "Noor",
    "skills": [
        "Python",
        "FastAPI",
        "AI"
    ]
}

print(person["skills"][1])

"""
Output:
FastAPI

Key Observation:
Lists and dictionaries are often combined.
"""

# =====================================================
# 20. Hashable Keys
# =====================================================

print("\n========== Hashable Keys ==========")

valid = {
    "Python": "Language",
    (1, 2): "Tuple",
    10: "Integer"
}

print(valid)

"""
Output:
Dictionary printed successfully.

Key Observation:
Only immutable objects can be dictionary keys.
"""

# =====================================================
# 21. Common Mistakes
# =====================================================

print("\n========== Common Mistakes ==========")

example = {}

print(type(example))

print("salary" in student)

"""
Output:
<class 'dict'>
False

Key Observation:
{} creates an empty dictionary.
'in' checks keys, not values.
"""

# =====================================================
# End of File
# =====================================================

print("\n🎉 Congratulations! You have completed Python Dictionaries.")