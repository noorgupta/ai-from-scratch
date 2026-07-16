"""
===========================================
Topic: Tuples in Python
Description: Examples of all major tuple concepts.
===========================================
"""

# ===========================================
# 1. Creating Tuples
# ===========================================

empty_tuple = ()

numbers = (10, 20, 30)

mixed = ("Noor", 20, True, 8.9)

single = (100,)

letters = tuple("AI")

print(empty_tuple)
print(numbers)
print(mixed)
print(single)
print(letters)

"""
Output:
()
(10, 20, 30)
('Noor', 20, True, 8.9)
(100,)
('A', 'I')
"""

# ===========================================
# 2. Accessing Elements
# ===========================================

student = ("Noor", 20, "BCA", 8.9)

print(student[0])
print(student[-1])
print(student[1:3])

"""
Output:
Noor
8.9
(20, 'BCA')
"""

# ===========================================
# 3. Tuple Immutability
# ===========================================

numbers = (10, 20, 30)

print(numbers)

# numbers[0] = 100     # TypeError

"""
Output:
(10, 20, 30)

Note:
Trying to modify a tuple raises:
TypeError: 'tuple' object does not support item assignment
"""

# ===========================================
# 4. Tuple Methods
# ===========================================

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
print(numbers.index(20))

"""
Output:
3
1
"""

# ===========================================
# 5. Tuple Packing
# ===========================================

student = "Noor", 20, "BCA"

print(student)

"""
Output:
('Noor', 20, 'BCA')
"""

# ===========================================
# 6. Tuple Unpacking
# ===========================================

student = ("Noor", 20, "BCA")

name, age, course = student

print(name)
print(age)
print(course)

"""
Output:
Noor
20
BCA
"""

# ===========================================
# 7. Swapping Variables
# ===========================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)

"""
Output:
20
10
"""

# ===========================================
# 8. Extended Unpacking
# ===========================================

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

"""
Output:
10
[20, 30, 40]
50
"""

# ===========================================
# 9. Nested Tuples
# ===========================================

students = (
    ("Noor", 20),
    ("Aman", 21),
    ("Priya", 19)
)

print(students[1][0])

for student in students:
    print(student)

"""
Output:
Aman
('Noor', 20)
('Aman', 21)
('Priya', 19)
"""

# ===========================================
# 10. Tuple with Mutable Object
# ===========================================

data = (
    "Python",
    [10, 20]
)

data[1].append(30)

print(data)

"""
Output:
('Python', [10, 20, 30])

Note:
The tuple is immutable, but the list inside it is mutable.
"""

# ===========================================
# 11. Lists vs Tuples
# ===========================================

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print(type(my_list))
print(type(my_tuple))

"""
Output:
<class 'list'>
<class 'tuple'>
"""