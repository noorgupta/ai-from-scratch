# Lambda Functions

## 📖 Overview

A **lambda function** is a small, anonymous (unnamed) function in Python.

Unlike a regular function defined using the `def` keyword, a lambda function is created in a single line and is generally used for simple operations.

Lambda functions are especially useful when a function is needed only once or for a short period, such as while sorting data or processing collections.

---

## ❓ Why Do We Need Lambda Functions?

Suppose we want to square a number.

Using a normal function:

```python
def square(number):
    return number * number

print(square(5))
```

**Output**

```text
25
```

If the function is only needed once, defining it separately may be unnecessary.

Lambda provides a shorter alternative.

```python
square = lambda number: number * number

print(square(5))
```

**Output**

```text
25
```

Both produce the same result.

---

# 🧠 Syntax

General syntax:

```python
lambda parameters: expression
```

Components:

- `lambda` → Keyword used to create an anonymous function.
- Parameters → Inputs to the function.
- Expression → A single expression whose value is automatically returned.

Unlike normal functions, lambda functions **do not use the `return` keyword**.

---

# 🧠 Lambda vs Normal Function

### Normal Function

```python
def add(a, b):
    return a + b
```

### Lambda Function

```python
add = lambda a, b: a + b
```

Both functions behave identically.

---

# 🧠 Lambda with One Parameter

```python
square = lambda x: x ** 2

print(square(6))
```

**Output**

```text
36
```

---

# 🧠 Lambda with Multiple Parameters

```python
multiply = lambda a, b: a * b

print(multiply(4, 5))
```

**Output**

```text
20
```

---

# 🧠 Using Lambda with `map()`

`map()` applies a function to every element of an iterable.

Without lambda:

```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]

result = list(map(square, numbers))

print(result)
```

Using lambda:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

**Output**

```text
[1, 4, 9, 16]
```

---

# 🧠 Using Lambda with `filter()`

`filter()` selects elements that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

**Output**

```text
[2, 4, 6]
```

---

# 🧠 Using Lambda with `sorted()`

Lambda functions are commonly used to specify sorting criteria.

```python
students = [
    ("Noor", 92),
    ("Aman", 85),
    ("Priya", 96)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)
```

**Output**

```text
[
 ('Aman', 85),
 ('Noor', 92),
 ('Priya', 96)
]
```

The list is sorted by marks instead of names.

---

# 🧠 Using Lambda with Dictionaries

```python
students = [
    {"name": "Noor", "age": 21},
    {"name": "Aman", "age": 19},
    {"name": "Priya", "age": 22}
]

students.sort(key=lambda student: student["age"])

print(students)
```

The list is sorted according to the `"age"` value.

---

# 🧠 Immediately Invoked Lambda Function

A lambda function can be executed immediately.

```python
result = (lambda x, y: x + y)(10, 20)

print(result)
```

**Output**

```text
30
```

Although valid, this style is uncommon in Python.

---

## ⚙️ Behind the Scenes

A lambda function is still a function object.

Example:

```python
square = lambda x: x ** 2
```

Conceptually, Python treats it similarly to:

```python
def square(x):
    return x ** 2
```

The main differences are:

- No function name in the definition.
- Limited to a single expression.
- Automatically returns the expression's value.

---

## 🌍 Real-World Applications

Lambda functions are widely used in:

- Sorting records
- Filtering data
- Transforming lists
- Event handling
- Data pipelines
- Configuration processing

They are especially useful when a function is needed only once.

---

## 🤖 AI Connection

Lambda functions are common in AI and data science workflows.

Examples include:

- Transforming datasets.
- Sorting predictions by confidence score.
- Filtering records.
- Feature engineering.
- Preprocessing data.
- Applying quick mathematical transformations.

Libraries such as **Pandas**, **NumPy**, and **Scikit-learn** often use lambda functions for concise data manipulation.

Example:

```python
data["Age"] = data["Age"].apply(lambda age: age + 1)
```

---

## 💼 Best Practices

- Use lambda functions only for short, simple operations.
- Prefer regular functions for complex logic.
- Use descriptive variable names around lambda expressions.
- Combine lambda with `map()`, `filter()`, and `sorted()` when it improves readability.

---

## ⚠️ Common Mistakes

### Writing Complex Lambda Functions

Avoid:

```python
lambda x: (
    x + 1 if x > 0
    else x - 1 if x < 0
    else 0
)
```

If the logic becomes difficult to read, use a normal function.

---

### Trying to Use Multiple Statements

Incorrect:

```python
lambda x:
    print(x)
    return x
```

A lambda function can contain **only one expression**.

---

### Overusing Lambda

Not every small function needs to be a lambda.

If the function is reused or contains business logic, define it with `def`.

---

## 📝 Interview Insight

### Question

What is the difference between a lambda function and a normal function?

### Answer

| Lambda Function | Normal Function |
|-----------------|-----------------|
| Anonymous | Named |
| Single expression | Multiple statements allowed |
| Implicit return | Uses `return` keyword |
| Best for short operations | Best for reusable and complex logic |

---

## 💡 Remember This

```
def

↓

Reusable
Named
Multiple Statements

----------------------------

lambda

↓

Anonymous
One Expression
Implicit Return
```

Use **`def`** for complex or reusable functions.

Use **`lambda`** for short, temporary operations.

---

## 🎯 Key Takeaways

- Lambda functions are anonymous, single-expression functions.
- They automatically return the value of their expression.
- They are commonly used with `map()`, `filter()`, and `sorted()`.
- Lambda functions improve code conciseness for simple tasks.
- For complex logic or reusable functionality, prefer regular functions.

---

## 💻 Code Reference

`code/functions.py`