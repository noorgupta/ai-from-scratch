# Recursion

## 📖 Overview

**Recursion** is a programming technique in which a function calls itself to solve a problem.

Instead of solving the entire problem at once, recursion breaks it into smaller, similar subproblems until it reaches a condition where no further recursion is needed.

That stopping condition is called the **base case**.

Recursion is widely used in algorithms involving trees, graphs, file systems, parsing, and Artificial Intelligence.

---

## ❓ Why Do We Need Recursion?

Imagine climbing a staircase.

To reach the top:

- Step to the next stair.
- Repeat the same action.
- Stop when you reach the last stair.

The same idea applies to recursion.

```
Problem
   │
   ▼
Smaller Problem
   │
   ▼
Even Smaller Problem
   │
   ▼
Base Case
```

Each recursive call works on a smaller version of the original problem.

---

# 🧠 How Recursion Works

Every recursive function has two essential parts.

### 1. Base Case

The condition that stops recursion.

### 2. Recursive Case

The part where the function calls itself.

Without a base case, recursion never ends.

---

# 🧠 Example 1: Counting Down

```python
def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

**Output**

```text
5
4
3
2
1
Done!
```

Each call reduces the value of `n` until it reaches the base case.

---

# 🧠 Example 2: Factorial

Mathematically,

```
5!

=

5 × 4 × 3 × 2 × 1
```

Recursive definition:

```
n!

=

n × (n-1)!
```

Base case:

```
0! = 1
```

Python:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

**Output**

```text
120
```

---

# 🧠 Call Stack Visualization

Calling:

```python
factorial(4)
```

Creates:

```
factorial(4)

↓

4 × factorial(3)

↓

4 × 3 × factorial(2)

↓

4 × 3 × 2 × factorial(1)

↓

4 × 3 × 2 × 1 × factorial(0)

↓

1
```

Then the calls return in reverse order:

```
1

↓

1

↓

2

↓

6

↓

24
```

Each function waits for the next recursive call to finish before returning.

---

# 🧠 Example 3: Fibonacci Numbers

Sequence:

```
0

1

1

2

3

5

8

13
```

Recursive implementation:

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```

**Output**

```text
8
```

Although elegant, this implementation is inefficient because it recalculates the same values many times.

---

# 🧠 Infinite Recursion

Incorrect:

```python
def hello():

    print("Hello")

    hello()
```

Python eventually raises:

```text
RecursionError:
maximum recursion depth exceeded
```

Always include a valid base case.

---

# 🧠 Recursion vs Iteration

Recursive countdown:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

Iterative countdown:

```python
for i in range(5, 0, -1):
    print(i)
```

Both solve the same problem.

Choose the approach that best balances readability and efficiency.

---

## ⚙️ Behind the Scenes

Each recursive call creates a **new stack frame**.

Example:

```python
factorial(3)
```

Conceptually:

```text
Top of Stack

factorial(0)

↓

factorial(1)

↓

factorial(2)

↓

factorial(3)

Bottom of Stack
```

When the base case is reached, Python removes each stack frame one by one.

This process is called **stack unwinding**.

---

## 📊 Time and Space Complexity

### Factorial

| Complexity | Value |
|------------|-------|
| Time | O(n) |
| Space | O(n) |

---

### Recursive Fibonacci

| Complexity | Value |
|------------|-------|
| Time | O(2ⁿ) |
| Space | O(n) |

This is why iterative or dynamic programming solutions are preferred for Fibonacci in real-world applications.

---

## 🌍 Real-World Applications

Recursion is widely used in:

- File system traversal
- Directory searching
- Expression parsing
- XML/JSON parsing
- Tree traversal
- Graph traversal
- Backtracking algorithms
- Divide-and-conquer algorithms

---

## 🤖 AI Connection

Recursion plays an important role in AI and computer science.

Examples include:

- Decision tree traversal
- Game tree search (Minimax)
- Depth-First Search (DFS)
- Recursive neural network concepts
- Parsing syntax trees
- Backtracking for constraint satisfaction
- Hierarchical clustering

Many AI algorithms naturally work on recursive data structures such as trees and graphs.

---

## 💼 Best Practices

- Always define a clear base case.
- Ensure each recursive call moves closer to the base case.
- Prefer iteration for very deep recursion when performance or recursion limits are a concern.
- Keep recursive functions simple and focused.

---

## ⚠️ Common Mistakes

### Forgetting the Base Case

Incorrect:

```python
def recurse():

    recurse()
```

Raises:

```text
RecursionError
```

---

### Not Making Progress

Incorrect:

```python
def factorial(n):

    return n * factorial(n)
```

The input never changes, so recursion never reaches the base case.

---

### Using Recursion for Simple Loops

Not every repetitive task requires recursion.

Sometimes a simple `for` or `while` loop is clearer and more efficient.

---

## 📝 Interview Insight

### Question

What are the two essential components of every recursive function?

### Answer

1. **Base Case** – Stops the recursion.
2. **Recursive Case** – Calls the function again with a smaller or simpler problem.

Without a base case, recursion results in infinite calls and eventually raises a `RecursionError`.

---

## 💡 Remember This

```
Recursion

↓

Base Case

+

Recursive Case
```

Think of recursion as:

> **"Solve a smaller version of the same problem until there is nothing left to solve."**

---

## 🎯 Key Takeaways

- Recursion is a function calling itself.
- Every recursive function must have a base case.
- Each recursive call should reduce the problem size.
- Python manages recursive calls using the call stack.
- Recursion is especially useful for trees, graphs, divide-and-conquer algorithms, and AI search problems.
- Choose recursion when it makes the solution clearer, but consider iteration when performance or recursion depth is a concern.

---

## 💻 Code Reference

`code/functions.py`