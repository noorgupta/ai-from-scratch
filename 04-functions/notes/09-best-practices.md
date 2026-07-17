# Best Practices for Writing Functions

## 📖 Overview

Writing a function that works is only the first step.

Professional developers write functions that are:

- Easy to read
- Easy to understand
- Easy to test
- Easy to reuse
- Easy to maintain

Following best practices makes your code more reliable and easier for others (and your future self) to work with.

---

## ❓ Why Do Best Practices Matter?

Imagine a project with hundreds of functions.

Poorly written functions can lead to:

- Difficult debugging
- Duplicate code
- Confusing logic
- Unexpected bugs
- Poor collaboration

Good function design solves these problems.

---

# 🧠 Follow the Single Responsibility Principle (SRP)

A function should perform **one well-defined task**.

❌ Poor Example

```python
def process_student():
    # Read file
    # Calculate marks
    # Save database
    # Send email
```

This function performs multiple unrelated tasks.

---

✅ Better Example

```python
def calculate_marks():
    pass

def save_student():
    pass

def send_email():
    pass
```

Each function has one clear responsibility.

---

# 🧠 Choose Meaningful Function Names

Function names should clearly describe their purpose.

❌ Poor

```python
def fun():
    pass

def xyz():
    pass
```

---

✅ Better

```python
def calculate_average():
    pass

def validate_email():
    pass

def load_dataset():
    pass
```

Good names reduce the need for extra comments.

---

# 🧠 Follow PEP 8 Naming Conventions

Python recommends using **snake_case** for function names.

✅ Correct

```python
def calculate_total():
    pass
```

❌ Avoid

```python
def CalculateTotal():
    pass

def calculateTotal():
    pass
```

---

# 🧠 Keep Functions Small

Large functions are difficult to understand.

Instead of writing:

```python
def manage_system():
    # 200 lines
```

Split it into smaller functions.

```python
login()

validate_user()

load_dashboard()

logout()
```

Small functions are easier to test and debug.

---

# 🧠 Avoid Duplicate Code

Instead of:

```python
print("Hello, Noor")

print("Hello, Aman")

print("Hello, Priya")
```

Create one reusable function.

```python
def greet(name):
    print("Hello,", name)
```

---

# 🧠 Return Values Instead of Printing

Prefer:

```python
def square(x):
    return x * x
```

Instead of:

```python
def square(x):
    print(x * x)
```

Returned values can be reused.

```python
result = square(5)

print(result + 10)
```

---

# 🧠 Use Docstrings

Docstrings explain what a function does.

```python
def calculate_area(radius):
    """
    Returns the area of a circle.
    """
```

They improve readability and help generate documentation automatically.

---

# 🧠 Use Type Hints

Type hints improve code clarity.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Benefits:

- Better readability
- Improved IDE support
- Easier debugging
- Static type checking

Type hints are recommendations—they do not enforce types at runtime.

---

# 🧠 Avoid Global Variables

Prefer passing data through parameters.

❌ Avoid

```python
count = 0

def increment():
    global count
    count += 1
```

---

✅ Better

```python
def increment(count):
    return count + 1
```

This makes the function more predictable and reusable.

---

# 🧠 Pure vs Impure Functions

### Pure Function

A pure function:

- Depends only on its inputs.
- Produces the same output for the same inputs.
- Does not modify external state.

```python
def square(x):
    return x * x
```

---

### Impure Function

An impure function depends on or changes external state.

```python
count = 0

def increment():
    global count
    count += 1
```

Pure functions are generally easier to test and maintain.

---

# 🧠 Avoid Side Effects

A side effect is any change outside the function itself.

Examples:

- Modifying global variables
- Writing to files
- Updating databases
- Printing unnecessarily
- Sending network requests

Limit side effects unless they are the function's primary purpose.

---

# 🧠 Write Testable Functions

Good functions are easy to test.

```python
def multiply(a, b):
    return a * b
```

Testing becomes simple:

```python
assert multiply(2, 3) == 6
```

---

## ⚙️ Behind the Scenes

Professional software is built from many small functions working together.

Conceptually:

```text
Main Program
      │
      ▼
load_data()

      │
      ▼
clean_data()

      │
      ▼
train_model()

      │
      ▼
evaluate_model()

      │
      ▼
save_results()
```

Each function performs one specific task, making the entire system easier to understand and maintain.

---

## 🌍 Real-World Applications

Professional function design is essential in:

- Backend APIs
- Banking systems
- Web applications
- Cloud services
- Automation
- AI pipelines
- Data engineering

Large software systems rely on well-designed functions to remain maintainable over time.

---

## 🤖 AI Connection

AI and Machine Learning projects often consist of many small functions.

Example:

```python
dataset = load_data()

dataset = preprocess_data(dataset)

model = train_model(dataset)

accuracy = evaluate_model(model)

save_model(model)
```

Each function has a single responsibility, making experiments easier to modify and debug.

---

## 💼 Best Practices Checklist

- Give functions meaningful names.
- Follow `snake_case`.
- Keep functions short and focused.
- Follow the Single Responsibility Principle.
- Return values instead of printing whenever appropriate.
- Use parameters instead of global variables.
- Write docstrings for reusable functions.
- Add type hints where helpful.
- Prefer pure functions when possible.
- Avoid unnecessary side effects.

---

## ⚠️ Common Mistakes

### Generic Function Names

```python
def test():
    pass
```

Better:

```python
def calculate_discount():
    pass
```

---

### Very Long Functions

A function with hundreds of lines usually performs too many tasks.

Break it into smaller reusable functions.

---

### Too Many Parameters

Instead of:

```python
def create_user(name, age, city, email, phone, country, language):
    pass
```

Consider grouping related information into a dictionary, dataclass, or object as your programs become more advanced.

---

### Missing Documentation

Complex functions should include a docstring explaining:

- Purpose
- Parameters
- Return value

---

## 📝 Interview Insight

### Question

What makes a good function?

### Answer

A good function:

- Has a clear purpose.
- Performs one task.
- Uses meaningful names.
- Is easy to read.
- Is easy to test.
- Avoids unnecessary side effects.
- Returns useful values.
- Can be reused.

---

## 💡 Remember This

```
Good Function

↓

One Responsibility

↓

Meaningful Name

↓

Reusable

↓

Readable

↓

Testable
```

Think:

> **"Small, focused, and reusable."**

---

## 🎯 Key Takeaways

- Good function design improves readability and maintainability.
- Follow the Single Responsibility Principle.
- Use descriptive names and `snake_case`.
- Return values instead of printing whenever appropriate.
- Use docstrings and type hints for clarity.
- Prefer pure functions and minimize side effects.
- Professional Python code is built from many small, reusable functions.

---

## 💻 Code Reference

`code/functions.py`

