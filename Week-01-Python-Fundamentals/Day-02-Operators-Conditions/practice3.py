#Exercise 3 — Logical operators
# A product should pass if:
# - Weight is between 95 and 105 grams.
# - Print quality is acceptable.
# Write the condition using and.

# Test these values:
# Weight	Print quality	Expected
# 100	True	PASS
# 90	True	REJECT
# 100	False	REJECT
# 110	False	REJECT

weight = 100
print_quality = False

if weight >= 95 and weight <= 105 and print_quality:
    print("PASS")
else:
    print("REJECT")
