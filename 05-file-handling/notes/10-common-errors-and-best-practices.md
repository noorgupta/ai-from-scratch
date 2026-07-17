# Common Errors and Best Practices

## 📖 Overview

File handling is one of the most common operations in Python applications.

However, working with files also introduces several challenges:

- Files may not exist.
- Programs may not have permission to access them.
- Files may already be open.
- Data may become corrupted if handled incorrectly.

Professional developers write file-handling code that anticipates these situations and responds safely.

This note covers the most common file-related errors, how to handle them, and the best practices followed in real-world Python projects.

---

## ❓ Why Error Handling Matters

Imagine a program that loads a configuration file.

```python
with open("config.json") as file:
    ...
```

If `config.json` is missing, the program crashes.

A better approach is to detect the problem and handle it gracefully.

```
Open File

↓

Success?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
Continue   Handle Error
```

---

# 🧠 Common File Handling Errors

Python raises different exceptions depending on the problem.

Understanding these exceptions helps you write robust applications.

---

# 🧠 `FileNotFoundError`

Raised when the specified file does not exist.

Example:

```python
with open("missing.txt", "r") as file:
    pass
```

Output

```text
FileNotFoundError
```

Solution:

- Verify the file name.
- Check the file path.
- Confirm the file exists.

---

# 🧠 `PermissionError`

Raised when the program lacks permission to access a file.

Example:

```python
with open("protected.txt", "w") as file:
    pass
```

Possible Output

```text
PermissionError
```

Common causes:

- File is read-only.
- Insufficient user permissions.
- Another application restricts access.

---

# 🧠 `IsADirectoryError`

Raised when attempting to open a directory as if it were a file.

Example:

```python
with open("data", "r") as file:
    pass
```

Output

```text
IsADirectoryError
```

---

# 🧠 `NotADirectoryError`

Raised when part of a path expected to be a directory is actually a file.

Example:

```python
open("notes.txt/data.csv")
```

Output

```text
NotADirectoryError
```

---

# 🧠 `FileExistsError`

Raised when using exclusive creation mode (`"x"`) and the file already exists.

Example:

```python
open("report.txt", "x")
```

Output

```text
FileExistsError
```

---

# 🧠 `UnicodeDecodeError`

Raised when Python cannot decode file contents using the specified text encoding.

Example:

```python
with open("data.txt", encoding="utf-8") as file:
    file.read()
```

If the file uses a different encoding, Python may raise:

```text
UnicodeDecodeError
```

Possible solutions:

```python
open("data.txt", encoding="latin-1")
```

or determine the correct encoding used to create the file.

---

# 🧠 Handling Errors with `try` and `except`

Instead of allowing the program to crash:

```python
try:
    with open("students.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
```

Output

```text
File not found.
```

The program continues running.

---

# 🧠 Handling Multiple Exceptions

```python
try:
    with open("students.txt") as file:
        ...

except FileNotFoundError:
    print("File missing.")

except PermissionError:
    print("Permission denied.")
```

Different exceptions can be handled separately.

---

# 🧠 Using `finally`

The `finally` block always executes.

Example:

```python
try:
    print("Opening file")

except Exception:
    print("Error")

finally:
    print("Cleanup completed")
```

Output

```text
Opening file

Cleanup completed
```

When using the `with` statement, explicit file cleanup is usually unnecessary because it is handled automatically.

---

# 🧠 Checking Before Opening

Instead of immediately opening a file:

```python
from pathlib import Path

path = Path("students.csv")

if path.exists():
    with path.open() as file:
        print(file.read())
else:
    print("File does not exist.")
```

This reduces the chance of runtime errors.

---

# 🧠 Logging Errors

Large applications usually record errors in log files instead of displaying them to users.

Example:

```text
2026-07-17 14:30
FileNotFoundError
config.json
```

Logs help developers diagnose problems later.

---

## ⚙️ Behind the Scenes

When Python opens a file:

```
Program

↓

Operating System

↓

Check Path

↓

Check Permissions

↓

Open File

↓

Return File Object
```

If any step fails, Python raises an appropriate exception instead of continuing with invalid data.

---

## 🌍 Real-World Applications

Professional applications use error handling when:

- Uploading documents
- Processing datasets
- Reading configuration files
- Saving reports
- Exporting invoices
- Managing backups
- Handling cloud storage

Users should receive meaningful messages rather than seeing the program crash.

---

## 🤖 AI Connection

Error handling is essential in AI and Machine Learning.

Examples:

- Verify a dataset exists before training.
- Handle missing model files gracefully.
- Validate configuration files.
- Detect corrupted training data.
- Save experiment logs even if training fails.

Reliable error handling improves the stability of AI pipelines.

---

## 💼 Best Practices

- Prefer the `with` statement for file operations.
- Use `pathlib` for modern path handling.
- Catch only the exceptions you expect.
- Display meaningful error messages.
- Validate file paths before processing.
- Use relative paths within projects.
- Organize files into dedicated directories.
- Log unexpected errors for debugging.
- Avoid hardcoding platform-specific file paths.

---

## ⚠️ Common Mistakes

### Using `except:` Without Specifying an Exception

Avoid:

```python
try:
    ...
except:
    print("Error")
```

Prefer:

```python
except FileNotFoundError:
```

Specific exceptions make debugging easier.

---

### Ignoring Exceptions

Avoid:

```python
except:
    pass
```

This hides errors and makes problems difficult to diagnose.

---

### Forgetting the `with` Statement

Avoid:

```python
file = open("notes.txt")
```

Prefer:

```python
with open("notes.txt") as file:
    ...
```

---

### Hardcoding File Paths

Avoid:

```python
"C:\\Users\\Noor\\Desktop\\file.txt"
```

Prefer:

```python
Path("data") / "file.txt"
```

---

## 📝 Interview Insight

### Question

Why should file operations use exception handling?

### Answer

File operations depend on external resources that may not always be available. Exception handling allows programs to recover gracefully instead of crashing.

---

### Question

Which exception is raised when a file does not exist?

### Answer

`FileNotFoundError`

---

### Question

Why is the `with` statement considered a best practice?

### Answer

It automatically closes files, even if an exception occurs, reducing resource leaks and improving code readability.

---

### Question

Why should `except:` be avoided?

### Answer

A bare `except:` catches every exception, including unexpected ones, making debugging more difficult. Catch specific exceptions whenever possible.

---

## 💡 Remember This

### Safe File Handling Workflow

```
Locate File

↓

Check Exists

↓

Open with `with`

↓

Read / Write

↓

Handle Exceptions

↓

Automatic Close
```

Think:

> **Expect failures. Handle them gracefully.**

---

## 🎯 Key Takeaways

- File operations may fail for reasons outside your program's control.
- Common exceptions include `FileNotFoundError`, `PermissionError`, `FileExistsError`, and `UnicodeDecodeError`.
- Use `try`/`except` to handle expected errors gracefully.
- The `with` statement automatically manages file cleanup.
- `pathlib` simplifies file path handling and improves portability.
- Writing defensive, well-structured file handling code results in more reliable backend systems, automation tools, and AI/ML applications.

---

## 💻 Code Reference

`code/file_handling.py`