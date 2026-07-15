"""
===========================================
Topic: Lists in Python
Description: Examples of all major list concepts.
===========================================
"""

# ===========================================
# 1. Creating Lists
# ===========================================

empty_list = []

numbers = [10, 20, 30]

mixed = [1, "Python", True, 3.14]

letters = list("AI")

zeros = [0] * 5

print("Creating Lists")
print(empty_list)
print(numbers)
print(mixed)
print(letters)
print(zeros)

print("-" * 50)

# ===========================================
# 2. Accessing Elements
# ===========================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Accessing Elements")

print(fruits[0])

print(fruits[-1])

print(fruits[1:3])

print("-" * 50)

# ===========================================
# 3. Modifying Elements
# ===========================================

marks = [75, 80, 90]

marks[1] = 85

print("Modifying Elements")

print(marks)

print("-" * 50)

# ===========================================
# 4. Deleting Elements
# ===========================================

numbers = [10, 20, 30, 40]

numbers.remove(20)

removed = numbers.pop()

print("Deleting Elements")

print(numbers)

print("Removed:", removed)

print("-" * 50)

# ===========================================
# 5. Adding Elements
# ===========================================

fruits = ["Apple", "Banana"]

fruits.append("Mango")

fruits.extend(["Orange", "Grapes"])

fruits.insert(1, "Kiwi")

print("Adding Elements")

print(fruits)

print("-" * 50)

# ===========================================
# 6. Searching & Counting
# ===========================================

numbers = [10, 20, 10, 30, 10]

print("Searching & Counting")

print(numbers.index(20))

print(numbers.count(10))

print("-" * 50)

# ===========================================
# 7. Ordering & Copying
# ===========================================

numbers = [40, 10, 30, 20]

numbers.sort()

print("Sorted")

print(numbers)

numbers.reverse()

print("Reversed")

print(numbers)

copy_numbers = numbers.copy()

print("Copied")

print(copy_numbers)

print("-" * 50)

# ===========================================
# 8. List Slicing
# ===========================================

numbers = [10, 20, 30, 40, 50]

print("List Slicing")

print(numbers[:3])

print(numbers[2:])

print(numbers[::2])

print(numbers[::-1])

print("-" * 50)

# ===========================================
# 9. Traversing Lists
# ===========================================

print("Traversing")

for fruit in fruits:
    print(fruit)

print("-" * 50)

# ===========================================
# 10. List Comprehension
# ===========================================

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print("List Comprehension")

print(squares)

print("-" * 50)

# ===========================================
# 11. Nested Lists
# ===========================================

matrix = [
    [1, 2],
    [3, 4]
]

print("Nested Lists")

print(matrix[1][0])

print("-" * 50)

# ===========================================
# 12. Memory Behind Lists
# ===========================================

list1 = [1, 2, 3]

list2 = list1

list3 = list1.copy()

print("Memory")

print(id(list1))

print(id(list2))

print(id(list3))

list2.append(4)

print(list1)

print(list3)