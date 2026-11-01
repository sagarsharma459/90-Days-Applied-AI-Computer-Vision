# Day 2 - Python Operators and Conditions

## Topics Learned
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- If, elif and else
- Nested conditions
- Python indentation

## Practical Exercises
1. Production calculation
2. Temperature validation
3. Weight validation
4. Product classification

## Main Project
Industrial Quality Decision System

## Inspection Parameters
- Weight: 95 to 105 grams
- Printing quality: Correct
- OCR confidence: Minimum 90%

## Key Learning
Used Python conditional logic to make
automated industrial inspection decisions.

## Test Results
Record all six test cases and their results.

## Revision
- D+1: Revise operators and conditions.
- D+7: Rebuild the inspection program.
- D+21: Implement the same logic without notes.

## Questions

# Day 2 – Python Interview Questions and Answers

## 1. What is the difference between `/` and `//`?

**Answer:** `/` performs normal division and returns a floating-point result, whereas `//` performs floor division and rounds the result down to the nearest integer.

```python
a = 10
b = 3

print(a / b)
print(a // b)
```

**Output:**
```text
3.3333333333333335
3
```

## 2. What does `%` return?

**Answer:** The `%` operator returns the remainder after dividing one number by another. It is also called the modulus operator.

```python
a = 10
b = 3

print(a % b)
```

**Output:**
```text
1
```

**Industrial example:** Checking whether products can be evenly distributed across multiple production tracks.

## 3. What is the difference between `=` and `==`?

**Answer:** `=` is an assignment operator used to assign a value to a variable. `==` is a comparison operator used to check whether two values are equal.

```python
weight = 100

print(weight == 100)
print(weight == 95)
```

**Output:**
```text
True
False
```

## 4. What is the difference between `and` and `or`?

**Answer:** `and` returns True only when both conditions are true. `or` returns True when at least one condition is true.

```python
weight = 100
print_quality = True

print(weight >= 95 and print_quality)
print(weight >= 110 or print_quality)
```

**Output:**
```text
True
True
```

**Industrial example:**
- `and`: Product must have correct weight AND correct printing.
- `or`: Product should be rejected if weight is incorrect OR printing is incorrect.

## 5. What happens when an `if` condition is false?

**Answer:** When an `if` condition is false, Python skips its code block and checks the next `elif` or `else` block, if available.

```python
weight = 90

if weight >= 95:
    print("PASS")
else:
    print("REJECT")
```

**Output:**
```text
REJECT
```

## 6. What is the purpose of `elif`?

**Answer:** `elif` means "else if". It allows us to check multiple conditions sequentially when the previous condition is false.

```python
weight = 110

if weight < 95:
    print("UNDERWEIGHT")
elif weight > 105:
    print("OVERWEIGHT")
else:
    print("PASS")
```

**Output:**
```text
OVERWEIGHT
```

## 7. What is nested `if`?

**Answer:** Nested `if` means placing one `if` statement inside another `if` statement. It is useful when a decision depends on another condition being satisfied first.

```python
print_quality = True
weight = 100

if print_quality:
    if weight >= 95 and weight <= 105:
        print("PRODUCT PASS")
    else:
        print("WEIGHT REJECT")
else:
    print("PRINTING REJECT")
```

**Output:**
```text
PRODUCT PASS
```

## 8. Why does Python require indentation?

**Answer:** Python uses indentation to define code blocks and identify which statements belong to conditions, loops, functions and classes. It also improves code readability.

```python
weight = 100

if weight >= 95:
    print("Product PASS")
    print("Weight accepted")

print("Inspection completed")
```

**Output:**
```text
Product PASS
Weight accepted
Inspection completed
```

Incorrect indentation can cause an `IndentationError`.

---

## Quick Revision Table

| Question | Short Answer |
|---|---|
| `/` vs `//` | Normal division vs floor division |
| `%` | Returns remainder |
| `=` vs `==` | Assignment vs comparison |
| `and` vs `or` | Both conditions vs at least one condition |
| False `if` | Skips its block |
| `elif` | Checks another condition |
| Nested `if` | An if statement inside another if |
| Indentation | Defines code blocks |

## Industrial Application – Product Quality Decision

**Interview question:** How would you implement a basic product quality decision using Python?

**Answer:** I would use conditional statements and logical operators to validate product weight and printing quality. If both conditions are satisfied, the product passes; otherwise, it is rejected.

```python
weight = 100
print_quality = True

if weight >= 95 and weight <= 105 and print_quality:
    print("PRODUCT PASS")
else:
    print("PRODUCT REJECT")
```

**Output:**
```text
PRODUCT PASS
```

## Key Learning

- Learned Python arithmetic, comparison, logical and assignment operators.
- Understood conditional statements and nested conditions.
- Applied decision-making logic to industrial quality inspection.
- Practised explaining Python concepts using real industrial examples.

## Revision Schedule

- **D+1:** Revise operators and conditional statements.
- **D+7:** Rebuild the quality inspection program without notes.
- **D+21:** Implement the same decision system independently.

## Self-Assessment

- [ ] I can explain all eight interview questions.
- [ ] I can use arithmetic and comparison operators.
- [ ] I can write `if`, `elif` and `else` independently.
- [ ] I understand nested conditions and indentation.
- [ ] I can implement industrial product quality decision logic.