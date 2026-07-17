# Variable Scope

## 📖 Overview

A **variable's scope** defines **where it can be accessed** within a program.

Not every variable is available everywhere.

Some variables exist only inside a function, while others can be accessed throughout the entire program.

Understanding scope helps you:

- Prevent accidental variable modifications.
- Write modular code.
- Avoid naming conflicts.
- Debug programs more easily.

Variable scope is one of the most important concepts in Python because every function creates its own scope.

---

## ❓ Why Do We Need Scope?

Imagine a school.

- A student's notebook belongs only to that student.
- The school timetable is available to everyone.

Variables behave similarly.

Some belong only to a function.

Others belong to the entire program.

Without scope, every variable would interfere with every other variable, making programs difficult to manage.

---

# 🧠 Local Variables

A **local variable** is created inside a function.

It exists only while that function is executing.

Example:

```python
def greet():
    message = "Hello"

    print(message)

greet()
```

**Output**

```text
Hello
```

Trying to access it outside the function:

```python
print(message)
```

Raises:

```text
NameError
```

The variable no longer exists.

---

# 🧠 Global Variables

A **global variable** is defined outside every function.

It can be accessed from anywhere in the program.

```python
course = "Python"

def show_course():
    print(course)

show_course()
```

**Output**

```text
Python
```

The function reads the global variable successfully.

---

# 🧠 Local vs Global Variables

```python
course = "Python"

def demo():

    course = "Machine Learning"

    print(course)

demo()

print(course)
```

**Output**

```text
Machine Learning

Python
```

The local variable hides the global variable inside the function.

This is called **variable shadowing**.

---

# 🧠 Variable Shadowing

A local variable with the same name as a global variable temporarily takes precedence inside the function.

```python
language = "Python"

def display():

    language = "Java"

    print(language)

display()

print(language)
```

**Output**

```text
Java

Python
```

The global variable remains unchanged.

---

# 🧠 The `global` Keyword

Normally, functions can read global variables but cannot modify them directly.

Incorrect:

```python
count = 0

def increase():

    count += 1
```

Raises:

```text
UnboundLocalError
```

Correct:

```python
count = 0

def increase():

    global count

    count += 1

increase()

print(count)
```

**Output**

```text
1
```

The `global` keyword tells Python to use the global variable instead of creating a local one.

---

# 🧠 The LEGB Rule

When Python looks for a variable, it follows this order:

```
L → Local

E → Enclosing

G → Global

B → Built-in
```

---

## 1. Local Scope

Variables inside the current function.

```python
def greet():

    name = "Noor"

    print(name)
```

---

## 2. Enclosing Scope

Variables inside an outer function.

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

Output:

```text
Hello
```

---

## 3. Global Scope

Variables defined outside all functions.

```python
city = "Lucknow"
```

---

## 4. Built-in Scope

Names provided by Python.

Examples:

```python
print()

len()

sum()

max()

type()
```

These are always available unless you overwrite them.

---

# 🧠 The `nonlocal` Keyword

`nonlocal` is used inside **nested functions** to modify a variable from the enclosing function.

```python
def outer():

    count = 0

    def inner():

        nonlocal count

        count += 1

        print(count)

    inner()

outer()
```

**Output**

```text
1
```

`nonlocal` works only with variables in the enclosing (non-global) scope.

---

## ⚙️ Behind the Scenes

Each function call creates a new **local namespace**.

Example:

```python
def greet():

    name = "Noor"
```

Conceptually:

```text
Global Namespace

course

city

greet()

        │

        ▼

Local Namespace

name
```

After the function finishes, its local namespace is destroyed.

The global namespace remains for the lifetime of the program.

---

## 🌍 Real-World Applications

Scope is important in:

- Backend APIs
- Banking software
- Authentication systems
- Data processing
- Web applications
- Automation scripts

Large applications use local variables extensively to avoid conflicts.

---

## 🤖 AI Connection

Scope is widely used in AI and Machine Learning.

Example:

```python
def train_model():

    learning_rate = 0.01

    epochs = 100
```

These variables are local to the training function.

Global variables may store:

- Model configuration
- Dataset paths
- Constants
- Labels

Nested functions using `nonlocal` are common in decorators and callback-based ML utilities.

---

## 💼 Best Practices

- Prefer local variables whenever possible.
- Minimize the use of global variables.
- Use meaningful variable names.
- Avoid modifying global variables inside functions.
- Use `nonlocal` only when nested functions truly need to share state.

---

## ⚠️ Common Mistakes

### Accessing Local Variables Outside Their Scope

Incorrect:

```python
def demo():

    x = 10

print(x)
```

Raises:

```text
NameError
```

---

### Modifying a Global Variable Without `global`

Incorrect:

```python
count = 0

def increment():

    count += 1
```

Raises:

```text
UnboundLocalError
```

Use:

```python
global count
```

---

### Shadowing Built-in Names

Avoid:

```python
list = [1, 2, 3]

print(list)
```

Now you can no longer use Python's built-in `list()` function.

Instead, use descriptive names such as:

```python
numbers = [1, 2, 3]
```

---

## 📝 Interview Insight

### Question

What is the LEGB rule?

### Answer

Python searches for variables in the following order:

1. **Local**
2. **Enclosing**
3. **Global**
4. **Built-in**

Python stops searching as soon as it finds the variable.

---

## 💡 Remember This

| Scope | Description |
|--------|-------------|
| Local | Inside the current function |
| Enclosing | Inside the outer function |
| Global | Outside all functions |
| Built-in | Provided by Python |

Search order:

```
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

---

## 🎯 Key Takeaways

- Scope determines where a variable can be accessed.
- Local variables exist only during a function call.
- Global variables exist throughout the program.
- The `global` keyword allows modification of global variables.
- The `nonlocal` keyword modifies variables in an enclosing function.
- Python follows the **LEGB rule** when resolving variable names.
- Using local variables makes programs safer, cleaner, and easier to maintain.

---

## 💻 Code Reference

`code/functions.py`