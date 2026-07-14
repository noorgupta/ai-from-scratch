# Float (`float`)

## 📖 Overview

A **float** (floating-point number) is a numeric data type used to represent numbers that contain a decimal point. It is commonly used whenever precision beyond whole numbers is required.

---

## ❓ Why Do We Need Floats?

Not all real-world values are whole numbers.

Examples include:

- Product prices
- Temperature
- Height and weight
- Scientific measurements
- Percentage values

Integers cannot accurately represent these values, so Python provides the `float` data type.

---

## 🧠 Characteristics

- Stores decimal numbers.
- Can be positive, negative, or zero.
- Supports arithmetic operations.
- More precise than integers for fractional values.

Examples:

```python
3.14
99.99
-12.5
0.0
```

---

## ⚙️ Internal Working

When Python encounters:

```python
price = 99.99
```

It:

1. Creates a floating-point object.
2. Stores it in memory.
3. Makes the variable `price` refer to that object.

---

## 💻 Examples

```python
price = 99.99
height = 5.8
temperature = -3.5

print(price)
print(type(price))
```

**Output**

```text
99.99
<class 'float'>
```

---

## 🌍 Real-World Applications

Floats are commonly used to represent:

- Product prices
- Student percentages
- Height and weight
- Distance
- Speed
- Temperature
- Financial calculations

---

## 🤖 AI Connection

Floating-point numbers are the backbone of Artificial Intelligence.

They are used for:

- Model weights
- Probabilities
- Learning rate
- Loss values
- Accuracy
- Prediction confidence
- Neural network calculations

Almost every AI model performs millions of floating-point calculations during training.

---

## ⚠️ Common Mistakes

### Assuming every number is an integer

```python
price = 99
```

This is an integer.

Correct:

```python
price = 99.99
```

---

### Forgetting to convert user input

```python
price = input("Enter price: ")
```

Use:

```python
price = float(input("Enter price: "))
```

when decimal values are expected.

---

## 💡 Remember This

- Floats store decimal numbers.
- They are used whenever fractional values are needed.
- AI models rely heavily on floating-point calculations.

---

## 🎯 Key Takeaways

- `float` represents decimal numbers.
- It is essential for scientific and mathematical computations.
- Floats are extensively used in Machine Learning and Deep Learning.
- Decimal values should generally be stored using the `float` data type.

---

## 💻 Code Reference

```text
code/02-float.py
```