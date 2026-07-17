# Parameters and Arguments

## 📖 Overview

Functions become truly useful when they can work with different pieces of data.

Instead of writing separate functions for every possible input, we can pass data to a function. This makes functions flexible, reusable, and scalable.

The values passed to a function are called **arguments**, while the variables that receive those values are called **parameters**.

Understanding parameters and arguments is essential because almost every Python program uses them.

---

## ❓ Why Do We Need Parameters?

Consider a function that greets a user.

Without parameters:

```python
def greet():
    print("Hello, Noor!")

greet()
```

This function always greets the same person.

What if we want to greet different people?

```python
def greet(name):
    print("Hello,", name)

greet("Noor")
greet("Aman")
greet("Priya")
```

**Output**

```text
Hello, Noor
Hello, Aman
Hello, Priya
```

The same function now works for any name.

---

# 🧠 Parameters vs Arguments

Although often used interchangeably, they have different meanings.

### Parameter

A **parameter** is a variable listed in the function definition.

```python
def greet(name):
```

Here, `name` is a **parameter**.

---

### Argument

An **argument** is the actual value passed to the function.

```python
greet("Noor")
```

Here, `"Noor"` is an **argument**.

---

### Easy Way to Remember

```text
Function Definition
        │
        ▼
Parameters

Function Call
        │
        ▼
Arguments
```

---

# 🧠 Positional Arguments

Arguments are assigned to parameters based on their position.

```python
def introduce(name, age):
    print(name)
    print(age)

introduce("Noor", 21)
```

**Output**

```text
Noor
21
```

The first argument goes to the first parameter, and the second argument goes to the second parameter.

---

# 🧠 Keyword Arguments

Instead of relying on position, you can specify parameter names.

```python
def introduce(name, age):
    print(name)
    print(age)

introduce(age=21, name="Noor")
```

**Output**

```text
Noor
21
```

Keyword arguments improve readability and allow arguments to be passed in any order.

---

# 🧠 Default Parameters

A parameter can have a default value.

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()

greet("Noor")
```

**Output**

```text
Hello, Guest
Hello, Noor
```

If no argument is provided, the default value is used.

---

# 🧠 Multiple Parameters

Functions can receive multiple values.

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student("Noor", 21, "BCA")
```

---

# 🧠 Variable-Length Arguments (`*args`)

Sometimes you don't know how many arguments will be passed.

Use `*args`.

```python
def total(*numbers):
    print(numbers)

total(10, 20)
total(1, 2, 3, 4, 5)
```

**Output**

```text
(10, 20)

(1, 2, 3, 4, 5)
```

`*args` collects all extra positional arguments into a tuple.

Example:

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
```

**Output**

```text
60
```

---

# 🧠 Variable-Length Keyword Arguments (`**kwargs`)

Sometimes you don't know which keyword arguments will be passed.

Use `**kwargs`.

```python
def profile(**details):
    print(details)

profile(name="Noor", age=21)
```

**Output**

```text
{'name': 'Noor', 'age': 21}
```

`**kwargs` collects keyword arguments into a dictionary.

---

# 🧠 Packing and Unpacking

Packing groups multiple values into a single object.

```python
def add(*numbers):
    print(numbers)

add(1, 2, 3)
```

Output:

```text
(1, 2, 3)
```

---

Unpacking does the opposite.

```python
numbers = [10, 20]

def add(a, b):
    print(a + b)

add(*numbers)
```

**Output**

```text
30
```

Dictionary unpacking:

```python
student = {
    "name": "Noor",
    "age": 21
}

def introduce(name, age):
    print(name, age)

introduce(**student)
```

**Output**

```text
Noor 21
```

---

## ⚙️ Argument Order Rules

Python follows this order when defining parameters:

```python
def example(
    positional,
    default_value="Python",
    *args,
    **kwargs
):
    pass
```

This order must be maintained.

---

## ⚙️ Behind the Scenes

When you call:

```python
greet("Noor")
```

Python:

1. Creates a new local namespace.
2. Assigns `"Noor"` to the parameter `name`.
3. Executes the function body.
4. Destroys the local namespace after execution.

Conceptually:

```text
Function Call
      │
      ▼
Argument
      │
      ▼
Parameter
      │
      ▼
Function Body
      │
      ▼
Execution Complete
```

---

## 🌍 Real-World Applications

Parameters are used in:

- Login systems
- Search functionality
- Database queries
- API endpoints
- Payment gateways
- Report generation
- Data processing

Almost every reusable function accepts parameters.

---

## 🤖 AI Connection

AI and Machine Learning libraries rely heavily on parameters.

Examples:

```python
train_model(
    learning_rate=0.01,
    epochs=100,
    batch_size=32
)
```

```python
predict(image)
```

```python
load_dataset(path)
```

Frameworks like **TensorFlow**, **PyTorch**, and **Scikit-learn** expose most configuration through function parameters.

---

## 💼 Best Practices

- Use meaningful parameter names.
- Keep the number of parameters reasonable.
- Prefer keyword arguments for readability when there are many optional values.
- Use default values for optional parameters.
- Use `*args` and `**kwargs` only when flexibility is required.

---

## ⚠️ Common Mistakes

### Confusing Parameters and Arguments

```python
def greet(name):
    pass
```

`name` is a parameter.

```python
greet("Noor")
```

`"Noor"` is an argument.

---

### Incorrect Argument Order

Incorrect:

```python
introduce(age=21, "Noor")
```

Raises:

```text
SyntaxError
```

Correct:

```python
introduce("Noor", age=21)
```

or

```python
introduce(name="Noor", age=21)
```

---

### Mutable Default Arguments

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same list is reused across function calls.

Better:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

This creates a new list for each call.

---

## 📝 Interview Insight

### Question

What is the difference between `*args` and `**kwargs`?

### Answer

- `*args` collects extra **positional arguments** into a **tuple**.
- `**kwargs` collects extra **keyword arguments** into a **dictionary**.

---

## 💡 Remember This

| Concept | Meaning |
|---------|---------|
| Parameter | Variable in the function definition |
| Argument | Actual value passed during the function call |
| Positional Argument | Matched by position |
| Keyword Argument | Matched by parameter name |
| Default Parameter | Used when no argument is provided |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dictionary |

---

## 🎯 Key Takeaways

- Parameters receive data inside a function.
- Arguments provide data when calling a function.
- Positional arguments depend on order.
- Keyword arguments improve readability.
- Default parameters make functions more flexible.
- `*args` and `**kwargs` allow functions to accept a variable number of arguments.
- Packing and unpacking simplify working with collections.

---

## 💻 Code Reference

`code/functions.py`