# List Methods Cheatsheet

This cheatsheet provides a quick reference to the most commonly used Python list methods. Use it for revision, interviews, or while solving problems.

---

## 📋 Quick Reference Table

| Method | Purpose | Modifies Original List | Returns |
|---------|---------|-----------------------|---------|
| `append(x)` | Add one element at the end | ✅ | `None` |
| `extend(iterable)` | Add multiple elements | ✅ | `None` |
| `insert(i, x)` | Insert an element at a specific index | ✅ | `None` |
| `remove(x)` | Remove the first occurrence of a value | ✅ | `None` |
| `pop([i])` | Remove and return an element | ✅ | Removed element |
| `clear()` | Remove all elements | ✅ | `None` |
| `index(x)` | Return the first index of a value | ❌ | Index |
| `count(x)` | Count occurrences of a value | ❌ | Integer |
| `sort()` | Sort the list | ✅ | `None` |
| `reverse()` | Reverse the list | ✅ | `None` |
| `copy()` | Create a shallow copy | ❌ | New List |

---

## 🧠 Which Method Should You Use?

| Goal | Method |
|------|--------|
| Add one element | `append()` |
| Add multiple elements | `extend()` |
| Insert at a specific position | `insert()` |
| Remove by value | `remove()` |
| Remove by index | `pop()` |
| Delete all elements | `clear()` |
| Find an element's position | `index()` |
| Count occurrences | `count()` |
| Sort data | `sort()` |
| Reverse current order | `reverse()` |
| Duplicate a list | `copy()` |

---

## ⚠️ Common Mistakes

### ❌ `append()` vs `extend()`

```python
numbers = [1, 2]

numbers.append([3, 4])
```

Output:

```python
[1, 2, [3, 4]]
```

Correct:

```python
numbers.extend([3, 4])
```

Output:

```python
[1, 2, 3, 4]
```

---

### ❌ `sort()` vs `reverse()`

```python
numbers.sort()
```

Sorts the list.

```python
numbers.reverse()
```

Only reverses the existing order.

---

### ❌ `copy()` vs Assignment

```python
list2 = list1
```

Both variables point to the same list.

Correct:

```python
list2 = list1.copy()
```

Creates a new list object.

---

## 🤖 AI Perspective

List methods are frequently used during:

- Dataset preparation
- Data cleaning
- Feature engineering
- Label management
- Prediction storage
- Data preprocessing before using NumPy or Pandas

Although AI libraries provide optimized data structures, Python lists remain an important starting point for handling and organizing data.

---

## 💡 Quick Revision

| Method | Remember |
|---------|----------|
| `append()` | One element |
| `extend()` | Multiple elements |
| `insert()` | Specific position |
| `remove()` | Remove by value |
| `pop()` | Remove by index and return |
| `clear()` | Empty the list |
| `index()` | First occurrence |
| `count()` | Number of occurrences |
| `sort()` | Arrange elements |
| `reverse()` | Reverse order |
| `copy()` | Duplicate list |

---

## 🎯 Final Takeaway

Mastering these list methods will make your Python code cleaner, shorter, and more efficient. These methods are used extensively in software development, data analysis, Machine Learning, and Artificial Intelligence.