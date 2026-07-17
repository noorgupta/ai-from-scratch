# Opening and Closing Files

## 📖 Overview

Before Python can read from or write to a file, it must first **open** the file.

Opening a file creates a connection between your Python program and the file stored on your computer.

Once the required operations are completed, the file should be **closed** to release system resources and ensure all changes are properly saved.

Python provides the built-in `open()` function to open files and the `close()` method to close them.

---

## ❓ Why Do We Need to Open a File?

Imagine a book kept inside a library.

Before you can read or write anything, you must first open the book.

```
Book Closed
      │
      ▼
Open Book
      │
      ▼
Read / Write
      │
      ▼
Close Book
```

Files work the same way.

Python cannot directly access a file until it has been opened.

---

# 🧠 The `open()` Function

Python uses the built-in `open()` function to open a file.

Basic syntax:

```python
file = open("example.txt")
```

Here:

- `"example.txt"` is the file name.
- `open()` returns a **file object**.
- The file object is stored in the variable `file`.

---

# 🧠 What is a File Object?

A **file object** represents the opened file.

It acts as a bridge between your Python program and the actual file stored on disk.

Example:

```python
file = open("notes.txt")

print(file)
```

Possible Output:

```text
<_io.TextIOWrapper name='notes.txt' mode='r' encoding='UTF-8'>
```

The exact output may vary depending on your operating system and Python version, but it indicates that Python has successfully opened the file and created a file object.

---

# 🧠 Opening an Existing File

If the file already exists:

```python
file = open("students.txt")
```

Python opens the file and returns a file object.

You can now read from or write to the file (depending on the mode used).

---

# 🧠 Opening a New File

Some file modes automatically create a new file if it does not already exist.

Example:

```python
file = open("report.txt", "w")
```

If `report.txt` does not exist, Python creates it automatically.

---

# 🧠 Closing a File

Once you finish working with a file, close it using the `close()` method.

```python
file = open("students.txt")

file.close()
```

Closing the file informs the operating system that your program has finished using it.

---

# 🧠 Why Closing Files is Important

Closing files is considered a best practice because it:

- Frees system resources.
- Ensures all buffered data is written to disk.
- Prevents accidental file corruption.
- Allows other programs to access the file safely.

---

# 🧠 What Happens If You Forget to Close a File?

If a file remains open:

- Memory may not be released immediately.
- Data may not be completely written.
- Other programs may be unable to modify the file.
- Long-running applications may eventually run out of available file handles.

Modern operating systems usually close files when the program exits, but relying on this behavior is not recommended.

---

# 🧠 Checking Whether a File is Closed

Every file object has a `closed` attribute.

Example:

```python
file = open("notes.txt")

print(file.closed)

file.close()

print(file.closed)
```

**Output**

```text
False

True
```

- `False` → File is still open.
- `True` → File has been closed.

---

## ⚙️ Behind the Scenes

When you call:

```python
file = open("notes.txt")
```

Python performs the following steps:

1. Requests the operating system to locate the file.
2. Verifies that your program has permission to access it.
3. Opens the file.
4. Creates a file object.
5. Returns the file object to your program.

Conceptually:

```text
Python Program
        │
        ▼
open("notes.txt")
        │
        ▼
Operating System
        │
        ▼
Storage Device (SSD/HDD)
        │
        ▼
File Object Returned
```

The file object is then used for all future operations on that file.

---

## 🌍 Real-World Applications

Opening and closing files is required in:

- Reading configuration files.
- Loading datasets.
- Saving reports.
- Exporting invoices.
- Reading uploaded documents.
- Processing log files.
- Managing application settings.

---

## 🤖 AI Connection

Almost every AI project begins by opening one or more files.

Examples:

```python
dataset = open("train.csv")
```

```python
config = open("config.json")
```

```python
model = open("weights.bin", "rb")
```

Before a model can train or make predictions, Python must first open the required files containing datasets, configurations, or saved model weights.

---

## 💼 Best Practices

- Always close files after use.
- Use descriptive file names.
- Store the returned file object in a meaningful variable.
- Check for file existence when appropriate.
- Prefer the `with` statement for automatic file management (covered in a later lesson).

---

## ⚠️ Common Mistakes

### Forgetting to Close Files

```python
file = open("data.txt")
```

The file remains open until the program exits or it is explicitly closed.

---

### Assuming `open()` Reads the File

```python
file = open("data.txt")
```

This only opens the file.

It does **not** read its contents.

Reading requires methods such as:

- `read()`
- `readline()`
- `readlines()`

---

### Using an Incorrect File Name

```python
file = open("student.txt")
```

If the file does not exist (in read mode), Python raises:

```text
FileNotFoundError
```

---

## 📝 Interview Insight

### Question

What does the `open()` function return?

### Answer

The `open()` function returns a **file object**, which is used to perform operations such as reading, writing, and closing the file.

---

### Question

Why should files be closed?

### Answer

Closing files:

- Releases system resources.
- Ensures all data is saved correctly.
- Prevents resource leaks.
- Allows other programs to access the file safely.

---

## 💡 Remember This

```
File

↓

open()

↓

File Object

↓

Read / Write

↓

close()
```

Think:

> **Open → Work → Close**

---

## 🎯 Key Takeaways

- `open()` is used to access files.
- `open()` returns a file object.
- A file object provides methods for reading, writing, and closing files.
- Closing files releases resources and protects data integrity.
- Opening a file does not automatically read its contents.
- Proper file management is essential in backend development, automation, and AI/ML.

---

## 💻 Code Reference

`code/file_handling.py`