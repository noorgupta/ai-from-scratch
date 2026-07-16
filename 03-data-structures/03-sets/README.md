# Sets

## 📖 Overview

A set is a built-in Python data structure used to store multiple unique values in a single variable.

Unlike lists and tuples, sets do **not maintain the order of elements** and automatically remove duplicate values.

Sets are optimized for fast membership testing and mathematical set operations such as union, intersection, and difference.

---

## ❓ Why Do We Need Sets?

Suppose you have the following list of student IDs:

```python
student_ids = [101, 102, 101, 103, 102]
```

Notice that some IDs appear multiple times.

If duplicate values are not allowed, using a list requires extra code to remove them.

Using a set:

```python
student_ids = {101, 102, 103}
```

The duplicates are removed automatically.

---

## 🧠 Learning Path

This module covers:

1. Introduction to Sets
2. Creating Sets
3. Accessing Elements
4. Adding & Removing Elements
5. Set Methods
6. Set Operations
7. Frozen Sets
8. Sets vs Lists vs Tuples

---

## 🤖 AI Connection

Sets are widely used in AI and Machine Learning for:

- Removing duplicate records
- Finding unique labels in datasets
- Comparing collections of data
- Fast lookups during preprocessing
- Vocabulary creation in Natural Language Processing (NLP)

Because membership checking in a set is very fast, sets help improve the efficiency of many AI applications.

---

## 📂 Structure

```text
03-sets/
│
├── README.md
├── notes/
├── code/
└── assets/
```

---

## 🎯 Key Takeaways

- Sets store unique values.
- Duplicate elements are automatically removed.
- Sets are unordered.
- Sets provide very fast searching and powerful mathematical operations.
