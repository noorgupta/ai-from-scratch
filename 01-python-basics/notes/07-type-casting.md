# Type Casting

## 📖 Overview

Type casting is the process of converting a value from one data type to another. It helps ensure that data is in the correct format before performing operations on it.

Python supports two types of type casting:

- Implicit Type Casting (Automatic)
- Explicit Type Casting (Manual)

---

## ❓ Why Do We Need Type Casting?

Different operations require different data types.

For example:

- Mathematical calculations require numbers.
- Text processing requires strings.
- User input is always received as a string.

Type casting allows Python programs to work with data correctly.

---

## 🧠 Types of Type Casting

### 1. Implicit Type Casting

Python automatically converts one data type into another when it can do so safely without losing information.

Example:

```python
num = 10
price = 5.5

result = num + price

print(result)
print(type(result))
```

**Output**

```text
15.5
<class 'float'>
```

Python automatically converts the integer `10` into `10.0` before performing the addition.

---

### 2. Explicit Type Casting

In explicit type casting, the programmer manually converts one data type into another using built-in functions.

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

---

## 💻 Common Type Casting Functions

### `int()`

Converts a compatible value into an integer.

```python
int(5.9)      # 5
int("25")     # 25
```

---

### `float()`

Converts a value into a floating-point number.

```python
float(10)      # 10.0
float("9.5")   # 9.5
```

---

### `str()`

Converts a value into a string.

```python
str(25)       # "25"
str(True)     # "True"
```

---

### `bool()`

Converts a value into a Boolean.

Examples:

```python
bool(1)        # True
bool(0)        # False
bool("")       # False
bool("Python") # True
```

---

## 🌍 Real-World Applications

Type casting is commonly used for:

- Processing user input
- Reading data from files
- API responses
- Mathematical calculations
- Data cleaning

---

## 🤖 AI Connection

In AI and Machine Learning, data often comes from CSV files, APIs, databases, and user input.

Before training a model, developers frequently convert data into the correct type.

Examples:

- `"25"` → `25`
- `"98.5"` → `98.5`
- `"True"` → Boolean (after appropriate processing)

Correct data types are essential for accurate model training.

---

## ⚠️ Common Mistakes

### Forgetting to convert user input

```python
age = input("Enter age: ")

print(age + 5)
```

This causes an error because `age` is a string.

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

---

### Invalid Conversion

```python
int("Hello")
```

This raises:

```text
ValueError
```

because `"Hello"` cannot be converted into an integer.

---

## 💡 Remember This

- Type casting converts one data type into another.
- Python performs implicit casting automatically when safe.
- Explicit casting is done using built-in functions.
- `input()` usually requires explicit type casting before numerical calculations.

---

## 🎯 Key Takeaways

- Type casting improves compatibility between different data types.
- Python supports both implicit and explicit type conversion.
- The most commonly used functions are `int()`, `float()`, `str()`, and `bool()`.
- Proper type conversion is essential for building reliable AI and software applications.

---

## 💻 Code Reference

```text
code/07-type-casting.py
```