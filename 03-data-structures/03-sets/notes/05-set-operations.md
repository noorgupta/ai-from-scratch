# Set Operations

## 📖 Overview

One of the biggest advantages of sets is the ability to perform mathematical operations directly.

These operations allow us to compare, combine, and analyze collections of unique data efficiently.

Python provides built-in methods and operators for these operations, making the code simple and highly optimized.

---

## ❓ Why Do We Need Set Operations?

Imagine two online courses.

Course A students:

```text
Alice
Bob
Charlie
```

Course B students:

```text
Bob
Charlie
David
```

Questions you might ask:

- Who is enrolled in **either** course?
- Who is enrolled in **both** courses?
- Who is enrolled only in Course A?
- Who is enrolled in exactly one course?

Set operations answer these questions easily.

---

# 🧠 Union (`|`)

The **Union** of two sets contains **every unique element** from both sets.

### Syntax

```python
set1 | set2
```

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

**Output**

```python
{1, 2, 3, 4, 5}
```

Duplicates appear only once.

---

# 🧠 Intersection (`&`)

The **Intersection** contains only the elements that exist in **both** sets.

### Syntax

```python
set1 & set2
```

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
```

**Output**

```python
{3}
```

---

# 🧠 Difference (`-`)

Difference returns elements that exist in the **first set but not in the second**.

### Syntax

```python
set1 - set2
```

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
```

**Output**

```python
{1, 2}
```

Notice:

```python
print(b - a)
```

Output

```python
{4, 5}
```

Difference is **not symmetric**.

---

# 🧠 Symmetric Difference (`^`)

Returns elements that belong to **exactly one** of the sets.

Common elements are removed.

### Syntax

```python
set1 ^ set2
```

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
```

**Output**

```python
{1, 2, 4, 5}
```

---

# 🧠 Subset

A set is a subset if **every element** exists in another set.

### Syntax

```python
set1.issubset(set2)
```

### Example

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

**Output**

```python
True
```

---

# 🧠 Superset

A superset contains **all elements** of another set.

### Syntax

```python
set1.issuperset(set2)
```

### Example

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))
```

**Output**

```python
True
```

---

# 🧠 Disjoint Sets

Two sets are disjoint if they have **no common elements**.

### Syntax

```python
set1.isdisjoint(set2)
```

### Example

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

**Output**

```python
True
```

---

## ⚙️ Visual Understanding

```
A = {1,2,3}
B = {3,4,5}

Union
{1,2,3,4,5}

Intersection
{3}

Difference (A-B)
{1,2}

Difference (B-A)
{4,5}

Symmetric Difference
{1,2,4,5}
```

---

## 🌍 Real-World Applications

Set operations are useful for:

- Finding common customers between stores.
- Comparing friend lists on social media.
- Identifying students enrolled in multiple courses.
- Removing duplicate records.
- Comparing product inventories.

---

## 🤖 AI Connection

Set operations are widely used in AI and Machine Learning.

Examples include:

- Finding common words between documents.
- Building vocabularies for NLP.
- Comparing predicted labels with actual labels.
- Identifying unique features.
- Measuring similarity between datasets.

Many similarity metrics, such as the **Jaccard Similarity**, are based directly on set operations.

---

## 💼 Best Practices

- Use operators (`|`, `&`, `-`, `^`) for concise and readable code.
- Use subset and superset checks when validating relationships between collections.
- Use disjoint checks to quickly verify whether two groups have anything in common.

---

## ⚠️ Common Mistakes

### Confusing Union and Intersection

```python
a | b
```

Returns all unique elements.

```python
a & b
```

Returns only common elements.

---

### Assuming Difference Works Both Ways

```python
a - b
```

is **not** the same as

```python
b - a
```

---

### Confusing Difference with Symmetric Difference

Difference removes only elements from one direction.

Symmetric Difference removes common elements from both sets.

---

## 📝 Interview Insight

### Question

What is the difference between Difference and Symmetric Difference?

### Answer

- **Difference (`-`)** returns elements present in the first set but not in the second.
- **Symmetric Difference (`^`)** returns elements that are present in either set but not in both.

---

## 💡 Remember This

| Operation | Meaning |
|-----------|---------|
| `|` | Combine all unique elements |
| `&` | Common elements |
| `-` | Elements only in first set |
| `^` | Elements in either set, not both |
| `issubset()` | Completely contained |
| `issuperset()` | Completely contains |
| `isdisjoint()` | No common elements |

---

## 🎯 Key Takeaways

- Set operations are inspired by mathematical set theory.
- They provide efficient ways to compare and combine collections.
- These operations are widely used in software development, databases, AI, and data science.
- Understanding these operations is essential for writing clean and efficient Python code.

---

## 💻 Code Reference

`code/sets.py`