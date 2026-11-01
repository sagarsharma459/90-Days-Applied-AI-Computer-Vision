# Main Day 2 project — Industrial Quality Decision System

# Imagine your inspection machine checks three quality parameters:
# 1. Weight.
# 2. Printing quality.
# 3. OCR confidence.
# Your rules:
# Parameter	Acceptance condition
# Weight	95–105 grams
# Printing	Must be correct
# OCR confidence	At least 90%

# The product passes only when all three conditions are satisfied.


print("===== INDUSTRIAL QUALITY INSPECTION =====")

weight = float(input("Enter product weight (grams): "))
weight = max(0.0,min(weight, 200.0))

print_quality = input(
    "Is printing correct? (yes/no): "
).lower()

if print_quality not in ["yes", "no"]:
    print("Invalid input for printing quality. Please enter 'yes' or 'no'.")
    print("Exiting the program.")
    exit()

ocr_confidence = float(
    input("Enter OCR confidence (%): ")
)

ocr_confidence = max(0.0, min(ocr_confidence, 100.0))

# Write your conditions below
if print_quality == "yes":
      if ocr_confidence >= 90.00:
          if weight >= 95.00 and weight <= 105.00:
              print("PASS")
          else:
              print("REJECT")
      else:
            print("REJECT")
else:
        print("REJECT")