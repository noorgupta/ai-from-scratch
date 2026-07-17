# Iterating Through Dictionaries

## 📖 Overview

Iteration is the process of visiting each element in a collection one at a time.

When working with dictionaries, you may need to iterate through:

- Keys
- Values
- Key-value pairs

Python provides several efficient ways to perform these tasks.

---

## ❓ Why Iterate Through Dictionaries?

Suppose you have student marks.

```python
marks = {
    "Python": 95,
    "AI": 91,
    "Math": 88
}
```

You might want to:

- Display all subjects.
- Print all marks.
- Generate a report.
- Calculate statistics.
- Validate data.

Iteration makes these operations possible.

---

# 🧠 Iterating Over Keys

By default, a `for` loop iterates over dictionary keys.

```python
marks = {
    "Python": 95,
    "AI": 91,
    "Math": 88
}

for subject in marks:
    print(subject)
```

**Output**

```text
Python
AI
Math
```

This is equivalent to:

```python
for subject in marks.keys():
    print(subject)
```

---

# 🧠 Iterating Over Values

Use the `values()` method.

```python
for score in marks.values():
    print(score)
```

**Output**

```text
95
91
88
```

Useful when only the values are required.

---

# 🧠 Iterating Over Key-Value Pairs

Use the `items()` method.

```python
for subject, score in marks.items():
    print(subject, ":", score)
```

**Output**

```text
Python : 95
AI : 91
Math : 88
```

This is the most common and recommended approach when both keys and values are needed.

---

# 🧠 Using `enumerate()` with Dictionaries

Sometimes you want an index while iterating.

```python
for index, (subject, score) in enumerate(marks.items(), start=1):
    print(index, subject, score)
```

**Output**

```text
1 Python 95
2 AI 91
3 Math 88
```

This is useful for generating numbered reports or tables.

---

# 🧠 Iterating Through Nested Dictionaries

```python
students = {
    "student1": {
        "name": "Noor",
        "age": 21
    },
    "student2": {
        "name": "Aman",
        "age": 22
    }
}
```

Iterate through both levels.

```python
for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, ":", value)
```

**Output**

```text
student1
name : Noor
age : 21

student2
name : Aman
age : 22
```

Nested iteration is common when processing structured data such as JSON.

---

## ⚙️ Behind the Scenes

When Python executes:

```python
for key, value in marks.items():
```

The `items()` method returns a view of key-value tuples.

Conceptually:

```text
('Python', 95)

('AI', 91)

('Math', 88)
```

Each tuple is unpacked into:

```python
key
value
```

This avoids repeated dictionary lookups and makes iteration efficient.

---

## 🌍 Real-World Applications

Dictionary iteration is useful for:

- Processing JSON data.
- Displaying user profiles.
- Creating reports.
- Reading configuration files.
- Exporting data to CSV.
- Building dashboards.

---

## 🤖 AI Connection

Iteration is used extensively in AI and Machine Learning.

Examples include:

- Iterating through model parameters.
- Reading feature dictionaries.
- Processing prediction results.
- Displaying evaluation metrics.
- Traversing NLP vocabularies.

Most AI frameworks return dictionaries that are processed using iteration.

---

## 💼 Best Practices

- Use `items()` when both keys and values are needed.
- Use `keys()` or direct iteration when only keys are required.
- Use `values()` when only values matter.
- Use `enumerate()` when numbering output.
- Avoid modifying a dictionary while iterating over it.

---

## ⚠️ Common Mistakes

### Forgetting `.items()`

Incorrect

```python
for key, value in marks:
    print(key, value)
```

Raises

```text
ValueError
```

Correct

```python
for key, value in marks.items():
    print(key, value)
```

---

### Modifying a Dictionary During Iteration

```python
for key in marks:
    marks["Physics"] = 90
```

Raises

```text
RuntimeError
```

If modifications are necessary:

```python
for key in list(marks.keys()):
    # Safe modifications
    pass
```

---

### Using Keys When Values Are Needed

Less efficient

```python
for key in marks:
    print(marks[key])
```

Better

```python
for value in marks.values():
    print(value)
```

Choose the iteration method that matches your goal.

---

## 📝 Interview Insight

### Question

What is the best way to iterate through both keys and values of a dictionary?

### Answer

Use the `items()` method.

```python
for key, value in dictionary.items():
```

It is more readable and avoids unnecessary lookups.

---

## 💡 Remember This

| Goal | Method |
|------|--------|
| Keys | `for key in dict` or `dict.keys()` |
| Values | `dict.values()` |
| Keys & Values | `dict.items()` |
| Numbered Output | `enumerate(dict.items())` |

---

## 🎯 Key Takeaways

- Dictionaries can be iterated over in multiple ways.
- Default iteration returns keys.
- `values()` returns values.
- `items()` returns key-value pairs and is the preferred method when both are required.
- Nested dictionaries require nested loops.
- Efficient iteration is an essential skill for backend development, data processing, and AI applications.

---

## 💻 Code Reference

`code/dictionaries.py`