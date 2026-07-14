# Comments

## 📖 Overview

Comments are non-executable lines in a program that are written to explain the code. They improve readability, make programs easier to understand, and help developers maintain code over time.

Python ignores comments during program execution.

---

## ❓ Why Do We Need Comments?

As programs grow larger, understanding the purpose of every line of code becomes difficult.

Comments help developers:

- Explain complex logic.
- Improve code readability.
- Leave notes for themselves or teammates.
- Temporarily disable code during testing and debugging.

Writing meaningful comments makes code easier to maintain and collaborate on.

---

## 🧠 Types of Comments

### 1. Single-Line Comment

A single-line comment begins with the `#` symbol.

```python
# This variable stores the user's age
age = 20
```

---

### 2. Multi-Line Comment

Python does not have a dedicated multi-line comment syntax. However, triple quotes (`'''` or `"""`) are commonly used to write multi-line explanatory text.

```python
"""
This program calculates
the total marks of a student.
"""
```

> **Note:** Triple-quoted text is technically a string literal. It is often used as a multi-line comment when it is not assigned to a variable.

---

## 🌍 Real-World Applications

Comments are useful for:

- Explaining business logic
- Documenting functions
- Collaborating in teams
- Debugging programs
- Maintaining large codebases

---

## 🤖 AI Connection

AI and Machine Learning projects often contain complex preprocessing steps, mathematical formulas, and model configurations.

Clear comments help developers understand:

- Data preprocessing
- Model architecture
- Training parameters
- Evaluation metrics
- Experiment results

Well-commented AI code is easier to debug, maintain, and improve.

---

## ⚠️ Common Mistakes

### Writing obvious comments

❌

```python
# Store 10 in x
x = 10
```

This comment adds no value.

---

### Better approach

✅

```python
# Store the minimum age required for registration
minimum_age = 18
```

The comment explains the **purpose**, not the syntax.

---

## 💡 Remember This

- Comments are ignored by Python during execution.
- Use comments to explain **why**, not **what**.
- Good comments improve readability and maintainability.
- Avoid unnecessary or outdated comments.

---

## 🎯 Key Takeaways

- Comments make code easier to understand and maintain.
- Use `#` for single-line comments.
- Triple quotes are commonly used for multi-line explanations.
- Write comments that explain the intent of the code rather than describing obvious statements.

---

## 💻 Code Reference

```text
code/09-comments.py
```