# The `type()` Function

## 📖 Overview

Python provides the built-in `type()` function to identify the data type of a value or variable.

It is one of the most useful functions for beginners because it helps verify whether Python is interpreting data as expected.

---

## ❓ Why Do We Need `type()`?

Sometimes two values may look similar but actually belong to different data types.

For example:

```python
20
"20"
```

Although they appear similar, Python treats them differently.

The `type()` function helps us identify the actual data type.

---

## 🧠 Syntax

```python
type(object)
```

The function accepts a value or variable and returns its data type.

---

## 💻 Examples

### Integer

```python
age = 20

print(type(age))
```

**Output**

```text
<class 'int'>
```

---

### Float

```python
price = 99.99

print(type(price))
```

**Output**

```text
<class 'float'>
```

---

### String

```python
name = "Noor"

print(type(name))
```

**Output**

```text
<class 'str'>
```

---

### Boolean

```python
is_student = True

print(type(is_student))
```

**Output**

```text
<class 'bool'>
```

---

## ⚙️ Internal Working

When Python executes:

```python
type(age)
```

it checks the object that `age` refers to and returns the class (data type) of that object.

For example:

```python
age = 20
```

Memory:

```text
age ─────► 20 (Integer Object)
```

Python inspects the object and returns:

```text
<class 'int'>
```

---

## 🌍 Real-World Applications

Developers use `type()` to:

- Debug programs
- Verify user input
- Check API responses
- Validate data before processing
- Understand unfamiliar code

---

## 🤖 AI Connection

In AI and Machine Learning, data often comes from files, APIs, databases, or users.

Before processing the data, developers frequently verify its type to avoid errors during training or prediction.

For example:

- Ensuring age is an integer.
- Ensuring price is a float.
- Ensuring user input is a string.

Checking data types early helps prevent bugs in AI pipelines.

---

## ⚠️ Common Mistakes

### Assuming `input()` returns an integer

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

`input()` always returns a string.

---

### Confusing values with data types

```python
print(type("25"))
```

Output:

```text
<class 'str'>
```

Even though `"25"` looks like a number, it is still a string because it is enclosed in quotation marks.

---

## 💡 Remember This

- `type()` tells you the data type of a value or variable.
- It is commonly used for debugging and learning.
- Always verify data types when working with user input.

---

## 🎯 Key Takeaways

- `type()` is a built-in Python function.
- It returns the data type of an object.
- It helps developers write accurate and error-free programs.
- It is especially useful when working with unknown or external data.

---

## 💻 Code Reference

```text
code/05-type-function.py
```