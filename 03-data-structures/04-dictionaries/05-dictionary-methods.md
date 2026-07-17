# Dictionary Methods

## 📖 Overview

Python provides several built-in methods that make working with dictionaries easier and more efficient.

These methods allow you to:

- Access keys and values
- Iterate over dictionary contents
- Copy dictionaries
- Provide default values
- Create new dictionaries efficiently

Understanding these methods is essential for writing clean, readable, and professional Python code.

---

## ❓ Why Learn Dictionary Methods?

Consider a student dictionary.

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

Sometimes you need:

- Only the keys
- Only the values
- Both keys and values
- A safe default value
- A copy of the dictionary

Python provides methods for all these situations.

---

# 🧠 `keys()`

Returns a view containing all dictionary keys.

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}

print(student.keys())
```

**Output**

```python
dict_keys(['name', 'age', 'course'])
```

Useful when you only need the keys.

---

# 🧠 `values()`

Returns all values.

```python
print(student.values())
```

**Output**

```python
dict_values(['Noor', 21, 'BCA'])
```

Useful for calculations, validation, and reporting.

---

# 🧠 `items()`

Returns both keys and values together as tuples.

```python
print(student.items())
```

**Output**

```python
dict_items([
    ('name', 'Noor'),
    ('age', 21),
    ('course', 'BCA')
])
```

This is the preferred method when iterating over dictionaries.

---

# 🧠 `copy()`

Creates a shallow copy of the dictionary.

```python
student_copy = student.copy()

print(student_copy)
```

**Output**

```python
{
    'name': 'Noor',
    'age': 21,
    'course': 'BCA'
}
```

Changing the copied dictionary does not affect the original for top-level values.

---

# 🧠 `setdefault()`

Returns the value for a key.

If the key does not exist, it inserts the key with the specified default value.

```python
student.setdefault("city", "Lucknow")

print(student)
```

**Output**

```python
{
    'name': 'Noor',
    'age': 21,
    'course': 'BCA',
    'city': 'Lucknow'
}
```

If the key already exists:

```python
student.setdefault("name", "Rahul")
```

Nothing changes.

---

# 🧠 `fromkeys()`

Creates a new dictionary using a sequence of keys.

```python
subjects = ["Python", "AI", "Math"]

marks = dict.fromkeys(subjects, 0)

print(marks)
```

**Output**

```python
{
    'Python': 0,
    'AI': 0,
    'Math': 0
}
```

Useful for initializing counters or placeholders.

---

## ⚙️ Summary

| Method | Purpose |
|---------|---------|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `copy()` | Creates a shallow copy |
| `setdefault()` | Returns value or inserts a default |
| `fromkeys()` | Creates a new dictionary from a sequence of keys |

---

## 🧠 Behind the Scenes

Methods like `keys()`, `values()`, and `items()` return **view objects**, not independent copies.

```python
student = {"name": "Noor"}

keys = student.keys()

student["age"] = 21

print(keys)
```

**Output**

```python
dict_keys(['name', 'age'])
```

The view automatically reflects changes made to the dictionary.

---

## 🌍 Real-World Applications

Dictionary methods are commonly used for:

- Displaying available settings.
- Processing API responses.
- Generating reports.
- Counting frequencies.
- Initializing configuration values.
- Copying user preferences.

---

## 🤖 AI Connection

Dictionary methods are heavily used in AI and Machine Learning.

Examples include:

- Reading model configuration dictionaries.
- Iterating through feature mappings.
- Copying experiment settings.
- Initializing evaluation metrics.
- Creating label dictionaries.

Frameworks like **PyTorch**, **TensorFlow**, and **Hugging Face Transformers** frequently use these methods when working with configuration and metadata.

---

## 💼 Best Practices

- Use `items()` when both keys and values are required.
- Use `keys()` or `values()` only when you specifically need one of them.
- Use `copy()` before modifying a dictionary you want to preserve.
- Use `setdefault()` to avoid manual existence checks.
- Use `fromkeys()` for initializing dictionaries with common default values.

---

## ⚠️ Common Mistakes

### Assuming `copy()` Creates a Deep Copy

```python
student_copy = student.copy()
```

This creates a **shallow copy**.

Nested mutable objects are still shared.

---

### Expecting `setdefault()` to Update Existing Values

```python
student.setdefault("name", "Rahul")
```

If `"name"` already exists, its value remains unchanged.

---

### Modifying a Dictionary While Iterating

```python
for key in student.keys():
    student["city"] = "Lucknow"
```

This may raise a `RuntimeError`.

If you need to modify the dictionary while iterating, iterate over a copy of the keys instead:

```python
for key in list(student.keys()):
    # Safe modifications
    pass
```

---

## 📝 Interview Insight

### Question

What is the difference between `get()` and `setdefault()`?

### Answer

- `get()` returns the value for a key (or a default) **without modifying the dictionary**.
- `setdefault()` returns the value if the key exists; otherwise, it **adds the key with the default value** and returns that value.

---

## 💡 Remember This

| Method | Easy Memory Trick |
|---------|-------------------|
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get both together |
| `copy()` | Duplicate dictionary |
| `setdefault()` | Get or create |
| `fromkeys()` | Build a dictionary from keys |

---

## 🎯 Key Takeaways

- Dictionary methods simplify common tasks and improve code readability.
- View methods (`keys()`, `values()`, `items()`) automatically reflect changes to the dictionary.
- `copy()` creates a shallow copy.
- `setdefault()` combines lookup and initialization.
- These methods are widely used in backend development, automation, data analysis, and AI workflows.

---

## 💻 Code Reference

`code/dictionaries.py`