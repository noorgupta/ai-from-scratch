# File Paths, `os` Module, and `pathlib`

## 📖 Overview

Every file on a computer has a **path** that tells the operating system where it is located.

When working with files in Python, simply knowing how to read or write isn't enough—you must also know **where the file is stored**.

Python provides two powerful modules for working with file paths:

- **`os`** – Traditional module for interacting with the operating system.
- **`pathlib`** – Modern, object-oriented approach (recommended for new Python code).

These modules allow you to:

- Navigate directories
- Create folders
- Check if files exist
- Rename and delete files
- Build paths that work across Windows, macOS, and Linux

---

## ❓ Why Are File Paths Important?

Suppose your project looks like this:

```text
project/
│
├── main.py
├── data/
│   └── students.csv
└── reports/
    └── report.txt
```

If `main.py` wants to read `students.csv`, Python must know where the file is located.

Without the correct path:

```python
open("students.csv")
```

Python may raise:

```text
FileNotFoundError
```

---

# 🧠 What is a File Path?

A **file path** specifies the location of a file or folder.

Example:

```text
/home/noor/project/data/students.csv
```

Windows example:

```text
C:\Users\Noor\Documents\data\students.csv
```

---

# 🧠 Relative Path

A **relative path** is interpreted from the current working directory.

Example:

```python
open("data/students.csv")
```

Project:

```text
project/
│
├── main.py
└── data/
    └── students.csv
```

This is the preferred approach for most projects because it makes them easier to move between systems.

---

# 🧠 Absolute Path

An **absolute path** starts from the root of the file system.

Linux/macOS:

```text
/home/noor/project/data/students.csv
```

Windows:

```text
C:\Users\Noor\Documents\project\data\students.csv
```

Example:

```python
open("/home/noor/project/data/students.csv")
```

Absolute paths work only if the file exists at exactly that location.

---

# 🧠 The `os` Module

The `os` module provides functions for interacting with the operating system.

Import:

```python
import os
```

---

# 🧠 Current Working Directory

Find the directory where Python is currently running.

```python
import os

print(os.getcwd())
```

Example Output:

```text
/home/noor/project
```

---

# 🧠 Listing Files

```python
import os

print(os.listdir())
```

Example Output:

```python
[
    "main.py",
    "data",
    "report.txt"
]
```

List a specific folder:

```python
os.listdir("data")
```

---

# 🧠 Creating a Directory

Create a single directory:

```python
import os

os.mkdir("reports")
```

Create nested directories:

```python
os.makedirs("data/archive/2026")
```

---

# 🧠 Checking if a File Exists

```python
import os

print(os.path.exists("students.csv"))
```

Output:

```text
True
```

or

```text
False
```

---

# 🧠 Checking File vs Directory

```python
os.path.isfile("students.csv")
```

Returns:

```text
True
```

```python
os.path.isdir("data")
```

Returns:

```text
True
```

---

# 🧠 Renaming Files

```python
import os

os.rename("old.txt", "new.txt")
```

---

# 🧠 Deleting Files

```python
import os

os.remove("notes.txt")
```

Delete an empty folder:

```python
os.rmdir("reports")
```

---

# 🧠 The `pathlib` Module

`pathlib` is the modern way to work with file paths.

Import:

```python
from pathlib import Path
```

---

# 🧠 Creating a Path Object

```python
from pathlib import Path

path = Path("data/students.csv")
```

`path` is now a **Path object**, which provides many useful methods.

---

# 🧠 Checking if a Path Exists

```python
from pathlib import Path

path = Path("students.csv")

print(path.exists())
```

---

# 🧠 Checking File or Directory

```python
path.is_file()
```

```python
path.is_dir()
```

---

# 🧠 Creating Directories

```python
from pathlib import Path

Path("reports").mkdir()
```

Create nested directories:

```python
Path("data/archive/2026").mkdir(parents=True, exist_ok=True)
```

- `parents=True` creates missing parent folders.
- `exist_ok=True` prevents an error if the folder already exists.

