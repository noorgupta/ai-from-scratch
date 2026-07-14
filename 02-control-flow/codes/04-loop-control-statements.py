"""
Topic: Loop Control Statements
Description: Examples of break, continue, and pass.
"""

# break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print()

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print()

# pass
for i in range(5):
    if i == 2:
        pass
    print(i)