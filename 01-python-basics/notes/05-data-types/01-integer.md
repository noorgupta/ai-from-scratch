# Integer (`int`)

## 📖 Overview

An **integer** is a whole number that does not contain a decimal point. Integers can be positive, negative, or zero.

Python uses the `int` data type to represent whole numbers.

---

## ❓ Why Do We Need Integers?

Many real-world values are naturally whole numbers.

For example:

- Number of students in a class
- Age of a person
- Total products in a cart
- Number of followers
- Score in a game

Using integers allows Python to perform mathematical operations efficiently on whole numbers.

---

## 🧠 Characteristics

- Stores whole numbers only.
- Can be positive, negative, or zero.
- Has no decimal point.
- Supports all arithmetic operations.

Examples:

```python
10
0
-45
2025
```

---

## ⚙️ Internal Working

When Python encounters an integer:

```python
age = 20
```

It:

1. Creates an integer object.
2. Stores it in memory.
3. Makes the variable `age` refer to that object.

---

## 💻 Examples

```python
age = 20
marks = 95
temperature = -5
students = 60

print(age)
print(type(age))
```

**Output**

```text
20
<class 'int'>
```

---

## 🌍 Real-World Applications

Integers are commonly used to represent:

- User age
- Product quantity
- Employee ID
- Population
- Number of files
- Game score
- OTP values

---

## 🤖 AI Connection

Integers are widely used in AI for storing:

- Class labels (0, 1, 2...)
- Number of training epochs
- Batch size
- Dataset size
- Iteration count
- Token IDs in language models

---

## ⚠️ Common Mistakes

### Using quotation marks

```python
age = "20"
```

This is a **string**, not an integer.

Correct:

```python
age = 20
```

---

### Expecting user input to be an integer

```python
age = input("Enter age: ")
```

`input()` always returns a string.

Use:

```python
age = int(input("Enter age: "))
```

---

## 💡 Remember This

- Integers store whole numbers.
- They do not contain decimal values.
- Do not place integers inside quotation marks.
- Use `type()` to verify the data type.

---

## 🎯 Key Takeaways

- `int` represents whole numbers.
- Integers are one of Python's fundamental data types.
- They are commonly used for counting, indexing, and mathematical calculations.
- Integers play an important role in AI, programming, and software development.

---

## 💻 Code Reference

See:

```text
code/01-integer.py
```