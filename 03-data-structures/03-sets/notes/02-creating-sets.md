# Creating Sets

## 📖 Overview

Python provides multiple ways to create a set. Regardless of how a set is created, it always stores **unique, hashable elements**.

Understanding the different ways to create sets helps when working with data from files, user input, databases, or AI datasets.

---

## ❓ Why Learn Different Ways to Create Sets?

Data can come from many sources, such as:

- User input
- Lists
- Tuples
- Strings
- Files
- APIs
- Databases

Python provides different ways to convert this data into a set.

---

# 🧠 Method 1: Creating a Set with Values

The most common way is using curly braces `{}`.

```python
numbers = {10, 20, 30, 40}
```

---

# 🧠 Method 2: Creating an Empty Set

Many beginners make this mistake.

❌ Wrong

```python
data = {}
```

This creates a **dictionary**, not a set.

```python
print(type(data))
```

Output

```text
<class 'dict'>
```

✅ Correct

```python
data = set()
```

Output

```python
<class 'set'>
```

---

# 🧠 Method 3: Creating a Set from a List

```python
numbers = [10, 20, 30, 20, 10]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output

```text
{10, 20, 30}
```

Duplicate values are automatically removed.

---

# 🧠 Method 4: Creating a Set from a Tuple

```python
numbers = (1, 2, 2, 3, 3)

unique = set(numbers)

print(unique)
```

Output

```text
{1, 2, 3}
```

---

# 🧠 Method 5: Creating a Set from a String

```python
letters = set("Python")
```

Output

```text
{'P', 'y', 't', 'h', 'o', 'n'}
```

Repeated characters appear only once.

Example:

```python
set("banana")
```

Output

```text
{'b', 'a', 'n'}
```

---

# 🧠 Automatic Removal of Duplicates

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
```

Output

```text
{10, 20, 30}
```

Python automatically keeps only unique values.

---

## ⚙️ How It Works

Suppose Python receives:

```python
{10, 20, 10, 30}
```

Python:

1. Reads `10`.
2. Stores it.
3. Reads `20`.
4. Stores it.
5. Reads another `10`.
6. Detects it already exists.
7. Ignores the duplicate.
8. Stores `30`.

Final set:

```python
{10, 20, 30}
```

---

## 🌍 Real-World Applications

Creating sets is useful for:

- Removing duplicate email addresses.
- Finding unique visitors to a website.
- Extracting unique product IDs.
- Cleaning repeated records.
- Building unique collections.

---

## 🤖 AI Connection

Sets are commonly used before model training to:

- Remove duplicate samples.
- Find unique labels.
- Extract unique words from text.
- Build NLP vocabularies.
- Clean datasets.

---

## 💼 Best Practices

- Use `{}` for non-empty sets.
- Use `set()` for empty sets.
- Convert lists to sets when duplicate values should be removed.

---

## ⚠️ Common Mistakes

### Using `{}` for an Empty Set

```python
data = {}
```

Creates a dictionary.

Correct:

```python
data = set()
```

---

### Expecting Duplicate Values

```python
numbers = {1, 1, 2, 2}
```

Output

```python
{1, 2}
```

Duplicates are removed automatically.

---

### Storing Mutable Objects

```python
data = {[1, 2], [3, 4]}
```

Raises

```text
TypeError
```

Only **hashable** (immutable) objects can be stored in a set.

---

## 📝 Interview Insight

### Question

Why does `{}` create a dictionary instead of a set?

### Answer

Python reserves `{}` for dictionaries.

To create an empty set, you must use:

```python
set()
```

---

## 💡 Remember This

- `{1, 2, 3}` → Set
- `{}` → Dictionary
- `set()` → Empty set
- Duplicate values are removed automatically.

---

## 🎯 Key Takeaways

- Python provides multiple ways to create sets.
- Empty sets must be created using `set()`.
- Sets automatically remove duplicate values.
- Sets can be created from any iterable.

---

## 💻 Code Reference

`code/sets.py`