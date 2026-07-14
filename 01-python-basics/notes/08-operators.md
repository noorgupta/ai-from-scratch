# Operators

## 📖 Overview

Operators are special symbols that perform operations on values and variables. They allow Python to perform calculations, compare values, assign data, and evaluate logical conditions.

---

## ❓ Why Do We Need Operators?

Imagine writing a program without operators.

You wouldn't be able to:

- Add two numbers.
- Compare two values.
- Check if a user is eligible.
- Update variable values.
- Combine multiple conditions.

Operators make programming possible by enabling computation and decision-making.

---

## 🧠 Types of Operators

### 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus (Remainder) | `10 % 3` |
| `**` | Exponent | `2 ** 3` |

---

### 2. Comparison Operators

Used to compare values.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or Equal to |
| `<=` | Less than or Equal to |

These operators always return `True` or `False`.

---

### 3. Logical Operators

Used to combine multiple conditions.

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the Boolean value |

---

### 4. Assignment Operators

Used to assign or update values.

Examples:

```python
x = 10
x += 5
x -= 2
x *= 3
x /= 2
```

---

### 5. Membership Operators

Used to check whether a value exists in a sequence.

```python
"AI" in "AI From Scratch"

5 in [1, 2, 3, 4, 5]
```

Operators:

- `in`
- `not in`

---

### 6. Identity Operators

Used to check whether two variables refer to the same object in memory.

Operators:

- `is`
- `is not`

Example:

```python
x = [1, 2]
y = x

print(x is y)
```

---

## 🌍 Real-World Applications

Operators are used in:

- Banking systems
- Login validation
- Shopping carts
- Data analysis
- Games
- Scientific calculations

---

## 🤖 AI Connection

Operators are used throughout AI development.

Examples:

- Calculating loss values.
- Updating model weights.
- Comparing predictions.
- Checking training conditions.
- Processing datasets.
- Applying mathematical formulas.

Without operators, AI algorithms cannot perform computations or make decisions.

---

## ⚠️ Common Mistakes

- Confusing `=` (assignment) with `==` (comparison).
- Using `/` instead of `//`.
- Forgetting operator precedence.
- Misusing `is` instead of `==`.

---

## 💡 Remember This

- Operators perform actions on data.
- Different operators serve different purposes.
- Comparison operators return Boolean values.
- Logical operators are heavily used in decision making.

---

## 🎯 Key Takeaways

- Operators are essential for calculations, comparisons, and logical decisions.
- Python provides Arithmetic, Comparison, Logical, Assignment, Membership, and Identity operators.
- They are used extensively in AI, Machine Learning, and general software development.

---

## 💻 Code Reference

```text
code/08-operators.py
```