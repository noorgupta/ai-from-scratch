# Accessing Elements in Dictionaries

## 📖 Overview

Unlike lists and tuples, dictionaries do not use numerical indexes to access data.

Instead, values are retrieved using their corresponding **keys**.

Python provides multiple ways to access dictionary values, each suitable for different situations.

---

## ❓ Why Access Data Using Keys?

Consider a student record.

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

Instead of remembering positions like:

```python
student[2]
```

you can directly access the required information.

```python
student["course"]
```

**Output**

```text
BCA
```

Using descriptive keys makes programs easier to understand and maintain.

---

# 🧠 Method 1: Using Square Brackets `[]`

The most direct way to access a value is by using its key.

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
```

**Output**

```text
Noor
```

---

## ⚠️ Missing Keys

If the key does not exist:

```python
print(student["cgpa"])
```

Python raises:

```text
KeyError
```

Because `"cgpa"` is not present in the dictionary.

---

# 🧠 Method 2: Using `get()`

The `get()` method safely retrieves a value.

```python
print(student.get("course"))
```

**Output**

```text
BCA
```

If the key does not exist:

```python
print(student.get("cgpa"))
```

**Output**

```python
None
```

Instead of raising an error, `get()` returns `None`.

---

# 🧠 Providing a Default Value

You can specify a default value if the key is missing.

```python
print(student.get("cgpa", "Not Available"))
```

**Output**

```text
Not Available
```

This is especially useful when working with optional data.

---

# 🧠 Membership Testing

Sometimes you only need to know whether a key exists.

Use the `in` operator.

```python
print("name" in student)
```

**Output**

```text
True
```

Example:

```python
print("salary" in student)
```

**Output**

```text
False
```

The `in` operator checks only the **keys**, not the values.

---

# 🧠 Accessing Nested Dictionaries

Dictionaries can contain other dictionaries.

```python
student = {
    "name": "Noor",
    "marks": {
        "Python": 95,
        "AI": 91
    }
}
```

Access nested values step by step.

```python
print(student["marks"]["Python"])
```

**Output**

```text
95
```

Python first retrieves the `"marks"` dictionary and then accesses the `"Python"` key within it.

---

## ⚙️ Behind the Scenes

When Python executes:

```python
student["name"]
```

It performs these steps:

```
"name"
   │
   ▼
Hash Function
   │
   ▼
Hash Value
   │
   ▼
Memory Location
   │
   ▼
"Noor"
```

Python does **not** search every key one by one.

Instead, it uses hashing to locate the value efficiently.

This is why dictionary lookups are generally very fast.

---

## 🌍 Real-World Applications

Accessing dictionary values is common in:

- Reading JSON responses from APIs.
- Processing user profiles.
- Configuration files.
- Product information.
- Database records.

---

## 🤖 AI Connection

Dictionary access is fundamental in AI and Machine Learning.

Examples include:

- Retrieving model parameters.
- Looking up token IDs.
- Accessing feature values.
- Reading prediction outputs.
- Loading configuration settings.

Fast dictionary lookups improve the efficiency of AI applications handling large amounts of data.

---

## 💼 Best Practices

- Use `[]` when you are certain the key exists.
- Use `get()` when the key may be missing.
- Provide a default value with `get()` when appropriate.
- Use descriptive keys to improve readability.

---

## ⚠️ Common Mistakes

### Accessing a Missing Key

```python
student["cgpa"]
```

Raises:

```text
KeyError
```

Use:

```python
student.get("cgpa")
```

instead.

---

### Confusing Keys with Values

```python
print("Noor" in student)
```

**Output**

```text
False
```

`in` checks keys, not values.

Correct:

```python
print("name" in student)
```

**Output**

```text
True
```

---

### Assuming Nested Data Can Be Accessed Directly

Incorrect:

```python
student["Python"]
```

Correct:

```python
student["marks"]["Python"]
```

You must access each level separately.

---

## 📝 Interview Insight

### Question

What is the difference between `[]` and `get()` when accessing dictionary values?

### Answer

- `[]` raises a `KeyError` if the key is missing.
- `get()` returns `None` or a specified default value instead of raising an error.

Use `get()` when missing keys are expected or acceptable.

---

## 💡 Remember This

| Method | Behavior |
|---------|----------|
| `dict[key]` | Returns the value or raises `KeyError` |
| `dict.get(key)` | Returns the value or `None` |
| `dict.get(key, default)` | Returns the value or the specified default |
| `key in dict` | Checks whether the key exists |

---

## 🎯 Key Takeaways

- Dictionary values are accessed using keys, not indexes.
- `[]` is suitable when the key is guaranteed to exist.
- `get()` provides a safer way to retrieve optional values.
- The `in` operator checks for key existence efficiently.
- Nested dictionaries are accessed one level at a time.
- Dictionary lookups are typically **O(1)** on average because of hashing.

---

## 💻 Code Reference

`code/dictionaries.py`