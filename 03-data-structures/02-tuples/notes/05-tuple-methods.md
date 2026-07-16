# Tuple Methods

## 📖 Overview

Unlike lists, tuples provide only **two built-in methods**:

- `count()`
- `index()`

Since tuples are immutable, they do not include methods for adding, removing, or modifying elements.

---

## ❓ Why Do Tuples Have Only Two Methods?

Lists are mutable, so Python provides methods to modify their contents.

Examples include:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`

Tuples, however, cannot be modified after creation.

As a result, Python only provides methods that **retrieve information** without changing the tuple.

---

# 🧠 `count()`

## What is `count()`?

The `count()` method returns the number of times a specified value appears in a tuple.

### Syntax

```python
tuple.count(value)
```

### Example

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

**Output**

```text
3
```

---

# 🧠 `index()`

## What is `index()`?

The `index()` method returns the index of the **first occurrence** of a specified value.

### Syntax

```python
tuple.index(value)
```

### Example

```python
fruits = ("Apple", "Banana", "Mango", "Banana")

print(fruits.index("Banana"))
```

**Output**

```text
1
```

Even though `"Banana"` appears twice, only the first occurrence is returned.

---

## ⚙️ Summary

| Method | Purpose | Returns |
|---------|----------|---------|
| `count()` | Counts occurrences | Integer |
| `index()` | Finds first occurrence | Integer |

---

## 🌍 Real-World Applications

Tuple methods are useful for:

- Counting repeated values.
- Searching configuration settings.
- Validating coordinates.
- Processing fixed datasets.

---

## 🤖 AI Connection

Tuple methods are used in AI when working with fixed metadata.

Examples include:

- Counting labels.
- Searching tensor dimensions.
- Finding the position of configuration values.
- Processing model output shapes.

---

## 💼 Best Practices

- Use `count()` to analyze frequency.
- Use `index()` only when you know the value exists.
- If the value may not exist, check first using the `in` operator.

Example:

```python
if "Banana" in fruits:
    print(fruits.index("Banana"))
```

---

## ⚠️ Common Mistakes

### Searching for a value that doesn't exist

```python
fruits = ("Apple", "Banana")

fruits.index("Orange")
```

Raises:

```text
ValueError
```

---

### Expecting `index()` to return all matches

```python
numbers = (5, 10, 5, 20)

numbers.index(5)
```

Output:

```text
0
```

Only the **first occurrence** is returned.

---

## 📝 Interview Insight

**Question:**

Why do tuples have only two built-in methods?

**Answer:**

Because tuples are immutable.

Python only provides methods that retrieve information (`count()` and `index()`), while modification methods are unnecessary.

---

## 💡 Remember This

- Tuples have only two methods.
- `count()` counts occurrences.
- `index()` returns the first occurrence.
- Neither method modifies the tuple.

---

## 🎯 Key Takeaways

- Tuple methods are read-only operations.
- They support searching and counting.
- Their limited functionality is a direct result of tuple immutability.

---

## 💻 Code Reference

`code/tuples.py`