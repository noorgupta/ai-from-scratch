# Built-in Functions

## 📖 Overview

Python provides many **built-in functions** that are available by default. These functions perform common tasks such as finding the length of a collection, calculating sums, sorting data, checking conditions, and converting data types.

Using built-in functions makes programs:

- Shorter
- Faster
- More readable
- More efficient

Instead of writing common algorithms yourself, you can rely on Python's optimized implementations.

---

## ❓ Why Do We Need Built-in Functions?

Imagine finding the length of a list manually.

```python
numbers = [10, 20, 30, 40]

count = 0

for _ in numbers:
    count += 1

print(count)
```

Python already provides a simpler solution.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

**Output**

```text
4
```

Built-in functions save time and reduce errors.

---

# 🧠 `len()`

Returns the number of items in an object.

```python
numbers = [1, 2, 3, 4]

print(len(numbers))
```

**Output**

```text
4
```

Works with:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

For dictionaries, `len()` returns the number of key-value pairs.

---

# 🧠 `sum()`

Returns the sum of numeric values.

```python
marks = [80, 90, 95]

print(sum(marks))
```

**Output**

```text
265
```

---

# 🧠 `max()`

Returns the largest value.

```python
print(max([5, 8, 2, 9]))
```

**Output**

```text
9
```

---

# 🧠 `min()`

Returns the smallest value.

```python
print(min([5, 8, 2, 9]))
```

**Output**

```text
2
```

---

# 🧠 `abs()`

Returns the absolute (positive) value.

```python
print(abs(-15))
```

**Output**

```text
15
```

Useful for calculating distances and errors.

---

# 🧠 `round()`

Rounds a number.

```python
print(round(3.14159, 2))
```

**Output**

```text
3.14
```

Without the second argument:

```python
print(round(3.8))
```

**Output**

```text
4
```

---

# 🧠 `sorted()`

Returns a new sorted list.

```python
numbers = [5, 2, 8, 1]

print(sorted(numbers))
```

**Output**

```text
[1, 2, 5, 8]
```

Descending order:

```python
print(sorted(numbers, reverse=True))
```

**Output**

```text
[8, 5, 2, 1]
```

Sorting by key:

```python
students = [
    ("Noor", 90),
    ("Aman", 85),
    ("Priya", 95)
]

print(sorted(students, key=lambda student: student[1]))
```

---

# 🧠 `zip()`

Combines multiple iterables element by element.

```python
names = ["Noor", "Aman"]

marks = [90, 85]

print(list(zip(names, marks)))
```

**Output**

```text
[
 ('Noor', 90),
 ('Aman', 85)
]
```

---

# 🧠 `enumerate()`

Adds an index while iterating.

```python
subjects = ["Python", "AI", "Math"]

for index, subject in enumerate(subjects, start=1):
    print(index, subject)
```

**Output**

```text
1 Python

2 AI

3 Math
```

---

# 🧠 `any()`

Returns `True` if **at least one** element is truthy.

```python
values = [False, False, True]

print(any(values))
```

**Output**

```text
True
```

---

# 🧠 `all()`

Returns `True` only if **every** element is truthy.

```python
values = [True, True, True]

print(all(values))
```

**Output**

```text
True
```

```python
values = [True, False]

print(all(values))
```

**Output**

```text
False
```

---

# 🧠 `type()`

Returns the data type of an object.

```python
print(type(100))
```

**Output**

```text
<class 'int'>
```

---

# 🧠 `isinstance()`

Checks whether an object belongs to a specific type.

```python
number = 10

print(isinstance(number, int))
```

**Output**

```text
True
```

Example:

```python
print(isinstance("Python", str))
```

**Output**

```text
True
```

---

## ⚙️ Summary

| Function | Purpose |
|----------|---------|
| `len()` | Count items |
| `sum()` | Add numbers |
| `max()` | Largest value |
| `min()` | Smallest value |
| `abs()` | Absolute value |
| `round()` | Round numbers |
| `sorted()` | Return sorted list |
| `zip()` | Combine iterables |
| `enumerate()` | Add indexes |
| `any()` | At least one True |
| `all()` | All True |
| `type()` | Return data type |
| `isinstance()` | Check object type |

---

## ⚙️ Behind the Scenes

Most built-in functions are implemented in **C** inside CPython, making them significantly faster than equivalent Python code.

For example:

```python
len(my_list)
```

does **not** iterate through the list each time. Lists internally store their length, allowing `len()` to return it in **O(1)** time.

Similarly:

- `sum()` uses optimized loops.
- `sorted()` implements **Timsort**, a highly efficient sorting algorithm.
- `zip()` returns an iterator instead of creating a new list immediately, making it memory efficient.

---

## 🌍 Real-World Applications

Built-in functions are used in:

- Data validation
- Report generation
- API responses
- Data aggregation
- Sorting dashboards
- File processing
- Automation scripts

They simplify common programming tasks and improve readability.

---

## 🤖 AI Connection

Built-in functions are frequently used in AI and Machine Learning.

Examples:

```python
len(dataset)
```

Count training samples.

```python
max(probabilities)
```

Find the highest prediction score.

```python
sorted(predictions)
```

Rank model outputs.

```python
zip(features, labels)
```

Pair input data with target values.

```python
enumerate(dataset)
```

Track batch numbers during training.

These functions are foundational in preprocessing and evaluation pipelines.

---

## 💼 Best Practices

- Prefer built-in functions over manually implementing common operations.
- Use `sorted()` instead of modifying data when you need to preserve the original collection.
- Use `enumerate()` instead of maintaining a manual counter.
- Use `zip()` to iterate over multiple collections together.
- Use `isinstance()` instead of comparing types directly when checking object types.

---

## ⚠️ Common Mistakes

### Confusing `sorted()` with `list.sort()`

```python
numbers = [3, 1, 2]

sorted_numbers = sorted(numbers)
```

`sorted()` returns a **new list**.

```python
numbers.sort()
```

`sort()` modifies the original list.

---

### Using `type()` for Type Checking

Less flexible:

```python
type(value) == int
```

Better:

```python
isinstance(value, int)
```

`isinstance()` also works correctly with inheritance.

---

### Forgetting that `zip()` Returns an Iterator

```python
pairs = zip(names, marks)
```

To display the results:

```python
print(list(pairs))
```

---

## 📝 Interview Insight

### Question

What is the difference between `type()` and `isinstance()`?

### Answer

- `type(obj)` returns the exact type of an object.
- `isinstance(obj, Class)` checks whether the object belongs to a class or any of its subclasses.

`isinstance()` is generally preferred for type checking in real-world applications.

---

## 💡 Remember This

| Function | Easy Memory Trick |
|----------|-------------------|
| `len()` | Count |
| `sum()` | Add |
| `max()` | Largest |
| `min()` | Smallest |
| `abs()` | Positive distance |
| `round()` | Approximate |
| `sorted()` | New sorted list |
| `zip()` | Pair together |
| `enumerate()` | Add index |
| `any()` | At least one |
| `all()` | Every one |
| `type()` | What type? |
| `isinstance()` | Is this type? |

---

## 🎯 Key Takeaways

- Built-in functions provide optimized solutions for common programming tasks.
- They improve code readability, maintainability, and performance.
- Functions such as `sorted()`, `zip()`, and `enumerate()` are widely used in professional Python code.
- `isinstance()` is generally preferred over `type()` for checking object types.
- Mastering these functions will significantly improve your productivity as a Python developer.

---

## 💻 Code Reference

`code/functions.py`