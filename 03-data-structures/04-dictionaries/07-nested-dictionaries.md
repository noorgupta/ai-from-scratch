# Nested Dictionaries

## 📖 Overview

A **nested dictionary** is a dictionary that contains one or more dictionaries as its values.

This allows Python to represent complex, hierarchical, and structured data efficiently.

Nested dictionaries are commonly used to model real-world objects and relationships.

---

## ❓ Why Do We Need Nested Dictionaries?

Suppose you want to store information about multiple students.

Using a single dictionary:

```python
student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

This works for one student.

But what if you have many students?

Nested dictionaries provide a clean solution.

```python
students = {
    "student1": {
        "name": "Noor",
        "age": 21,
        "course": "BCA"
    },
    "student2": {
        "name": "Aman",
        "age": 22,
        "course": "B.Tech"
    }
}
```

Each student is represented as its own dictionary.

---

# 🧠 Accessing Nested Values

Access nested dictionaries one level at a time.

```python
students = {
    "student1": {
        "name": "Noor",
        "age": 21
    }
}

print(students["student1"]["name"])
```

**Output**

```text
Noor
```

Python first retrieves `"student1"` and then accesses `"name"` inside it.

---

# 🧠 Updating Nested Values

Nested values can be modified just like normal dictionary values.

```python
students["student1"]["age"] = 22

print(students)
```

**Output**

```python
{
    'student1': {
        'name': 'Noor',
        'age': 22
    }
}
```

---

# 🧠 Adding New Data

You can add new keys inside nested dictionaries.

```python
students["student1"]["city"] = "Lucknow"

print(students)
```

**Output**

```python
{
    'student1': {
        'name': 'Noor',
        'age': 22,
        'city': 'Lucknow'
    }
}
```

---

# 🧠 Adding a New Nested Dictionary

```python
students["student2"] = {
    "name": "Aman",
    "age": 20,
    "course": "B.Tech"
}
```

The dictionary now stores two students.

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

---

# 🧠 Dictionaries Inside Lists

Nested structures often combine dictionaries and lists.

```python
students = [
    {
        "name": "Noor",
        "skills": ["Python", "AI"]
    },
    {
        "name": "Aman",
        "skills": ["Java", "SQL"]
    }
]
```

Accessing data:

```python
print(students[0]["skills"][1])
```

**Output**

```text
AI
```

This combination is extremely common in API responses.

---

# 🧠 Lists Inside Dictionaries

A dictionary can also contain lists.

```python
student = {
    "name": "Noor",
    "skills": [
        "Python",
        "FastAPI",
        "Machine Learning"
    ]
}
```

Accessing:

```python
print(student["skills"][0])
```

**Output**

```text
Python
```

---

## ⚙️ Behind the Scenes

Nested dictionaries are simply references to other dictionary objects.

Conceptually:

```text
students
    │
    ▼
+--------------------+
| student1 | ------+ |
| student2 | --+   | |
+-----------|--|---+-+
            |  |
            ▼  ▼

Dictionary    Dictionary
```

Each nested dictionary occupies its own location in memory.

The outer dictionary stores references to these inner dictionaries.

---

## 🌍 Real-World Applications

Nested dictionaries are widely used in:

- User profiles
- Banking systems
- Product catalogs
- School management systems
- Configuration files
- REST APIs
- JSON documents

---

## 🤖 AI Connection

Nested dictionaries are fundamental in AI and Machine Learning.

Examples include:

- Model configuration files.
- Tokenizer vocabularies.
- Prediction results.
- Training metrics.
- Hyperparameter storage.
- Dataset metadata.

Frameworks like **TensorFlow**, **PyTorch**, and **Hugging Face Transformers** frequently return deeply nested dictionaries.

---

## 💼 Best Practices

- Keep nesting as shallow as practical.
- Use meaningful key names.
- Check that keys exist before accessing deeply nested data.
- Consider helper functions when working with very deep structures.

---

## ⚠️ Common Mistakes

### Forgetting Intermediate Keys

Incorrect

```python
students["name"]
```

Raises

```text
KeyError
```

Correct

```python
students["student1"]["name"]
```

---

### Confusing Lists and Dictionaries

```python
students["student1"][0]
```

Raises

```text
KeyError
```

Use keys for dictionaries and indexes for lists.

---

### Assuming Every Nested Key Exists

```python
students["student3"]["name"]
```

Raises

```text
KeyError
```

Safer approach:

```python
students.get("student3", {}).get("name")
```

This returns `None` instead of raising an error.

---

## 📝 Interview Insight

### Question

How do you safely access a deeply nested dictionary?

### Answer

Use chained `get()` calls with default values.

```python
students.get("student1", {}).get("name")
```

This avoids `KeyError` if any intermediate key is missing.

---

## 💡 Remember This

- Dictionary → Dictionary → Key
- Dictionary → List → Index
- List → Dictionary → Key

Examples:

```python
students["student1"]["name"]

student["skills"][0]

students[0]["skills"][1]
```

---

## 🎯 Key Takeaways

- Nested dictionaries represent hierarchical data.
- They are widely used in JSON, APIs, databases, and AI applications.
- Access nested data one level at a time.
- Combine dictionaries and lists to model complex real-world information.
- Use `get()` for safer access when keys may be missing.

---

## 💻 Code Reference

`code/dictionaries.py`