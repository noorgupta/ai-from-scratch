# ==========================================================
# FUNCTIONS IN PYTHON
# Comprehensive Practice File
# ==========================================================

# ==========================================================
# 1. Defining and Calling Functions
# ==========================================================

print("\n===== Defining and Calling Functions =====")


def greet():
    print("Hello, Welcome to Python!")


greet()

"""
Output:
Hello, Welcome to Python!

Key Observation:
A function executes only when it is called.
"""

# ==========================================================
# 2. Parameters and Arguments
# ==========================================================

print("\n===== Parameters and Arguments =====")


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Noor")
greet_user("Alice")

"""
Output:
Hello, Noor!
Hello, Alice!

Key Observation:
Parameters receive values passed as arguments.
"""

# ==========================================================
# 3. Positional Arguments
# ==========================================================

print("\n===== Positional Arguments =====")


def subtract(a, b):
    print(a - b)


subtract(10, 3)

"""
Output:
7

Key Observation:
Arguments are matched according to position.
"""

# ==========================================================
# 4. Keyword Arguments
# ==========================================================

print("\n===== Keyword Arguments =====")


def student(name, age):
    print(name, age)


student(age=21, name="Noor")

"""
Output:
Noor 21

Key Observation:
Keyword arguments remove dependency on order.
"""

# ==========================================================
# 5. Default Parameters
# ==========================================================

print("\n===== Default Parameters =====")


def greet(name="Guest"):
    print(f"Welcome, {name}")


greet()
greet("Noor")

"""
Output:
Welcome, Guest
Welcome, Noor

Key Observation:
Default values are used when arguments are omitted.
"""

# ==========================================================
# 6. *args
# ==========================================================

print("\n===== *args =====")


def total(*numbers):
    print(sum(numbers))


total(10, 20)
total(1, 2, 3, 4, 5)

"""
Output:
30
15

Key Observation:
*args collects multiple positional arguments into a tuple.
"""

# ==========================================================
# 7. **kwargs
# ==========================================================

print("\n===== **kwargs =====")


def profile(**details):
    for key, value in details.items():
        print(key, ":", value)


profile(name="Noor", age=21, city="Lucknow")

"""
Output:
name : Noor
age : 21
city : Lucknow

Key Observation:
**kwargs collects keyword arguments into a dictionary.
"""

# ==========================================================
# 8. Return Statement
# ==========================================================

print("\n===== Return Statement =====")


def square(x):
    return x ** 2


result = square(6)

print(result)

"""
Output:
36

Key Observation:
return sends data back to the caller.
"""

# ==========================================================
# 9. Returning Multiple Values
# ==========================================================

print("\n===== Returning Multiple Values =====")


def operations(a, b):
    return a + b, a * b


addition, multiplication = operations(5, 4)

print(addition)
print(multiplication)

"""
Output:
9
20

Key Observation:
Python returns multiple values as a tuple.
"""

# ==========================================================
# 10. Local Scope
# ==========================================================

print("\n===== Local Scope =====")


def local_demo():
    message = "Local Variable"
    print(message)


local_demo()

"""
Output:
Local Variable

Key Observation:
Local variables exist only inside the function.
"""

# ==========================================================
# 11. Global Scope
# ==========================================================

print("\n===== Global Scope =====")

course = "Python"


def show_course():
    print(course)


show_course()

"""
Output:
Python

Key Observation:
Global variables can be accessed inside functions.
"""

# ==========================================================
# 12. global Keyword
# ==========================================================

print("\n===== global Keyword =====")

count = 0


def increase():
    global count
    count += 1


increase()

print(count)

"""
Output:
1

Key Observation:
global allows modification of global variables.
"""

# ==========================================================
# 13. nonlocal Keyword
# ==========================================================

print("\n===== nonlocal Keyword =====")


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()


outer()

"""
Output:
1

Key Observation:
nonlocal modifies variables from the enclosing scope.
"""

# ==========================================================
# 14. Recursion - Countdown
# ==========================================================

print("\n===== Recursion: Countdown =====")


def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)


countdown(5)

"""
Output:
5
4
3
2
1
Done!

Key Observation:
Each recursive call solves a smaller problem.
"""

# ==========================================================
# 15. Recursion - Factorial
# ==========================================================

print("\n===== Recursion: Factorial =====")


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

"""
Output:
120

Key Observation:
Recursion requires a base case to stop.
"""

# ==========================================================
# 16. Recursion - Fibonacci
# ==========================================================

print("\n===== Recursion: Fibonacci =====")


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

"""
Output:
8

Key Observation:
Recursive Fibonacci is simple but inefficient.
"""

# ==========================================================
# 17. Lambda Function
# ==========================================================

print("\n===== Lambda Function =====")

square = lambda x: x ** 2

print(square(8))

"""
Output:
64

Key Observation:
Lambda functions are anonymous one-line functions.
"""

# ==========================================================
# 18. Lambda with map()
# ==========================================================

print("\n===== Lambda with map() =====")

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** 2, numbers))

print(result)

"""
Output:
[1, 4, 9, 16]

Key Observation:
map() applies a function to every element.
"""

# ==========================================================
# 19. Lambda with filter()
# ==========================================================

print("\n===== Lambda with filter() =====")

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

"""
Output:
[2, 4, 6]

Key Observation:
filter() keeps elements that satisfy a condition.
"""

# ==========================================================
# 20. Lambda with sorted()
# ==========================================================

print("\n===== Lambda with sorted() =====")

students = [
    ("Noor", 92),
    ("Aman", 85),
    ("Priya", 97)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)

"""
Output:
[
 ('Aman', 85),
 ('Noor', 92),
 ('Priya', 97)
]

Key Observation:
Lambda is commonly used as the sorting key.
"""

# ==========================================================
# 21. Built-in Functions
# ==========================================================

print("\n===== Built-in Functions =====")

numbers = [5, 10, 15]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Absolute:", abs(-20))
print("Rounded:", round(3.14159, 2))

"""
Output:
Length: 3
Sum: 30
Maximum: 15
Minimum: 5
Absolute: 20
Rounded: 3.14

Key Observation:
Python provides many optimized built-in functions.
"""

# ==========================================================
# 22. zip()
# ==========================================================

print("\n===== zip() =====")

names = ["Noor", "Aman"]
marks = [95, 88]

print(list(zip(names, marks)))

"""
Output:
[('Noor', 95), ('Aman', 88)]

Key Observation:
zip() pairs corresponding elements together.
"""

# ==========================================================
# 23. enumerate()
# ==========================================================

print("\n===== enumerate() =====")

subjects = ["Python", "AI", "Math"]

for index, subject in enumerate(subjects, start=1):
    print(index, subject)

"""
Output:
1 Python
2 AI
3 Math

Key Observation:
enumerate() provides both index and value.
"""

# ==========================================================
# 24. any() and all()
# ==========================================================

print("\n===== any() and all() =====")

values = [True, False, True]

print(any(values))
print(all(values))

"""
Output:
True
False

Key Observation:
any() checks if at least one value is True.
all() checks if every value is True.
"""

# ==========================================================
# 25. type() and isinstance()
# ==========================================================

print("\n===== type() and isinstance() =====")

number = 10

print(type(number))
print(isinstance(number, int))

"""
Output:
<class 'int'>
True

Key Observation:
type() returns the object's type.
isinstance() checks whether an object belongs to a type.
"""

# ==========================================================
# END OF FILE
# ==========================================================