# `while` Loop

## 📖 Overview

A `while` loop repeatedly executes a block of code **as long as a specified condition remains `True`**.

Unlike a `for` loop, a `while` loop is generally used when the number of iterations is **not known in advance**.

---

## ❓ Why Do We Need a `while` Loop?

Some tasks continue until a condition changes.

Examples include:

- Waiting for a user to enter the correct password.
- Running a game until the player quits.
- Reading data until the end of a file.
- Continuously monitoring a sensor.

In such cases, we cannot determine beforehand how many times the loop should execute.

---

## 🧠 Syntax

```python
while condition:
    # code to execute
```

---

## 💻 Examples

### Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

**Output**

```text
1
2
3
4
5
```

---

### User Input Example

```python
password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted!")
```

The loop continues until the correct password is entered.

---

## ⚙️ How It Works

Python follows these steps:

1. Evaluate the condition.
2. If the condition is `True`, execute the loop body.
3. Return to the condition.
4. Repeat until the condition becomes `False`.

Once the condition is `False`, the loop stops.

---

## 🌍 Real-World Applications

`while` loops are commonly used in:

- Login systems
- ATM machines
- Games
- Menu-driven programs
- Background services
- Data streaming

---

## 🤖 AI Connection

`while` loops are useful in AI for:

- Running a process until a stopping condition is met.
- Monitoring incoming data streams.
- Processing live sensor data.
- Waiting for user interaction in AI applications.

---

## ⚠️ Common Mistakes

### Forgetting to update the condition

```python
count = 1

while count <= 5:
    print(count)
```

This creates an **infinite loop** because `count` never changes.

Correct:

```python
count += 1
```

---

### Incorrect indentation

```python
while count <= 5:
print(count)
```

Always indent the loop body.

---

## 💡 Remember This

- `while` continues as long as the condition is `True`.
- It is useful when the number of iterations is unknown.
- Always ensure the condition eventually becomes `False`.

---

## 🎯 Key Takeaways

- `while` loops execute based on a condition.
- They stop automatically when the condition becomes `False`.
- They are ideal for condition-driven repetition rather than fixed iterations.
- Be careful to avoid infinite loops.

---

## 💻 Code Reference

`code/03-while-loop.py`