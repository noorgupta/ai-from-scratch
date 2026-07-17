"""
===========================================
PYTHON SETS
Comprehensive Practice File
===========================================
"""

# =====================================================
# 1. Creating Sets
# =====================================================

print("\n========== Creating Sets ==========")

numbers = {1, 2, 3, 4}
print(numbers)

empty_set = set()
print(empty_set)

from_list = set([1, 2, 2, 3, 4, 4])
print(from_list)

from_tuple = set((10, 20, 20, 30))
print(from_tuple)

from_string = set("banana")
print(from_string)

"""
Output:
{1, 2, 3, 4}
set()
{1, 2, 3, 4}
{10, 20, 30}
{'b', 'a', 'n'}

Key Observation:
- Duplicate values are removed automatically.
- {} creates a dictionary, not an empty set.
"""

# =====================================================
# 2. Accessing Elements
# =====================================================

print("\n========== Accessing Elements ==========")

fruits = {"Apple", "Banana", "Mango"}

print("Traversing Set:")

for fruit in fruits:
    print(fruit)

print("Banana" in fruits)
print("Orange" in fruits)

"""
Output:
Apple
Banana
Mango
True
False

(Note: Traversal order may vary.)

Key Observation:
- Sets do not support indexing.
- Membership testing is very fast.
"""

# =====================================================
# 3. Adding Elements
# =====================================================

print("\n========== add() ==========")

colors = {"Red", "Blue"}

colors.add("Green")
print(colors)

colors.add("Blue")
print(colors)

"""
Output:
{'Red', 'Blue', 'Green'}
{'Red', 'Blue', 'Green'}

Key Observation:
Adding an existing element has no effect.
"""

# =====================================================
# 4. update()
# =====================================================

print("\n========== update() ==========")

numbers = {1, 2, 3}

numbers.update([4, 5])
print(numbers)

numbers.update((5, 6, 7))
print(numbers)

"""
Output:
{1,2,3,4,5}
{1,2,3,4,5,6,7}

Key Observation:
update() adds multiple elements from any iterable.
"""

# =====================================================
# 5. remove()
# =====================================================

print("\n========== remove() ==========")

cities = {"Delhi", "Mumbai", "Lucknow"}

cities.remove("Mumbai")

print(cities)

"""
Output:
{'Delhi', 'Lucknow'}

Key Observation:
remove() raises KeyError if the element does not exist.
"""

# =====================================================
# 6. discard()
# =====================================================

print("\n========== discard() ==========")

cities.discard("Kolkata")

print(cities)

"""
Output:
{'Delhi', 'Lucknow'}

Key Observation:
discard() never raises an error.
"""

# =====================================================
# 7. pop()
# =====================================================

print("\n========== pop() ==========")

animals = {"Dog", "Cat", "Horse"}

removed = animals.pop()

print("Removed:", removed)
print("Remaining:", animals)

"""
Output:
(Removed element varies)

Key Observation:
pop() removes an arbitrary element.
"""

# =====================================================
# 8. clear()
# =====================================================

print("\n========== clear() ==========")

items = {1, 2, 3}

items.clear()

print(items)

"""
Output:
set()

Key Observation:
clear() removes every element but the set still exists.
"""

# =====================================================
# 9. Union
# =====================================================

print("\n========== Union ==========")

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

"""
Output:
{1,2,3,4,5}

Key Observation:
Union combines unique elements.
"""

# =====================================================
# 10. Intersection
# =====================================================

print("\n========== Intersection ==========")

print(A & B)

"""
Output:
{3}

Key Observation:
Intersection returns common elements.
"""

# =====================================================
# 11. Difference
# =====================================================

print("\n========== Difference ==========")

print(A - B)
print(B - A)

"""
Output:
{1,2}
{4,5}

Key Observation:
Difference depends on order.
"""

# =====================================================
# 12. Symmetric Difference
# =====================================================

print("\n========== Symmetric Difference ==========")

print(A ^ B)

"""
Output:
{1,2,4,5}

Key Observation:
Removes common elements.
"""

# =====================================================
# 13. Subset
# =====================================================

print("\n========== issubset() ==========")

small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))

"""
Output:
True

Key Observation:
Every element of the first set exists in the second.
"""

# =====================================================
# 14. Superset
# =====================================================

print("\n========== issuperset() ==========")

print(large.issuperset(small))

"""
Output:
True

Key Observation:
Superset contains all elements of another set.
"""

# =====================================================
# 15. Disjoint
# =====================================================

print("\n========== isdisjoint() ==========")

A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))

"""
Output:
True

Key Observation:
Disjoint sets share no common elements.
"""

# =====================================================
# 16. Hashable Objects
# =====================================================

print("\n========== Hashable Objects ==========")

valid = {
    10,
    "Python",
    (1, 2)
}

print(valid)

"""
Output:
{10, 'Python', (1,2)}

Key Observation:
Only immutable (hashable) objects can be stored.
"""

# =====================================================
# 17. Time Complexity Demonstration
# =====================================================

print("\n========== Membership ==========")

languages = {
    "Python",
    "Java",
    "C++",
    "Go"
}

print("Python" in languages)
print("Rust" in languages)

"""
Output:
True
False

Key Observation:
Membership testing in sets is O(1) on average.
"""

# =====================================================
# 18. Common Mistakes
# =====================================================

print("\n========== Common Mistakes ==========")

# Empty set

empty = {}

print(type(empty))

correct = set()

print(type(correct))

"""
Output:
<class 'dict'>
<class 'set'>

Key Observation:
{} creates a dictionary.
"""

# =====================================================
# End of File
# =====================================================

print("\nCongratulations! You have completed Python Sets.")