# Working with JSON Files

## 📖 Overview

**JSON (JavaScript Object Notation)** is a lightweight text format used to store and exchange structured data.

Although it originated from JavaScript, JSON is language-independent and is supported by almost every modern programming language.

Python provides the built-in **`json` module** to read, write, and manipulate JSON data.

Today, JSON is the most widely used format for:

- REST APIs
- Web applications
- Configuration files
- Cloud services
- Mobile applications
- AI applications

---

## ❓ Why Do We Need JSON?

Suppose we want to store information about a student.

Without JSON:

```text
Name: Noor
Age: 21
Course: BCA
```

With JSON:

```json
{
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

JSON organizes information into key-value pairs, making it easy for both humans and programs to understand.

---

# 🧠 What is JSON?

JSON stands for:

**JavaScript Object Notation**

It stores data using:

- Objects
- Arrays
- Strings
- Numbers
- Booleans
- Null values

Example:

```json
{
    "name": "Noor",
    "age": 21,
    "skills": [
        "Python",
        "FastAPI",
        "Machine Learning"
    ],
    "graduated": false
}
```

---

# 🧠 JSON Data Types

| JSON Type | Python Type |
|------------|-------------|
| Object | dict |
| Array | list |
| String | str |
| Number | int / float |
| Boolean | bool |
| Null | None |

Example:

```json
{
    "name": "Noor",
    "age": 21,
    "active": true,
    "city": null
}
```

becomes

```python
{
    "name": "Noor",
    "age": 21,
    "active": True,
    "city": None
}
```

---

# 🧠 The `json` Module

Import it using:

```python
import json
```

It is included in Python's standard library.

---

# 🧠 Reading JSON Files

Use `json.load()`.

Example

`student.json`

```json
{
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

Python:

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
```

Output

```python
{
    'name': 'Noor',
    'age': 21,
    'course': 'BCA'
}
```

Notice that Python converts the JSON object into a dictionary.

---

# 🧠 Accessing Values

Since JSON objects become dictionaries:

```python
print(data["name"])
```

Output

```text
Noor
```

Another example:

```python
print(data["course"])
```

Output

```text
BCA
```

---

# 🧠 Writing JSON Files

Use `json.dump()`.

Example

```python
import json

student = {
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}

with open("student.json", "w") as file:
    json.dump(student, file)
```

Generated file:

```json
{"name": "Noor", "age": 21, "course": "BCA"}
```

---

# 🧠 Pretty Printing JSON

For better readability:

```python
json.dump(student, file, indent=4)
```

Generated file:

```json
{
    "name": "Noor",
    "age": 21,
    "course": "BCA"
}
```

The `indent` parameter formats the output with spaces and line breaks.

---

# 🧠 `load()` vs `loads()`

Both read JSON, but from different sources.

### `json.load()`

Reads JSON from a file.

```python
with open("student.json") as file:
    data = json.load(file)
```

---

### `json.loads()`

Reads JSON from a string.

```python
import json

text = '{"name":"Noor","age":21}'

data = json.loads(text)

print(data)
```

Output

```python
{
    'name': 'Noor',
    'age': 21
}
```

---

# 🧠 `dump()` vs `dumps()`

### `json.dump()`

Writes JSON directly into a file.

```python
json.dump(student, file)
```

---

### `json.dumps()`

Converts a Python object into a JSON string.

```python
text = json.dumps(student)

print(text)
```

Output

```json
{"name": "Noor", "age": 21, "course": "BCA"}
```

---

# 🧠 Summary

| Function | Works With | Purpose |
|----------|------------|----------|
| `load()` | File | Read JSON |
| `loads()` | String | Parse JSON string |
| `dump()` | File | Write JSON |
| `dumps()` | String | Convert to JSON string |

---

## ⚙️ Behind the Scenes

When Python reads JSON:

```
JSON File

↓

Read Text

↓

json Module

↓

Python Dictionary / List

↓

Program
```

When writing:

```
Python Dictionary

↓

json Module

↓

JSON Text

↓

JSON File
```

The `json` module automatically converts between JSON and Python data types.

---

## 🌍 Real-World Applications

JSON is widely used for:

- REST APIs
- Configuration files
- Mobile applications
- Cloud services
- Authentication systems
- Browser storage
- Web applications
- Microservices

---

## 🤖 AI Connection

JSON is one of the most important formats in AI and Machine Learning.

Examples:

### Store model configuration

```json
{
    "learning_rate": 0.001,
    "epochs": 20,
    "batch_size": 32
}
```

---

### Save predictions

```json
{
    "prediction": "Positive",
    "confidence": 0.98
}
```

---

### Exchange API responses

Large Language Models often return structured JSON such as:

```json
{
    "summary": "...",
    "keywords": [
        "AI",
        "Python"
    ]
}
```

Frameworks like FastAPI automatically convert Python dictionaries into JSON responses.

---

## 💼 Best Practices

- Always use the `json` module instead of manually creating JSON strings.
- Use `indent=4` for human-readable files.
- Use descriptive key names.
- Keep nested structures organized.
- Validate JSON before processing if it comes from external sources.

---

## ⚠️ Common Mistakes

### Confusing JSON with Python Dictionaries

JSON:

```json
{
    "age": 21
}
```

Python:

```python
{
    "age": 21
}
```

Differences:

- JSON uses `true`, `false`, and `null`.
- Python uses `True`, `False`, and `None`.

---

### Forgetting `json.load()`

Incorrect:

```python
file.read()
```

Correct:

```python
json.load(file)
```

The `json` module parses the JSON text into Python objects.

---

### Creating JSON Manually

Avoid:

```python
text = '{"name":"Noor"}'
```

Prefer:

```python
json.dumps(student)
```

It correctly handles escaping, formatting, and special characters.

---

## 📝 Interview Insight

### Question

What is JSON?

### Answer

JSON is a lightweight text-based format used to store and exchange structured data. It is language-independent and widely used in web applications and APIs.

---

### Question

What is the difference between `load()` and `loads()`?

### Answer

- `json.load()` reads JSON from a file.
- `json.loads()` reads JSON from a string.

---

### Question

What is the difference between `dump()` and `dumps()`?

### Answer

- `json.dump()` writes JSON to a file.
- `json.dumps()` converts a Python object into a JSON-formatted string.

---

### Question

Why is JSON popular?

### Answer

Because it is lightweight, human-readable, language-independent, and supported by nearly every programming language and web framework.

---

## 💡 Remember This

| Function | Memory Trick |
|----------|--------------|
| `load()` | Load from **File** |
| `loads()` | Load from **String** |
| `dump()` | Dump into **File** |
| `dumps()` | Dump into **String** |

Think:

> **No "s" = File.  
> "s" = String.**

---

## 🎯 Key Takeaways

- JSON is the standard format for structured data exchange.
- Python's `json` module simplifies reading and writing JSON.
- `load()` and `dump()` work with files.
- `loads()` and `dumps()` work with strings.
- JSON objects become Python dictionaries, and JSON arrays become Python lists.
- JSON is essential for backend development, REST APIs, cloud applications, and AI/ML workflows.

---

## 💻 Code Reference

`code/file_handling.py`