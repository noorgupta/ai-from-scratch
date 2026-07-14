# Nested Loops

## 📖 Overview

A nested loop is a loop inside another loop. The inner loop executes completely for every iteration of the outer loop.

Nested loops are useful when working with multi-dimensional data, patterns, matrices, and combinations of elements.

---

## ❓ Why Do We Need Nested Loops?

Some problems require multiple levels of repetition.

For example:

- Printing patterns
- Processing rows and columns of a matrix
- Comparing every element with every other element
- Generating combinations of values

A single loop cannot efficiently solve these problems.

---

## 🧠 Syntax

```python
for outer in sequence:
    for inner in sequence:
        # code to execute
```

A `while` loop can also be nested inside another `while` loop or inside a `for` loop.

---

## 💻 Examples

### Example 1: Basic Nested Loop

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

**Output**

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

---

### Example 2: Pattern Printing

```python
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
```

**Output**

```text
* * *
* * *
* * *
```

---

## ⚙️ How It Works

Suppose we execute:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

Execution order:

```
Outer Loop → i = 0
    Inner Loop → j = 0
    Inner Loop → j = 1
    Inner Loop → j = 2

Outer Loop → i = 1
    Inner Loop → j = 0
    Inner Loop → j = 1
    Inner Loop → j = 2
```

The inner loop completes all its iterations before the outer loop moves to the next iteration.

---

## 🌍 Real-World Applications

Nested loops are commonly used in:

- Matrix operations
- Pattern generation
- Tables and grids
- Comparing datasets
- Game development

---

## 🤖 AI Connection

Nested loops are used in AI and Machine Learning for:

- Processing images pixel by pixel
- Traversing matrices and tensors
- Comparing features in datasets
- Distance calculations
- Grid-based algorithms

Although modern AI libraries optimize these operations internally, understanding nested loops helps build strong programming and algorithmic thinking.

---

## ⚠️ Common Mistakes

### Confusing the outer and inner loops

Remember:

- The outer loop controls the number of repetitions.
- The inner loop completes all its iterations for each outer loop iteration.

---

### Excessive Nesting

Too many nested loops can make programs slower and harder to read.

Whenever possible, use efficient algorithms or built-in Python functions.

---

## 💡 Remember This

- A nested loop is simply a loop inside another loop.
- The inner loop finishes completely before the outer loop continues.
- Nested loops are commonly used for matrices, patterns, and multi-dimensional data.

---

## 🎯 Key Takeaways

- Nested loops allow multiple levels of iteration.
- They are useful for solving complex repetitive tasks.
- Understanding nested loops is important for DSA, AI, and matrix-based computations.

---

## 💻 Code Reference

`code/05-nested-loops.py`