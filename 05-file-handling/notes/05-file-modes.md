# File Modes

## 📖 Overview

Whenever a file is opened in Python, you must specify **how** you want to interact with it.

This is done using **file modes**.

A file mode tells Python whether you want to:

- Read data
- Write data
- Append data
- Create a new file
- Work with binary files
- Work with text files
- Perform both reading and writing

Choosing the correct mode prevents accidental data loss and ensures your program behaves as expected.

---

## ❓ Why Do We Need File Modes?

Imagine a library.

Different visitors have different permissions.

```
Library

│

├── Read Books
├── Write New Books
├── Add Pages
├── Read + Edit
└── Create New Books
```

Similarly, Python needs to know what kind of access you require before opening a file.

---

# 🧠 Read Mode (`r`)

The `"r"` mode opens a file for **reading only**.

```python
file = open("notes.txt", "r")
```

Characteristics:

- Default mode
- File must already exist
- Cannot modify the file
- Pointer starts at the beginning

If the file does not exist:

```text
FileNotFoundError
```

Use cases:

- Reading configuration files
- Loading datasets
- Viewing reports

---

# 🧠 Write Mode (`w`)

The `"w"` mode opens a file for writing.

```python
file = open("notes.txt", "w")
```

Characteristics:

- Creates file if it doesn't exist
- Deletes existing content
- Pointer starts at the beginning

Use cases:

- Creating reports
- Exporting results
- Replacing outdated files

---

# 🧠 Append Mode (`a`)

The `"a"` mode adds new data to the end of a file.

```python
file = open("notes.txt", "a")
```

Characteristics:

- Preserves existing content
- Creates file if missing
- Pointer starts at the end

Use cases:

- Log files
- Activity history
- Error reports

---

# 🧠 Exclusive Creation Mode (`x`)

The `"x"` mode creates a **new** file.

```python
file = open("notes.txt", "x")
```

Characteristics:

- Creates a new file
- Raises an error if the file already exists

If the file exists:

```text
FileExistsError
```

Use cases:

- Prevent accidental overwriting
- Generate unique reports
- Secure file creation

---

# 🧠 Text Mode (`t`)

Text mode is used for human-readable files.

Examples:

```text
.txt
.csv
.json
.html
.css
.py
```

```python
file = open("notes.txt", "rt")
```

Since text mode is the default, `"t"` is usually omitted.

Equivalent:

```python
open("notes.txt")

open("notes.txt", "rt")
```

---

# 🧠 Binary Mode (`b`)

Binary mode works with raw bytes.

Examples:

```text
.jpg
.png
.pdf
.mp3
.mp4
.exe
```

```python
file = open("photo.jpg", "rb")
```

Binary mode is essential for files that are not plain text.

---

# 🧠 Update Mode (`+`)

The `"+"` symbol allows both reading and writing.

It is combined with other modes.

Examples:

```
r+
w+
a+
```

---

# 🧠 `r+`

Read and write.

```python
file = open("notes.txt", "r+")
```

Characteristics:

- File must exist
- Does not erase content
- Pointer starts at the beginning

Use cases:

- Modify existing files
- Update records

---

# 🧠 `w+`

Read and write.

```python
file = open("notes.txt", "w+")
```

Characteristics:

- Creates file if needed
- Erases existing content
- Allows reading and writing

Use cases:

- Generate fresh reports
- Temporary processing files

---

# 🧠 `a+`

Append and read.

```python
file = open("notes.txt", "a+")
```

Characteristics:

- Preserves content
- Adds new data at the end
- Allows reading
- Creates file if missing

Use cases:

- Log management
- Chat history
- Audit records

---

# 🧠 Common Binary Combinations

Read binary:

```python
open("image.png", "rb")
```

Write binary:

```python
open("image.png", "wb")
```

Append binary:

```python
open("video.mp4", "ab")
```

Read and write binary:

```python
open("weights.bin", "rb+")
```

---

# 📊 Summary of File Modes

