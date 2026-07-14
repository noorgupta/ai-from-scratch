# Loop Control Statements (`break`, `continue`, `pass`)

## 📖 Overview

Loop control statements allow us to modify the normal execution of a loop. They can stop a loop, skip specific iterations, or act as placeholders for future code.

Python provides three loop control statements:

- `break`
- `continue`
- `pass`

---

## ❓ Why Do We Need Loop Control Statements?

Sometimes, executing every iteration of a loop is unnecessary.

For example:

- Stop searching once the required item is found.
- Skip invalid data while processing a dataset.
- Leave a block empty temporarily while developing a program.

Loop control statements make programs more efficient and flexible.

---

# `break`

## 🧠 What is `break`?

The `break` statement immediately terminates the loop and transfers control to the first statement after the loop.

### Example

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

**Output**

```text
1
2
3
```

---

# `continue`

## 🧠 What is `continue`?

The `continue` statement skips the current iteration and moves directly to the next iteration of the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output**

```text
1
2
4
5
```

---

# `pass`

## 🧠 What is `pass`?

The `pass` statement does nothing.

It acts as a placeholder when Python expects a statement but no implementation has been written yet.

### Example

```python
for i in range(5):
    if i == 3:
        pass
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

The `pass` statement has no effect on the execution of the loop.

---

## 🌍 Real-World Applications

### `break`

- Stop searching after finding a record.
- Exit a menu-driven program.
- Stop processing when an error occurs.

### `continue`

- Skip invalid user input.
- Ignore missing values in a dataset.
- Skip corrupted records while reading files.

### `pass`

- Create the basic structure of a program before writing the implementation.
- Define empty functions or classes during development.

---

## 🤖 AI Connection

Loop control statements are commonly used in AI workflows.

Examples include:

- **`break`**: Stop training early when the desired accuracy is achieved.
- **`continue`**: Skip incomplete or corrupted data samples.
- **`pass`**: Build the initial structure of AI pipelines before implementing all components.

---

## ⚠️ Common Mistakes

### Confusing `break` and `continue`

- `break` → Stops the entire loop.
- `continue` → Skips only the current iteration.

---

### Expecting `pass` to skip an iteration

`pass` does **not** skip anything.

It simply tells Python to "do nothing."

---

## 💡 Remember This

- `break` → Exit the loop.
- `continue` → Skip the current iteration.
- `pass` → Do nothing (placeholder).

---

## 🎯 Key Takeaways

- Loop control statements modify how loops execute.
- `break` terminates a loop.
- `continue` skips the current iteration.
- `pass` is a placeholder and performs no action.

---

## 💻 Code Reference

`code/04-loop-control-statements.py`