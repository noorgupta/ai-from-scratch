# Input and Output

## 📖 Overview

Every program interacts with data. Sometimes it needs to receive information from the user, and sometimes it needs to display information back to the user.

In Python, this interaction is mainly performed using two built-in functions:

- `input()` → Receives data from the user.
- `print()` → Displays data to the user.

Together, they form the foundation of user interaction in Python.

---

## ❓ Why Do We Need Input and Output?

Imagine an ATM machine.

- It asks you to enter your PIN.
- You enter the PIN.
- The ATM displays your account details or an error message.

This is an example of input and output.

Almost every software application communicates with users in this way.

---

# Output

## 🧠 What is `print()`?

The `print()` function is used to display information on the screen.

### Syntax

```python
print(object)
```

---

### Example

```python
print("Hello, World!")
```

**Output**

```text
Hello, World!
```

---

### Printing Multiple Values

```python
name = "Noor"
age = 20

print(name, age)
```

**Output**

```text
Noor 20
```

Python automatically separates multiple values with a space.

---

### The `sep` Parameter

The `sep` parameter changes the separator between multiple values.

```python
print("Python", "AI", "ML", sep=" | ")
```

**Output**

```text
Python | AI | ML
```

---

### The `end` Parameter

By default, `print()` moves to the next line after printing.

The `end` parameter changes this behavior.

```python
print("Hello", end=" ")
print("World")
```

**Output**

```text
Hello World
```

---

# Input

## 🧠 What is `input()`?

The `input()` function allows a program to receive data from the user during execution.

### Syntax

```python
input("Message")
```

---

### Example

```python
name = input("Enter your name: ")

print(name)
```

If the user enters:

```text
Noor
```

Output:

```text
Noor
```

---

## ⚙️ How `input()` Works

When Python executes:

```python
name = input("Enter your name: ")
```

It:

1. Displays the message.
2. Waits for the user's input.
3. Stores the entered value.
4. Returns the value as a **string**.

---

## ⚠️ Very Important

`input()` **always returns a string**, regardless of what the user enters.

Example:

```python
age = input("Enter age: ")

print(type(age))
```

If the user enters:

```text
20
```

Output:

```text
<class 'str'>
```

To use it as a number:

```python
age = int(input("Enter age: "))
```

---

## 🌍 Real-World Applications

Input and output are used in:

- Login systems
- Registration forms
- Banking applications
- Online shopping
- Games
- Surveys
- Chatbots

---

## 🤖 AI Connection

Every AI application interacts with users through input and output.

Examples:

- ChatGPT receives your prompt using input.
- It generates a response as output.
- Voice assistants receive speech as input and return spoken responses as output.
- AI image generators receive prompts as input and generate images as output.

---

## ⚠️ Common Mistakes

### Assuming `input()` returns an integer

```python
age = input("Enter age: ")
```

Wrong:

```python
print(age + 5)
```

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

---

### Forgetting quotation marks

```python
print(Hello)
```

Python looks for a variable named `Hello`.

Correct:

```python
print("Hello")
```

---

## 💡 Remember This

- `print()` displays information.
- `input()` receives information.
- `input()` always returns a string.
- Convert user input when numerical calculations are required.

---

## 🎯 Key Takeaways

- `print()` is used for output.
- `input()` is used for user input.
- These two functions enable interaction between users and programs.
- Understanding input and output is essential before learning decision making, loops, and real-world application development.

---

## 💻 Code Reference

```text
code/06-input-output.py
```