| Mode | Read | Write | Create if Missing | Overwrite Existing | Pointer Position |
|------|------|-------|-------------------|--------------------|------------------|
| `r` | ✅ | ❌ | ❌ | ❌ | Beginning |
| `w` | ❌ | ✅ | ✅ | ✅ | Beginning |
| `a` | ❌ | ✅ | ✅ | ❌ | End |
| `x` | ❌ | ✅ | ✅ | ❌ (Error if exists) | Beginning |
| `r+` | ✅ | ✅ | ❌ | ❌ | Beginning |
| `w+` | ✅ | ✅ | ✅ | ✅ | Beginning |
| `a+` | ✅ | ✅ | ✅ | ❌ | End |

---

## ⚙️ Behind the Scenes

When you call:

```python
open("data.txt", "r")
```

Python:

1. Verifies the file exists.
2. Checks read permissions.
3. Creates a file object.
4. Sets the pointer to the beginning.

Different modes simply change the permissions and the initial position of the file pointer.

---

## 🌍 Real-World Applications

Different file modes are used depending on the application's needs.

Examples:

| Scenario | Mode |
|----------|------|
| Read configuration | `r` |
| Save report | `w` |
| Maintain logs | `a` |
| Create unique file | `x` |
| Update records | `r+` |
| Read image | `rb` |
| Save PDF | `wb` |
| Append chat messages | `a+` |

---

## 🤖 AI Connection

File modes are widely used in AI and Machine Learning.

Examples:

### Read dataset

```python
open("train.csv", "r")
```

### Save predictions

```python
open("predictions.csv", "w")
```

### Append training logs

```python
open("training.log", "a")
```

### Load model weights

```python
open("model.bin", "rb")
```

### Save serialized models

```python
open("model.pkl", "wb")
```

Choosing the correct file mode is essential to avoid corrupting datasets or trained models.

---

## 💼 Best Practices

- Use `"r"` when you only need to read.
- Use `"w"` only when replacing existing content is intentional.
- Use `"a"` for logs and historical records.
- Use `"x"` when accidental overwriting must be prevented.
- Use binary modes for images, videos, PDFs, and serialized objects.
- Prefer the least permissive mode needed for the task.

---

## ⚠️ Common Mistakes

### Accidentally Using `"w"`

```python
open("students.txt", "w")
```

This erases the file before writing.

---

### Reading Binary Files as Text

Incorrect:

```python
open("photo.jpg", "r")
```

Correct:

```python
open("photo.jpg", "rb")
```

---

### Forgetting That `r` Requires an Existing File

```python
open("missing.txt", "r")
```

Raises:

```text
FileNotFoundError
```

---

### Assuming `a` Starts Writing at the Beginning

```python
open("log.txt", "a")
```

The pointer starts at the **end**, so new content is appended.

---

## 📝 Interview Insight

### Question

Which mode is the default in Python?

**Answer**

`"r"` (Read mode)

---

### Question

Which mode preserves existing content?

**Answer**

`"a"` (Append mode)

---

### Question

Which mode creates a new file and raises an error if it already exists?

**Answer**

`"x"` (Exclusive creation mode)

---

### Question

Which mode is used for images or PDFs?

**Answer**

Binary mode (`"rb"`, `"wb"`, `"ab"`)

---

## 💡 Remember This

| Mode | Think Of |
|------|----------|
| `r` | Read |
| `w` | Replace |
| `a` | Add |
| `x` | Create Only |
| `b` | Bytes |
| `t` | Text |
| `+` | Read + Write |

**Easy memory trick:**

- **R** → Read
- **W** → Wipe & Write
- **A** → Add
- **X** → eXclusive Create
- **B** → Binary
- **T** → Text
- **+** → Both Read & Write

---

## 🎯 Key Takeaways

- File modes define how Python interacts with a file.
- `"r"` is the default mode for reading existing files.
- `"w"` overwrites existing content or creates a new file.
- `"a"` appends data while preserving existing content.
- `"x"` safely creates a new file and prevents accidental overwrites.
- Binary modes (`"rb"`, `"wb"`) are used for non-text files like images, PDFs, and model files.
- Choosing the correct mode is essential for reliable backend systems, automation scripts, and AI/ML applications.

---

## 💻 Code Reference

`code/file_handling.py`