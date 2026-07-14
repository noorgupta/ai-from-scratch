"""
Topic: While Loop
Description: Examples of condition-based iteration.
"""

# Counting from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1

print()

# Password example
password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted!")