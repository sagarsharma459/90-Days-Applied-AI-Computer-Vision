# Exercise 3 — Use break and continue
# Write a for loop from 1 to 10.

# Requirements:
# - Skip product number 5.
# - Stop the loop when product number 9 is reached.
# - Print all other product numbers.

for product in range(1,11):
   if product == 5 :
     continue
   elif product == 9:
     break
   else:
     print("Product:",product)
  