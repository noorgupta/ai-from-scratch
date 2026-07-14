# String (`str`)

## 📖 Overview

A **string** is a sequence of characters used to represent textual data in Python. It can contain letters, numbers, symbols, spaces, or a combination of these.

Strings are enclosed within either single quotes (`' '`) or double quotes (`" "`).

---

## ❓ Why Do We Need Strings?

Computers don't only work with numbers—they also process text.

Strings allow us to store and manipulate textual information such as:

- Names
- Addresses
- Email IDs
- Passwords
- Messages
- User Input
- URLs

Without strings, handling text in programming would not be possible.

---

## 🧠 Characteristics

- Stores textual data.
- Enclosed in single or double quotes.
- Can contain letters, numbers, symbols, and spaces.
- Supports many built-in operations and methods.

Examples:

```python
"Hello"
'Python'
"Noor Gupta"
"AI From Scratch"
```

---

## ⚙️ Internal Working

When Python encounters:

```python
language = "Python"
```

It:

1. Creates a string object.
2. Stores the sequence of characters in memory.
3. Makes the variable `language` refer to that string object.

Unlike integers, a string is made up of individual characters stored in order.

---

## 💻 Examples

```python
name = "Noor"
course = "Artificial Intelligence"

print(name)
print(type(name))
```

**Output**

```text
Noor
<class 'str'>
```

---

## 🌍 Real-World Applications

Strings are used to store:

- User names
- Email addresses
- Phone numbers (when not performing calculations)
- Passwords
- Search queries
- Chat messages
- File names
- Website URLs

---

## 🤖 AI Connection

Strings are one of the most important data types in Artificial Intelligence.

They are used in:

- Chatbots
- Large Language Models (LLMs)
- Prompt Engineering
- Natural Language Processing (NLP)
- Machine Translation
- Sentiment Analysis
- Speech-to-Text systems

Whenever you type a prompt into ChatGPT, your input is received and processed as a **string**.

---

## ⚠️ Common Mistakes

### Forgetting quotation marks

```python
name = Noor
```

❌ Python looks for a variable named `Noor`.

Correct:

```python
name = "Noor"
```

---

### Assuming numbers inside quotes are integers

```python
age = "20"
```

This is a **string**, not an integer.

To perform mathematical operations, convert it using:

```python
age = int(age)
```

---

## 💡 Remember This

- Strings store textual information.
- Strings must be enclosed in quotes.
- `"25"` and `25` are different data types.
- Every prompt given to an AI chatbot is processed as a string.

---

## 🎯 Key Takeaways

- `str` represents textual data.
- Strings are one of the most frequently used data types in programming.
- They play a fundamental role in AI, especially in NLP and Generative AI.
- Understanding strings is essential before learning string operations and text processing.

---

## 💻 Code Reference

```text
code/03-string.py
```