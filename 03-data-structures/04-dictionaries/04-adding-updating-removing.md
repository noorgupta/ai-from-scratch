# Adding, Updating, and Removing Elements

## 📖 Overview

Dictionaries are **mutable**, which means you can add new key-value pairs, modify existing values, and remove entries after the dictionary has been created.

Python provides several built-in operations and methods to perform these tasks efficiently.

---

## ❓ Why Are These Operations Important?

Data changes continuously in real-world applications.

For example:

- A new user registers.
- A customer's address changes.
- A product goes out of stock.
- A student's marks are updated.
- An API response needs modification before processing.

Dictionaries make these operations simple and efficient.

---

# 🧠 Adding New Key-Value Pairs

If the key does not already exist, assigning a value creates a new entry.

```python
student = {
    "name": "Noor",
    "age": 21
}

student["course"] = "BCA"

print(student)
```

**Output**

```python
{
    'name': 'Noor',
    'age': 21,
    'course': 'BCA'
}
```

Python automatically adds the new key-value pair.

---

# 🧠 Updating Existing Values

If the key already exists, assigning a new value updates it.

```python
student["age"] = 22

print(student)
```

**Output**

```python
{
    'name': 'Noor',
    'age': 22,
    'course': 'BCA'
}
```

The existing value is replaced.

---

# 🧠 Updating Multiple Values with `update()`

The `update()` method adds new key-value pairs and updates existing ones.

```python
student.update({
    "age": 23,
    "city": "Lucknow"
})

print(student)
```

**Output**

```python
{
    'name': 'Noor',
    'age': 23,
    'course': 'BCA',
    'city': 'Lucknow'
}
```

- Existing keys are updated.
- New keys are added automatically.

---

# 🧠 Removing with `pop()`

`pop()` removes a key and returns its value.

```python
age = student.pop("age")

print(age)
print(student)
```

**Output**

```text
23

{
    'name': 'Noor',
    'course': 'BCA',
    'city': 'Lucknow'
}
```

If the key does not exist:

```python
student.pop("cgpa")
```

Raises

```text
KeyError
```

---

# 🧠 Providing a Default with `pop()`

You can avoid errors by providing a default value.

```python
student.pop("cgpa", "Not Found")
```

**Output**

```text
Not Found
```

---

# 🧠 Removing the Last Inserted Item with `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}

print(student.popitem())
```

**Output**

```python
('course', 'BCA')
```

After removal:

```python
{
    'name': 'Noor',
    'age': 21
}
```

> **Note:** Since Python 3.7+, dictionaries preserve insertion order, so `popitem()` removes the most recently added entry.

---

# 🧠 Removing with `del`

The `del` statement removes a specific key.

```python
del student["age"]

print(student)
```

**Output**

```python
{
    'name': 'Noor',
    'course': 'BCA'
}
```

If the key does not exist:

```python
del student["cgpa"]
```

Raises

```text
KeyError
```

---

# 🧠 Clearing the Dictionary

The `clear()` method removes every key-value pair.

```python
student.clear()

print(student)
```

**Output**

```python
{}
```

The dictionary still exists—it is simply empty.

---

## ⚙️ Summary

| Operation | Purpose |
|-----------|---------|
| `dict[key] = value` | Add or update a single key-value pair |
| `update()` | Add or update multiple key-value pairs |
| `pop(key)` | Remove a key and return its value |
| `pop(key, default)` | Remove safely with a default value |
| `popitem()` | Remove and return the last inserted key-value pair |
| `del` | Remove a specific key |
| `clear()` | Remove all entries |

---

## 🌍 Real-World Applications

These operations are commonly used in:

- Updating user profiles.
- Editing configuration files.
- Processing API responses.
- Managing shopping carts.
- Modifying database records.

---

## 🤖 AI Connection

Dictionary updates are common in AI workflows.

Examples include:

- Updating model parameters.
- Recording training metrics.
- Modifying feature dictionaries.
- Tracking experiment results.
- Storing prediction outputs.

---

## 💼 Best Practices

- Use assignment (`dict[key] = value`) for adding or updating one item.
- Use `update()` when changing multiple items.
- Use `pop()` when you need the removed value.
- Use `del` when you simply want to delete a key.
- Use `clear()` only when you want to empty the entire dictionary.

---

## ⚠️ Common Mistakes

### Expecting `pop()` to Work on Missing Keys

```python
student.pop("cgpa")
```

Raises

```text
KeyError
```

Safer:

```python
student.pop("cgpa", None)
```

---

### Confusing `pop()` and `del`

```python
value = student.pop("age")
```

Returns the removed value.

```python
del student["age"]
```

Simply deletes the key.

---

### Assuming `update()` Only Updates

```python
student.update({"city": "Lucknow"})
```

If `"city"` doesn't exist, it is **added**, not ignored.

---

## 📝 Interview Insight

### Question

What is the difference between `pop()` and `del`?

### Answer

- `pop()` removes a key **and returns its value**.
- `del` removes a key without returning anything.

Use `pop()` when you need the removed data; use `del` when you only need to delete the entry.

---

## 💡 Remember This

- `dict[key] = value` → Add or update one item
- `update()` → Add or update multiple items
- `pop()` → Remove and return value
- `popitem()` → Remove the last inserted pair
- `del` → Delete a specific key
- `clear()` → Empty the dictionary

---

## 🎯 Key Takeaways

- Dictionaries are mutable and easy to modify.
- Python provides multiple ways to add, update, and remove data.
- Choosing the right operation improves readability and efficiency.
- These operations are essential for backend development, API handling, and AI applications.

---

## 💻 Code Reference

`code/dictionaries.py`