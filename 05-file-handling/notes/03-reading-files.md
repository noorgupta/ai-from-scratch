# Reading Files

## 📖 Overview

Once a file has been opened, Python provides several methods to read its contents.

Depending on your requirement, you can:

- Read the entire file.
- Read a fixed number of characters.
- Read one line at a time.
- Read all lines into a list.

Choosing the appropriate reading method improves performance, especially when working with large files.

---

## ❓ Why Do We Need Different Reading Methods?

Imagine reading a 500-page book.

Sometimes you want to:

- Read the whole book.
- Read one page.
- Read one paragraph.
- Read a few words.

Python offers similar flexibility when reading files.

```
File
 │
 ├── Read Everything
 ├── Read Some Characters
 ├── Read One Line
 └── Read All Lines
```

---

# 🧠 The `read()` Method

The `read()` method reads the entire contents of a file.

Example:

```python
file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()
```

Suppose `notes.txt` contains:

```text
Python
Machine Learning
Artificial Intelligence
```

**Output**

```text
Python
Machine Learning
Artificial Intelligence
```

---

# 🧠 Reading a Fixed Number of Characters

`read(size)` reads only the specified number of characters.

```python
file = open("notes.txt")

print(file.read(6))

file.close()
```

**Output**

```text
Python
```

The next call continues from where the previous one stopped.

```python
file = open("notes.txt")

print(file.read(6))

print(file.read(7))

file.close()
```

Example Output

```text
Python

Machine
```

Python does **not** start reading from the beginning again.

---

# 🧠 The File Pointer

Whenever Python reads a file, it keeps track of the current reading position.

This position is called the **file pointer**.

Example:

```
Python Programming

^

Pointer starts here
```

After:

```python
file.read(7)
```

```
Python Programming

       ^

Pointer moves here
```

Every read operation continues from the current pointer location.

---

# 🧠 The `readline()` Method

`readline()` reads only one line.

Example:

```python
file = open("notes.txt")

print(file.readline())

print(file.readline())

file.close()
```

Suppose the file contains:

```text
Python
AI
ML
```

**Output**

```text
Python

AI
```

Each call reads the next line.

---

# 🧠 The `readlines()` Method

`readlines()` reads every line and stores them inside a list.

Example:

```python
file = open("notes.txt")

lines = file.readlines()

print(lines)

file.close()
```

**Output**

```python
[
    "Python\n",
    "AI\n",
    "ML"
]
```

Notice that each line keeps its newline character (`\n`) except possibly the last line.

---

# 🧠 Reading Files Using a Loop

Instead of loading everything into memory, we can read line by line.

```python
file = open("notes.txt")

for line in file:
    print(line.strip())

file.close()
```

**Output**

```text
Python
AI
ML
```

`strip()` removes the newline character.

This approach is preferred for large files.

---

# 🧠 End of File (EOF)

Python stops reading when it reaches the **End of File (EOF)**.

Example:

```python
file = open("notes.txt")

print(file.read())

print(file.read())

file.close()
```

Output

```text
Python
AI
ML

''
```

The second `read()` returns an empty string because the pointer is already at the end.

---

# 🧠 Moving the File Pointer

Sometimes we want to read the file again.

Python provides:

```python
seek(position)
```

Example:

```python
file = open("notes.txt")

print(file.read())

file.seek(0)

print(file.read())

file.close()
```

The pointer moves back to the beginning.

---

# 🧠 Checking Current Position

Python also provides:

```python
tell()
```

Example:

```python
file = open("notes.txt")

print(file.tell())

file.read(5)

print(file.tell())

file.close()
```

Possible Output

```text
0

5
```

`tell()` returns the current position of the file pointer.

---

## ⚙️ Behind the Scenes

When Python reads a file:

```
Storage Device

↓

Operating System

↓

Buffer

↓

Python File Object

↓

Your Program
```

Python usually reads data into a memory buffer before giving it to your program. This reduces the number of slow disk operations and improves performance.

---

## 🌍 Real-World Applications

Reading files is used in:

- Loading configuration files.
- Reading application logs.
- Importing CSV datasets.
- Reading JSON APIs stored locally.
- Loading HTML templates.
- Reading user-uploaded documents.
- Parsing reports.

---

## 🤖 AI Connection

Reading files is fundamental in AI.

Examples:

```python
with open("train.csv") as file:
```

Load training datasets.

```python
with open("prompts.txt") as file:
```

Load prompts for LLM applications.

```python
with open("config.json") as file:
```

Read model configuration.

```python
with open("vocabulary.txt") as file:
```

Load NLP vocabularies.

Almost every AI pipeline begins by reading one or more files.

---

## 💼 Best Practices

- Use the appropriate reading method for your task.
- Use loops for very large files.
- Prefer the `with` statement (covered later).
- Avoid loading extremely large files entirely into memory.
- Use `strip()` when reading line-by-line to remove unwanted newline characters.

---

## ⚠️ Common Mistakes

### Forgetting That `read()` Moves the Pointer

```python
file.read()

file.read()
```

The second call usually returns an empty string because the pointer is already at the end.

---

### Using `read()` for Huge Files

Avoid:

```python
content = file.read()
```

for multi-GB files.

Instead:

```python
for line in file:
    ...
```

---

### Forgetting Newline Characters

```python
print(file.readline())
```

may produce extra blank lines because the line already contains `\n`.

Use:

```python
print(file.readline().strip())
```

---

## 📝 Interview Insight

### Question

What is the difference between `read()`, `readline()`, and `readlines()`?

### Answer

| Method | Returns |
|---------|----------|
| `read()` | Entire file or specified number of characters |
| `readline()` | One line |
| `readlines()` | List containing all lines |

---

### Question

What is the file pointer?

### Answer

The file pointer is the current position from which Python reads or writes data. It automatically moves as data is processed.

---

## 💡 Remember This

| Method | Purpose |
|---------|----------|
| `read()` | Entire file |
| `read(size)` | Fixed number of characters |
| `readline()` | One line |
| `readlines()` | All lines as a list |
| `seek()` | Move pointer |
| `tell()` | Current pointer position |

Think:

> **Read what you need—not always everything.**

---

## 🎯 Key Takeaways

- Python provides multiple methods for reading files.
- `read()` reads the entire file or a specified number of characters.
- `readline()` reads one line at a time.
- `readlines()` returns all lines as a list.
- The file pointer tracks the current read position.
- `seek()` repositions the pointer, while `tell()` reports its current location.
- Reading files efficiently is essential for backend development, automation, data analysis, and AI/ML.

---

## 💻 Code Reference

`code/file_handling.py`