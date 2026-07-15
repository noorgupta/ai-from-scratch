# Ordering and Copying Lists

## 📖 Overview

Python provides several built-in methods to organize and duplicate lists efficiently. These methods allow developers to sort data, reverse the order of elements, and create copies of existing lists.

The primary methods are:

- `sort()`
- `reverse()`
- `copy()`

---

## ❓ Why Do We Need These Methods?

In real-world applications, data often needs to be organized or duplicated.

For example:

- Display products from lowest to highest price.
- Show the latest messages first.
- Create a backup before modifying data.

Python provides built-in methods to perform these operations efficiently.

---

# `sort()`

## 🧠 What is `sort()`?

The `sort()` method arranges the elements of a list in ascending order by default.

### Syntax

```python
list.sort()
```

### Example

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

**Output**

```text
[10, 20, 30, 40]
```

### Descending Order

```python
numbers.sort(reverse=True)

print(numbers)
```

**Output**

```text
[40, 30, 20, 10]
```

> **Note:** `sort()` modifies the original list.

---

# `reverse()`

## 🧠 What is `reverse()`?

The `reverse()` method reverses the current order of the elements.

### Syntax

```python
list.reverse()
```

### Example

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

**Output**

```text
[40, 30, 20, 10]
```

> **Important:** `reverse()` does **not** sort the list. It simply reverses the existing order.

---

# `copy()`

## 🧠 What is `copy()`?

The `copy()` method creates a **shallow copy** of a list.

### Syntax

```python
list.copy()
```

### Example

```python
original = [10, 20, 30]

duplicate = original.copy()

print(duplicate)
```

**Output**

```text
[10, 20, 30]
```

Both lists contain the same elements but are different list objects.

---

## ⚙️ Choosing the Right Method

| Method | Purpose |
|---------|----------|
| `sort()` | Arrange elements in ascending or descending order |
| `reverse()` | Reverse the current order |
| `copy()` | Create a duplicate of the list |

---

## 🌍 Real-World Applications

These methods are useful for:

- Sorting products by price.
- Ranking students by marks.
- Displaying recent notifications first.
- Creating backups before editing data.
- Organizing reports.

---

## 🤖 AI Connection

These methods are frequently used during data preprocessing.

Examples include:

- Sorting datasets.
- Reversing sequences.
- Creating copies before applying transformations.
- Preserving the original data while experimenting with preprocessing techniques.

---

## 💼 Best Practices

- Use `sort()` when you want to permanently arrange a list.
- Use `reverse()` only when reversing the existing order.
- Use `copy()` before making changes if the original data must remain unchanged.

---

## ⚠️ Common Mistakes

### Confusing `sort()` with `reverse()`

```python
numbers = [3, 1, 2]

numbers.reverse()
```

Output:

```text
[2, 1, 3]
```

This is **not** sorted.

Correct:

```python
numbers.sort()
```

Output:

```text
[1, 2, 3]
```

---

### Assigning Instead of Copying

```python
list1 = [1, 2, 3]
list2 = list1
```

This **does not** create a new list.

Both variables refer to the same list object.

To create an independent copy:

```python
list2 = list1.copy()
```

---

## 💡 Remember This

- `sort()` → Arrange elements.
- `reverse()` → Reverse the order.
- `copy()` → Create a new list with the same elements.

---

## 🎯 Key Takeaways

- Python provides efficient methods for organizing and duplicating lists.
- `sort()` modifies the original list.
- `reverse()` only changes the order of elements.
- `copy()` creates a shallow copy, allowing safe modifications without affecting the original list.

---

## 💻 Code Reference

`code/06-list-methods/03-ordering-copying.py`