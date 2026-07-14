# `for` Loop

## 📖 Overview

A `for` loop is used to execute a block of code repeatedly by iterating over a sequence such as a string, list, tuple, dictionary, set, or a range of numbers.

Unlike a `while` loop, a `for` loop is generally used when the number of iterations is known or when iterating through a collection of data.

---

## ❓ Why Do We Need a `for` Loop?

Imagine displaying the same message 100 times.

Without a loop, you would have to write:

```python
print("Hello")
print("Hello")
print("Hello")
...
```

This approach is repetitive, time-consuming, and difficult to maintain.

A `for` loop allows you to perform the same task with just a few lines of code.

---

## 🧠 Syntax

```python
for variable in sequence:
    # code to execute
```

---

## 💻 Examples

### Using `range()`

```python
for i in range(5):
    print(i)
```

**Output**

```text
0
1
2
3
4
```

---

### Iterating Over a String

```python
for letter in "Python":
    print(letter)
```

---

### Iterating Over a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

## ⚙️ How It Works

When Python encounters a `for` loop:

1. It takes the first item from the sequence.
2. Assigns it to the loop variable.
3. Executes the loop body.
4. Moves to the next item.
5. Repeats until all items have been processed.

After the last item, the loop automatically stops.

---

## 🌍 Real-World Applications

`for` loops are commonly used for:

- Processing lists of products
- Reading files line by line
- Sending emails to multiple users
- Displaying records from a database
- Generating reports

---

## 🤖 AI Connection

`for` loops are extensively used in AI and Machine Learning.

Examples include:

- Iterating through datasets
- Training models over multiple epochs
- Processing batches of data
- Calculating evaluation metrics
- Making predictions for multiple inputs

Without loops, handling large datasets efficiently would be nearly impossible.

---

## ⚠️ Common Mistakes

### Forgetting the colon (`:`)

```python
for i in range(5)
```

Correct:

```python
for i in range(5):
```

---

### Incorrect indentation

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

### Modifying the loop variable unnecessarily

```python
for i in range(5):
    i = 100
```

Changing the loop variable does not affect the sequence being iterated.

---

## 💡 Remember This

- A `for` loop is used to iterate over sequences.
- It automatically stops after processing all items.
- It is ideal when the number of iterations is known or when working with collections.

---

## 🎯 Key Takeaways

- The `for` loop simplifies repetitive tasks.
- It can iterate over strings, lists, tuples, dictionaries, sets, and ranges.
- It is one of the most commonly used loops in Python and AI applications.

---

## 💻 Code Reference

```text
code/02-for-loop.py
```