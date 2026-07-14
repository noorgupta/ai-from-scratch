"""
Topic: Nested Loops
Description: Examples of loops inside loops.
"""

# Printing coordinates
for i in range(3):
    for j in range(2):
        print(i, j)

print()

# Pattern printing
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()