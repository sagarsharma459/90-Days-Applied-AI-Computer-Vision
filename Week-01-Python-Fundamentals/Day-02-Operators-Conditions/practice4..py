# Exercise 4 — Conditional statements
# Write a program to classify the weight:
# - Below 95 → UNDERWEIGHT
# - 95 to 105 → PASS
# - Above 105 → OVERWEIGHT
# Try these values: 90, 95, 100, 105, 110.

weight = 106
if weight < 95:
  print("UNDERWEIGHT")
elif weight >= 95 and weight <= 105:
  print("PASS")
else:
  print("OVERWEIGHT")