---

# 🧠 Joining Paths

Instead of writing:

```python
"data/" + "students.csv"
```

Use:

```python
from pathlib import Path

path = Path("data") / "students.csv"
```

Result:

```text
data/students.csv
```

The `/` operator automatically creates the correct path for the operating system.

---

# 🧠 Why Prefer `pathlib`?

Comparison:

### Using `os`

```python
os.path.join("data", "students.csv")
```

### Using `pathlib`

```python
Path("data") / "students.csv"
```

`pathlib` is shorter, easier to read, and more object-oriented.

---

## ⚙️ Behind the Scenes

When Python opens a file:

```
Path

↓

Operating System

↓

Locate File

↓

Check Permissions

↓

Return File Object
```

Modules like `os` and `pathlib` help Python communicate with the operating system using the correct file paths.

---

## 🌍 Real-World Applications

File paths are used in:

- Reading datasets
- Saving reports
- Managing uploads
- Creating backups
- Logging
- Loading configuration files
- Processing images
- Organizing project files

---

## 🤖 AI Connection

File paths are essential in AI and Machine Learning.

Examples:

```python
dataset = Path("datasets/train.csv")
```

Load a training dataset.

```python
model = Path("models/model.pkl")
```

Save a trained model.

```python
logs = Path("logs/training.log")
```

Record training progress.

```python
images = Path("images")
```

Process image datasets for computer vision.

Well-organized directories make AI projects easier to maintain and scale.

---

## 💼 Best Practices

- Prefer **relative paths** within projects.
- Use `pathlib` for new Python projects.
- Check whether files exist before opening them.
- Avoid hardcoding absolute paths unless necessary.
- Organize project files into meaningful folders.

---

## ⚠️ Common Mistakes

### Hardcoding Absolute Paths

```python
open("C:\\Users\\Noor\\Desktop\\students.csv")
```

This may fail on another computer.

Prefer:

```python
Path("data") / "students.csv"
```

---

### Assuming a File Exists

Incorrect:

```python
open("config.json")
```

Better:

```python
path = Path("config.json")

if path.exists():
    with path.open() as file:
        ...
```

---

### String Concatenation for Paths

Avoid:

```python
"data/" + filename
```

Prefer:

```python
Path("data") / filename
```

---

## 📝 Interview Insight

### Question

What is the difference between an absolute path and a relative path?

### Answer

- An **absolute path** specifies the complete location of a file from the root of the file system.
- A **relative path** specifies the location relative to the current working directory.

---

### Question

Why is `pathlib` preferred over `os.path`?

### Answer

`pathlib` provides a cleaner, object-oriented interface for working with paths, improving readability and portability across operating systems.

---

### Question

How can you check if a file exists?

### Answer

Using `os`:

```python
os.path.exists("students.csv")
```

Using `pathlib`:

```python
Path("students.csv").exists()
```

---

## 💡 Remember This

| Task | `os` | `pathlib` |
|------|------|-----------|
| Current directory | `os.getcwd()` | — |
| List files | `os.listdir()` | `Path.iterdir()` |
| Check exists | `os.path.exists()` | `Path.exists()` |
| File? | `os.path.isfile()` | `Path.is_file()` |
| Directory? | `os.path.isdir()` | `Path.is_dir()` |
| Create folder | `os.mkdir()` | `Path.mkdir()` |
| Join paths | `os.path.join()` | `Path() / "file"` |

Think:

> **`os` gives functions. `pathlib` gives objects.**

---

## 🎯 Key Takeaways

- Every file has a path that tells the operating system where it is located.
- Relative paths improve project portability, while absolute paths specify an exact location.
- The `os` module provides functions for interacting with files and directories.
- `pathlib` offers a modern, object-oriented approach to working with paths and is recommended for new Python projects.
- Checking for file existence before opening it helps prevent runtime errors.
- Proper path management is essential for backend development, automation, data engineering, and AI/ML projects.

---

## 💻 Code Reference

`code/file_handling.py`