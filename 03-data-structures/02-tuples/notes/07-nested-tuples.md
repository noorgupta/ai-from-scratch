# Nested Tuples

## 📖 Overview

A nested tuple is a tuple that contains one or more tuples as its elements.

It allows us to organize related data into multiple levels while keeping the entire structure immutable.

Nested tuples are useful when representing structured information such as coordinates, records, or grouped data.

---

## ❓ Why Do We Need Nested Tuples?

Sometimes data naturally belongs in groups.

For example:

- Student records
- Product details
- GPS coordinates
- Monthly reports
- RGB color collections

Instead of storing everything in one long tuple, nested tuples improve organization and readability.

---

## 🧠 Creating a Nested Tuple

```python
students = (
    ("Noor", 20),
    ("Aman", 21),
    ("Priya", 19)
)
```

Here,

- The outer tuple contains three tuples.
- Each inner tuple represents one student's record.

---

## 🧠 Accessing Elements

Use multiple indexes to access nested elements.

```python
students = (
    ("Noor", 20),
    ("Aman", 21),
    ("Priya", 19)
)

print(students[1][0])
```

**Output**

```text
Aman
```

Explanation:

- `students[1]` → `("Aman", 21)`
- `students[1][0]` → `"Aman"`

---

## 🧠 Traversing Nested Tuples

Nested tuples are commonly traversed using nested loops.

```python
students = (
    ("Noor", 20),
    ("Aman", 21),
    ("Priya", 19)
)

for student in students:
    for value in student:
        print(value, end=" ")
    print()
```

**Output**

```text
Noor 20
Aman 21
Priya 19
```

---

## 🧠 Tuple Inside Tuple Inside Tuple

Python supports multiple levels of nesting.

```python
data = (
    ("AI", ("Machine Learning", "Deep Learning")),
    ("Web", ("HTML", "CSS"))
)
```

Accessing `"Deep Learning"`:

```python
print(data[0][1][1])
```

**Output**

```text
Deep Learning
```

---

## ⚙️ How It Works

```
students

                Outer Tuple
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 ("Noor",20)   ("Aman",21)   ("Priya",19)
```

Python first accesses the required inner tuple, then retrieves the desired element using another index.

---

## 🌍 Real-World Applications

Nested tuples are commonly used for:

- Student records
- Employee details
- Geographic coordinates
- Product information
- Database query results
- Configuration settings

---

## 🤖 AI Connection

Nested tuples are frequently used in AI and scientific computing.

Examples include:

- Storing image dimensions.
- Representing bounding boxes.
- Returning multiple groups of results.
- Organizing model metadata.
- Storing coordinates and labels.

Many Python libraries return nested tuples to represent structured, read-only information.

---

## 💼 Best Practices

- Keep nesting levels reasonable.
- Use descriptive variable names.
- Choose tuples when the grouped data should remain unchanged.

---

## ⚠️ Common Mistakes

### Forgetting the second index

```python
students[1]
```

Output

```python
("Aman", 21)
```

This returns the entire inner tuple.

To access the age:

```python
students[1][1]
```

---

### Trying to Modify an Inner Tuple

```python
students[0][0] = "Rahul"
```

Raises

```text
TypeError
```

because tuples are immutable.

---

## 📝 Interview Insight

**Question:**

Can a nested tuple contain mutable objects?

**Answer:**

Yes.

Example:

```python
data = (
    [1, 2, 3],
    "Python"
)
```

The tuple itself is immutable, but the list inside it can still be modified.

---

## 💡 Remember This

- A nested tuple contains other tuples.
- Access nested values using multiple indexes.
- Traverse nested tuples using nested loops.
- Tuples themselves remain immutable.

---

## 🎯 Key Takeaways

- Nested tuples organize structured data efficiently.
- Each inner tuple behaves like a normal tuple.
- Nested indexing retrieves specific values.
- Nested tuples are useful for representing grouped, read-only data.

---