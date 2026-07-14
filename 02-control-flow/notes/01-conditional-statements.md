# Conditional Statements (`if`, `elif`, `else`)

## 📖 Overview

Conditional statements allow a program to make decisions based on specific conditions. Instead of executing every line of code, the program evaluates a condition and chooses which block of code to execute.

In Python, conditional statements are implemented using:

- `if`
- `elif`
- `else`

---

## ❓ Why Do We Need Conditional Statements?

Real-world applications constantly make decisions.

For example:

- Should a user be allowed to log in?
- Is a student eligible to take an exam?
- Does a customer have enough balance to complete a purchase?
- Should an AI model classify an email as spam?

Without conditional statements, programs would execute every instruction regardless of the situation, making intelligent decision-making impossible.

---

## 🧠 The `if` Statement

The `if` statement executes a block of code only if its condition evaluates to `True`.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

## 🧠 The `elif` Statement

The `elif` (else if) statement allows Python to check another condition if the previous condition is `False`.

### Syntax

```python
if condition1:
    ...
elif condition2:
    ...
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
```

---

## 🧠 The `else` Statement

The `else` statement executes when none of the previous conditions are `True`.

### Syntax

```python
if condition:
    ...
else:
    ...
```

### Example

```python
age = 15

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## ⚙️ How Python Executes Conditional Statements

Python follows this sequence:

1. Evaluate the `if` condition.
2. If it is `True`, execute the `if` block and skip the remaining conditions.
3. If it is `False`, check the `elif` condition (if present).
4. If an `elif` condition is `True`, execute its block and skip the rest.
5. If no conditions are `True`, execute the `else` block (if present).

Only **one** block executes in an `if-elif-else` chain.

---

## 🌍 Real-World Applications

Conditional statements are used in:

- Login systems
- ATM machines
- Online shopping discounts
- Banking applications
- Access control
- Game development

---

## 🤖 AI Connection

Conditional statements play an important role in AI.

Examples include:

- Deciding whether a prediction is accepted based on confidence.
- Detecting spam emails.
- Classifying images into categories.
- Validating user input before making predictions.
- Choosing different actions based on model output.

---

## ⚠️ Common Mistakes

### Forgetting the colon (`:`)

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

### Incorrect indentation

```python
if age >= 18:
print("Eligible")
```

Correct:

```python
if age >= 18:
    print("Eligible")
```

Python uses indentation to define code blocks.

---

### Using `=` instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## 💡 Remember This

- `if` checks the first condition.
- `elif` checks additional conditions.
- `else` executes when all previous conditions are `False`.
- Only one block executes in an `if-elif-else` chain.

---

## 🎯 Key Takeaways

- Conditional statements enable decision-making in programs.
- Python uses `if`, `elif`, and `else` for branching.
- Indentation is mandatory.
- Conditional statements are widely used in software development and AI applications.

---

## 💻 Code Reference

```text
code/01-conditional-statements.py
```