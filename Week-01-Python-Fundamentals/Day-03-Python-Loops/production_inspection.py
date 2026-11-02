# Scenario: Your machine needs to inspect 5 products.

# The acceptable weight is 95–105 grams.

# Your program must:
# 1. Ask how many products need inspection.
# 2. Accept each product's weight.
# 3. Check whether the weight is acceptable.
# 4. Count accepted products.
# 5. Count rejected products.
# 6. Calculate rejection percentage.
# 7. Display the final inspection report.


# Scenario: Your machine needs to inspect 5 products.

# The acceptable weight is 95–105 grams.

# Your program must:
# 1. Ask how many products need inspection.
# 2. Accept each product's weight.
# 3. Check whether the weight is acceptable.
# 4. Count accepted products.
# 5. Count rejected products.
# 6. Calculate rejection percentage.
# 7. Display the final inspection report.

accepted_product=0
rejected_product=0

inspection_product = int(input("Enter the inspection products"))
print("Inpspection_product is ", inspection_product)

for inspection in range(1 , inspection_product+1):
    product_weight = float(input("Enter the product weight in grams"))
    if product_weight >= 95 and product_weight <=105:
      accepted_product +=1
    else:
      rejected_product +=1

rejected_percentage = (rejected_product/inspection_product)*100.00

print("Total Inspected Product : ", inspection_product)
print("Total accepted product: ",accepted_product)
print("Total rejected Product:", rejected_product)
print("Rejected Percentage: ", rejected_percentage)

      