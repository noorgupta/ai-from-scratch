# Return Statement

## 📖 Overview

The `return` statement is used to send a value back from a function to the place where the function was called.

Unlike `print()`, which only displays information on the screen, `return` allows the result of a function to be stored, reused, modified, or passed to another function.

Almost every real-world Python application uses `return` because functions often need to produce results rather than simply display them.

---

## ❓ Why Do We Need `return`?

Suppose we want to calculate the sum of two numbers.

Using `print()`:

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

**Output**

```text
30
None
```

The function prints `30`, but the variable `result` contains `None` because nothing was returned.

Using `return`:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

**Output**

```text
30
```

Now the value can be reused anywhere in the program.

---

# 🧠 Syntax

```python
def function_name():
    return value
```

Example:

```python
def square(number):
    return number * number
```

---

# 🧠 Returning a Single Value

```python
def cube(number):
    return number ** 3

result = cube(4)

print(result)
```

**Output**

```text
64
```

The returned value is stored in `result`.

---

# 🧠 Returning Multiple Values

Python allows multiple values to be returned.

```python
def student():
    return "Noor", 21, "BCA"

data = student()

print(data)
```

**Output**

```text
('Noor', 21, 'BCA')
```

Python automatically packs the returned values into a tuple.

---

## 🧠 Unpacking Returned Values

```python
def student():
    return "Noor", 21

name, age = student()

print(name)
print(age)
```

**Output**

```text
Noor
21
```

---

# 🧠 Returning Different Data Types

Functions can return any Python object.

### Integer

```python
return 100
```

### Float

```python
return 3.14
```

### String

```python
return "Hello"
```

### List

```python
return [1, 2, 3]
```

### Dictionary

```python
return {
    "name": "Noor"
}
```

### Boolean

```python
return True
```

### Object

Functions can also return custom objects created using classes.

---

# 🧠 Returning `None`

If a function does not explicitly return a value, Python automatically returns `None`.

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

**Output**

```text
Hello
None
```

Conceptually:

```text
No return statement
        │
        ▼
Python automatically returns None
```

---

# 🧠 Early Return

A function stops executing immediately after encountering `return`.

```python
def check(number):

    if number < 0:
        return "Negative"

    return "Positive"

print(check(-5))
print(check(10))
```

**Output**

```text
Negative
Positive
```

Anything after `return` is ignored.

---

# 🧠 Code After `return`

```python
def greet():

    return "Hello"

    print("World")
```

The `print("World")` statement is **never executed**.

Execution stops as soon as `return` is reached.

---

## ⚙️ Behind the Scenes

Consider:

```python
def square(x):
    return x * x
```

When called:

```python
result = square(5)
```

Python performs the following steps:

1. Creates a new local namespace.
2. Assigns `5` to `x`.
3. Calculates `x * x`.
4. Returns `25`.
5. Destroys the local namespace.
6. Stores `25` in `result`.

Conceptually:

```text
Function Call
      │
      ▼
Execute Function
      │
      ▼
return Value
      │
      ▼
Back to Caller
```

---

## 🌍 Real-World Applications

The `return` statement is used in:

- Login validation
- Database queries
- API responses
- Search algorithms
- Mathematical calculations
- File processing
- Data analysis

Almost every function in production code returns a value.

---

## 🤖 AI Connection

AI and Machine Learning libraries rely heavily on returned values.

Examples:

```python
model = train_model(data)
```

```python
predictions = predict(image)
```

```python
accuracy = evaluate_model(test_data)
```

Functions return models, predictions, metrics, and processed datasets that are reused throughout the workflow.

---

## 💼 Best Practices

- Return values instead of printing whenever the result needs further processing.
- Keep return values predictable and consistent.
- Use descriptive variable names to store returned values.
- Return early to simplify complex logic.

---

## ⚠️ Common Mistakes

### Confusing `print()` with `return`

Incorrect:

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
```

`result` becomes:

```text
None
```

Correct:

```python
def add(a, b):
    return a + b
```

---

### Writing Code After `return`

```python
def example():

    return 10

    print("Hello")
```

The `print()` statement never runs.

---

### Forgetting to Store the Returned Value

```python
def square(x):
    return x * x

square(5)
```

The value is returned but discarded.

Better:

```python
result = square(5)
```

---

## 📝 Interview Insight

### Question

What is the difference between `print()` and `return`?

### Answer

| `print()` | `return` |
|-----------|-----------|
| Displays output on the screen | Sends a value back to the caller |
| Cannot be reused directly | Returned value can be stored and reused |
| Mainly used for debugging or displaying information | Used for producing results in reusable functions |

---

## 💡 Remember This

- `print()` shows information.
- `return` sends information back.
- A function stops executing after `return`.
- If no value is returned, Python returns `None`.
- A function can return multiple values.

---

## 🎯 Key Takeaways

- `return` sends values back from a function.
- Returned values can be stored, reused, or passed to other functions.
- `print()` and `return` serve different purposes.
- Functions automatically return `None` if no `return` statement is present.
- Understanding `return` is essential for writing reusable and maintainable Python programs.

---

## 💻 Code Reference

`code/functions.py`