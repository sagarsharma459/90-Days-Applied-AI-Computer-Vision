# Exercise 2 — Calculate production quantity
# Use a while loop to calculate the total production count from 1 to 10.

counter = 1
total_production = 0

while counter <= 10:
    total_production += counter
    counter += 1

print("Total production :", total_production)