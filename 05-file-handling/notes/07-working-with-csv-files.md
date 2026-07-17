# Working with CSV Files

## 📖 Overview

A **CSV (Comma-Separated Values)** file is a text file used to store **tabular data**.

Each row represents a record, and each value is separated by a delimiter (commonly a comma).

CSV files are lightweight, human-readable, and supported by almost every programming language, spreadsheet software, and database system.

Python provides the built-in **`csv` module** to read from and write to CSV files efficiently.

---

## ❓ Why Use CSV Files?

Suppose a school stores student information.

Instead of saving it like this:

```text
Name: Noor
Age: 21
Course: BCA

Name: Aman
Age: 22
Course: B.Tech
```

It can be organized as:

```csv
Name,Age,Course
Noor,21,BCA
Aman,22,B.Tech
```

This format is easier to process programmatically.

---

# 🧠 What is a CSV File?

A CSV file stores data in rows and columns.

Example:

```csv
ID,Name,Age
1,Noor,21
2,Aman,22
3,Riya,20
```

Visual representation:

| ID | Name | Age |
|----|------|-----|
|1|Noor|21|
|2|Aman|22|
|3|Riya|20|

Each row represents one record.

---

# 🧠 The `csv` Module

Python includes the `csv` module in its standard library.

Import it using:

```python
import csv
```

No installation is required.

---

# 🧠 Reading CSV Files

Use `csv.reader()` to read rows.

Example:

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Suppose `students.csv` contains:

```csv
ID,Name,Age
1,Noor,21
2,Aman,22
```

Output

```python
['ID', 'Name', 'Age']
['1', 'Noor', '21']
['2', 'Aman', '22']
```

Each row is returned as a list of strings.

---

# 🧠 Skipping the Header

Often, the first row contains column names.

Example:

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

Output

```python
['1', 'Noor', '21']
['2', 'Aman', '22']
```

`next(reader)` skips the first row.

---

# 🧠 Writing CSV Files

Use `csv.writer()`.

Example:

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "Noor", 21])
    writer.writerow([2, "Aman", 22])
```

Generated file:

```csv
ID,Name,Age
1,Noor,21
2,Aman,22
```

---

# 🧠 Writing Multiple Rows

Use `writerows()`.

Example:

```python
import csv

rows = [
    ["ID", "Name", "Age"],
    [1, "Noor", 21],
    [2, "Aman", 22],
    [3, "Riya", 20]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(rows)
```

---

# 🧠 Using `DictReader`

Instead of lists, rows can be read as dictionaries.

Example:

```python
import csv

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Output

```python
{
    'ID': '1',
    'Name': 'Noor',
    'Age': '21'
}

{
    'ID': '2',
    'Name': 'Aman',
    'Age': '22'
}
```

This improves readability because values can be accessed using column names.

Example:

```python
print(row["Name"])
```

---

# 🧠 Using `DictWriter`

Example:

```python
import csv

with open("students.csv", "w", newline="") as file:

    fieldnames = ["ID", "Name", "Age"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "ID": 1,
        "Name": "Noor",
        "Age": 21
    })
```

Generated CSV

```csv
ID,Name,Age
1,Noor,21
```

---

# 🧠 Delimiters

Although commas are common, CSV files can use other separators.

Example:

```text
ID;Name;Age
```

Specify the delimiter:

```python
reader = csv.reader(file, delimiter=";")
```

Common delimiters:

- `,` (Comma)
- `;` (Semicolon)
- `\t` (Tab)

---

# 🧠 Why `newline=""`?

When writing CSV files:

```python
open("students.csv", "w", newline="")
```

Using `newline=""` prevents extra blank lines on some operating systems, especially Windows.

It is considered a best practice whenever using `csv.writer()`.

---

## ⚙️ Behind the Scenes

When Python reads a CSV file:

```
CSV File

↓

Read Text

↓

Split by Delimiter

↓

Convert Each Row to List / Dictionary

↓

Return to Program
```

Unlike Excel, a CSV file contains only plain text.

The `csv` module interprets that text and organizes it into rows and columns.

---

## 🌍 Real-World Applications

CSV files are widely used for:

- Student records
- Sales reports
- Banking transactions
- Employee information
- Product catalogs
- Analytics reports
- Database imports and exports
- Spreadsheet data exchange

---

## 🤖 AI Connection

CSV is the most common format for machine learning datasets.

Examples:

```csv
age,income,bought_product
25,40000,Yes
31,55000,No
29,47000,Yes
```

Typical AI workflow:

```
CSV Dataset

↓

Read with Python

↓

Preprocess Data

↓

Train Model

↓

Generate Predictions
```

Popular libraries like **Pandas**, **NumPy**, and **Scikit-learn** often load data from CSV files.

---

## 💼 Best Practices

- Always use the `csv` module instead of manually splitting strings.
- Open CSV files using the `with` statement.
- Use `newline=""` when writing.
- Prefer `DictReader` when column names matter.
- Keep headers descriptive and consistent.

---

## ⚠️ Common Mistakes

### Manually Splitting Rows

Incorrect:

```python
line.split(",")
```

Correct:

```python
csv.reader(file)
```

---

### Forgetting `newline=""`

Incorrect:

```python
open("students.csv", "w")
```

Correct:

```python
open("students.csv", "w", newline="")
```

---

### Assuming Numbers Stay as Numbers

```python
reader = csv.reader(file)
```

Every value is read as a **string**.

Example:

```python
age = int(row[2])
```

Convert values when numeric operations are needed.

---

## 📝 Interview Insight

### Question

Why should we use the `csv` module instead of reading lines manually?

### Answer

The `csv` module correctly handles delimiters, quoted values, and different CSV formats, making the code more reliable and easier to maintain.

---

### Question

What is the difference between `csv.reader()` and `csv.DictReader()`?

### Answer

| `csv.reader()` | `csv.DictReader()` |
|----------------|--------------------|
| Returns each row as a list | Returns each row as a dictionary |
| Access values by index | Access values by column name |

---

### Question

Why is `newline=""` recommended when writing CSV files?

### Answer

It prevents extra blank lines from being added on some operating systems and ensures consistent CSV formatting.

---

## 💡 Remember This

| Function | Purpose |
|----------|---------|
| `csv.reader()` | Read rows as lists |
| `csv.writer()` | Write rows |
| `writerow()` | Write one row |
| `writerows()` | Write multiple rows |
| `DictReader()` | Read rows as dictionaries |
| `DictWriter()` | Write dictionaries |

Think:

> **CSV stores tables. The `csv` module helps Python understand those tables.**

---

## 🎯 Key Takeaways

- CSV files store structured tabular data in plain text.
- Python's built-in `csv` module simplifies reading and writing CSV files.
- `csv.reader()` returns rows as lists, while `DictReader()` returns rows as dictionaries.
- `writerow()` writes a single row, and `writerows()` writes multiple rows.
- Use `newline=""` when writing CSV files to avoid formatting issues.
- CSV is one of the most widely used formats in backend development, data engineering, analytics, and AI/ML.

---

## 💻 Code Reference

`code/file_handling.py`