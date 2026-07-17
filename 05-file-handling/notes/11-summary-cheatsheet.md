# 📋 File Handling Cheatsheet

A quick reference guide for Python File Handling.

---

# 📂 File Handling Workflow

```
Open File
     │
     ▼
Read / Write / Append
     │
     ▼
Close File
```

**Recommended way:**

```python
with open("file.txt", "r") as file:
    data = file.read()
```

The `with` statement automatically closes the file.

---

# 📖 Opening Files

```python
open("file.txt")
```

Default mode:

```python
open("file.txt", "r")
```

General syntax:

```python
open(file_name, mode)
```

---

# 📖 Reading Files

Read entire file

```python
file.read()
```

Read fixed number of characters

```python
file.read(10)
```

Read one line

```python
file.readline()
```

Read all lines

```python
file.readlines()
```

Read line-by-line

```python
for line in file:
    print(line.strip())
```

---

# ✍️ Writing Files

Write text

```python
file.write("Hello")
```

Write multiple lines

```python
file.writelines(lines)
```

Append data

```python
file.write("\nNew Line")
```

---

# 📌 File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read |
| `w` | Write (Overwrite) |
| `a` | Append |
| `x` | Create New File |
| `b` | Binary Mode |
| `t` | Text Mode |
| `+` | Read and Write |

---

## Common Mode Combinations

| Mode | Description |
|------|-------------|
| `rb` | Read Binary |
| `wb` | Write Binary |
| `ab` | Append Binary |
| `r+` | Read + Write |
| `w+` | Write + Read |
| `a+` | Append + Read |

---

# 📌 File Pointer

Current position

```python
file.tell()
```

Move pointer

```python
file.seek(0)
```

---

# 📌 File Object

```python
file.closed
```

Returns

```text
True
```

or

```text
False
```

---

# 📌 CSV Quick Reference

Import

```python
import csv
```

Read CSV

```python
csv.reader(file)
```

Write CSV

```python
csv.writer(file)
```

Read as dictionary

```python
csv.DictReader(file)
```

Write dictionary

```python
csv.DictWriter(file)
```

Write one row

```python
writer.writerow(row)
```

Write multiple rows

```python
writer.writerows(rows)
```

---

# 📌 JSON Quick Reference

Import

```python
import json
```

Read JSON file

```python
json.load(file)
```

Read JSON string

```python
json.loads(text)
```

Write JSON file

```python
json.dump(data, file)
```

Convert object to JSON string

```python
json.dumps(data)
```

Pretty print

```python
json.dump(data, file, indent=4)
```

---

# 📌 `os` Module

Import

```python
import os
```

Current directory

```python
os.getcwd()
```

List files

```python
os.listdir()
```

Create directory

```python
os.mkdir("data")
```

Create nested directories

```python
os.makedirs("data/archive")
```

Rename file

```python
os.rename("old.txt", "new.txt")
```

Delete file

```python
os.remove("notes.txt")
```

Check existence

```python
os.path.exists("data.txt")
```

Check file

```python
os.path.isfile("data.txt")
```

Check directory

```python
os.path.isdir("data")
```

---

# 📌 `pathlib` Quick Reference

Import

```python
from pathlib import Path
```

Create path

```python
Path("data/file.txt")
```

Join paths

```python
Path("data") / "file.txt"
```

Exists

```python
path.exists()
```

Is file

```python
path.is_file()
```

Is directory

```python
path.is_dir()
```

Create directory

```python
Path("reports").mkdir()
```

Open file

```python
with path.open():
```

---

# 📌 Common Exceptions

| Exception | Meaning |
|-----------|---------|
| `FileNotFoundError` | File doesn't exist |
| `PermissionError` | No permission |
| `FileExistsError` | File already exists |
| `IsADirectoryError` | Expected file, got directory |
| `NotADirectoryError` | Expected directory, got file |
| `UnicodeDecodeError` | Encoding issue |

---

# 📌 Best Practices Checklist

✅ Use the `with` statement.

✅ Prefer `pathlib` for new projects.

✅ Check file existence before processing.

✅ Use relative paths.

✅ Handle expected exceptions.

✅ Close files automatically.

✅ Keep project folders organized.

✅ Use meaningful file names.

✅ Store configuration in JSON.

✅ Store tabular data in CSV.

---

# 📌 Memory Tricks

### File Modes

```
R → Read

W → Wipe & Write

A → Add

X → eXclusive Create

B → Binary

T → Text

+ → Read & Write
```

---

### JSON Functions

```
load()

↓

File

------------------

loads()

↓

String

------------------

dump()

↓

File

------------------

dumps()

↓

String
```

---

### Reading Methods

```
read()

↓

Entire File

----------------

readline()

↓

One Line

----------------

readlines()

↓

List of Lines
```

---

### File Pointer

```
tell()

↓

Current Position

----------------

seek()

↓

Move Position
```

---

# 📌 Interview Revision

### What does `open()` return?

A file object.

---

### Which mode is default?

`r`

---

### Which mode preserves existing data?

`a`

---

### Which mode overwrites existing data?

`w`

---

### Which mode creates a new file only?

`x`

---

### Why use `with`?

Automatic resource management and file closing.

---

### Difference between `read()` and `readline()`?

- `read()` reads the entire file.
- `readline()` reads one line.

---

### Difference between `load()` and `loads()`?

- `load()` → File
- `loads()` → String

---

### Difference between `dump()` and `dumps()`?

- `dump()` → File
- `dumps()` → String

---

### CSV vs JSON

| CSV | JSON |
|------|------|
| Tabular data | Structured objects |
| Rows & columns | Key-value pairs |
| Common in datasets | Common in APIs |

---

### `os` vs `pathlib`

| `os` | `pathlib` |
|------|-----------|
| Functional | Object-oriented |
| Older approach | Modern approach |
| More verbose | Cleaner syntax |

---

# 🎯 Module Summary

After completing this module, you can:

- Open and close files safely.
- Read and write text files.
- Append data without overwriting.
- Understand every file mode.
- Use the `with` statement confidently.
- Work with CSV and JSON files.
- Manage paths using `os` and `pathlib`.
- Handle common file-related exceptions.
- Follow professional file-handling best practices.

These skills form the foundation for backend development, automation, data engineering, and AI/ML projects.

---

## 💻 Code Reference

`code/file_handling.py`