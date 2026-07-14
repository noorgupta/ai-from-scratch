# Boolean (`bool`)

## 📖 Overview

A **Boolean** is a data type that represents one of two possible values:

- `True`
- `False`

Booleans are primarily used to make decisions in a program. Whenever Python evaluates a condition, the result is always a Boolean value.

---

## ❓ Why Do We Need Booleans?

Many real-world situations involve decision making.

For example:

- Is the user logged in?
- Is the payment successful?
- Is the password correct?
- Is the student eligible?
- Has the AI model finished training?

These questions have only two possible answers: **Yes** or **No**, which Python represents as `True` and `False`.

---

## 🧠 Characteristics

- Stores only two values: `True` and `False`.
- Result of comparison and logical operations.
- Used extensively in conditional statements and loops.
- Boolean values are case-sensitive and always begin with a capital letter.

Examples:

```python
True
False
```

---

## ⚙️ Internal Working

When Python evaluates a condition, it returns a Boolean value.

Example:

```python
age = 20

print(age >= 18)
```

Python checks whether the condition is true.

Output:

```text
True
```

This Boolean result is then used to decide which block of code should execute.

---

## 💻 Examples

```python
is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))
```

**Output**

```text
True
<class 'bool'>
```

---

## 🌍 Real-World Applications

Booleans are used in:

- Login systems
- Payment verification
- Access control
- Email verification
- Form validation
- Game logic
- Security checks

---

## 🤖 AI Connection

Boolean values are widely used in Artificial Intelligence.

Examples include:

- Whether model training is complete.
- Whether confidence exceeds a threshold.
- Whether a prediction is correct.
- Whether data preprocessing has finished.
- Whether an object is detected in an image.

Although AI often works with numbers, Boolean values help control the program's decision-making process.

---

## ⚠️ Common Mistakes

### Using quotation marks

```python
status = "True"
```

This is a **string**, not a Boolean.

Correct:

```python
status = True
```

---

### Incorrect capitalization

```python
true
false
```

❌ Invalid in Python.

Correct:

```python
True
False
```

---

## 💡 Remember This

- Boolean values are either `True` or `False`.
- They are used whenever a program needs to make a decision.
- Do not use quotation marks around Boolean values.
- `True` and `"True"` are different data types.

---

## 🎯 Key Takeaways

- `bool` represents logical values.
- It stores only two values: `True` and `False`.
- Booleans are the foundation of decision making in programming.
- They are extensively used in AI, web development, and software applications.

---

## 💻 Code Reference

```text
code/04-boolean.py
```