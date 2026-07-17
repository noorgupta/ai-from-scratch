# Defining and Calling Functions

## 📖 Overview

After understanding what a function is and why it is useful, the next step is learning how to create and use one.

In Python, functions are created using the `def` keyword.

Once defined, a function can be called (executed) whenever its functionality is needed.

This separation between **definition** and **execution** makes functions reusable and modular.

---

## ❓ Function Syntax

The general syntax of a function is:

```python
def function_name():
    # Function body
```

Components:

- `def` → Keyword used to define a function.
- `function_name` → Name of the function.
- `()` → Parentheses used to receive parameters (if any).
- `:` → Indicates the start of the function body.
- Indented block → The statements executed when the function is called.

---

## 🧠 Defining a Function

Example:

```python
def greet():
    print("Hello, World!")
```

This creates a function named `greet`.

At this point, **nothing is printed** because the function has only been defined.

---

## 🧠 Calling a Function

A function executes only when it is called.

```python
def greet():
    print("Hello, World!")

greet()
```

**Output**

```text
Hello, World!
```

The parentheses `()` tell Python to execute the function.

---

## 🧠 Calling a Function Multiple Times

One of the biggest advantages of functions is reusability.

```python
def greet():
    print("Hello!")

greet()
greet()
greet()
```

**Output**

```text
Hello!
Hello!
Hello!
```

The same function can be called as many times as needed.

---

## 🧠 Execution Flow

Consider:

```python
def greet():
    print("Hello")

print("Start")

greet()

print("End")
```

**Output**

```text
Start
Hello
End
```

Execution order:

```
Program Starts
      │
      ▼
Function Definition
      │
      ▼
print("Start")
      │
      ▼
greet()
      │
      ▼
Function Executes
      │
      ▼
print("End")
```

Python executes statements from top to bottom, except that function bodies are skipped until the function is called.

---

## 🧠 Calling One Function from Another

Functions can call other functions.

```python
def greet():
    print("Hello")

def welcome():
    greet()
    print("Welcome!")
    
welcome()
```

**Output**

```text
Hello
Welcome!
```

This technique helps divide large problems into smaller tasks.

---

## 🧠 Empty Functions

Sometimes you want to create a function that you'll implement later.

Use the `pass` statement.

```python
def future_feature():
    pass
```

This avoids syntax errors while keeping the function definition valid.

---

## ⚙️ Behind the Scenes

When Python reads:

```python
def greet():
    print("Hello")
```

It:

1. Creates a function object.
2. Stores the function in memory.
3. Associates it with the name `greet`.

When Python encounters:

```python
greet()
```

It:

1. Finds the function object.
2. Creates a new execution frame.
3. Executes the statements inside the function.
4. Returns control to the point where the function was called.

Conceptually:

```
Program
   │
   ▼
greet()
   │
   ▼
Function Memory
   │
   ▼
Execute Statements
   │
   ▼
Return to Caller
```

---

## 🌍 Real-World Applications

Defining and calling functions is essential in:

- User login systems
- Payment processing
- Email services
- Data validation
- REST API endpoints
- Automation scripts
- Data analysis pipelines

Every software application is composed of many functions working together.

---

## 🤖 AI Connection

AI and Machine Learning workflows are built using functions.

Examples:

```python
load_data()

clean_data()

train_model()

evaluate_model()

predict()
```

Breaking AI workflows into functions makes code reusable, testable, and easier to debug.

---

## 💼 Best Practices

- Use descriptive function names.
- Keep each function focused on one responsibility.
- Avoid writing very long functions.
- Use lowercase names with underscores (`snake_case`).
- Define functions before calling them.

Example:

```python
def calculate_average():
```

Better than:

```python
def fun():
```

---

## ⚠️ Common Mistakes

### Forgetting Parentheses While Calling

Incorrect

```python
greet
```

Correct

```python
greet()
```

---

### Calling Before Defining

Incorrect

```python
greet()

def greet():
    print("Hello")
```

Raises:

```text
NameError
```

Define the function before calling it.

---

### Missing Indentation

Incorrect

```python
def greet():
print("Hello")
```

Raises:

```text
IndentationError
```

Python requires proper indentation.

---

### Forgetting the Colon

Incorrect

```python
def greet()
```

Correct

```python
def greet():
```

---

## 📝 Interview Insight

### Question

What happens when Python encounters a function definition?

### Answer

Python creates a **function object** and stores it in memory.

The code inside the function is **not executed immediately**.

Execution begins only when the function is called using parentheses.

---

## 💡 Remember This

- `def` defines a function.
- Defining is different from calling.
- Parentheses `()` execute the function.
- Functions can call other functions.
- `pass` creates an empty placeholder function.

---

## 🎯 Key Takeaways

- Functions are created using the `def` keyword.
- A function definition does not execute its code.
- Functions run only when called.
- Functions can be called multiple times.
- Large programs become easier to manage by dividing them into small functions.

---

## 💻 Code Reference

`code/functions.py`