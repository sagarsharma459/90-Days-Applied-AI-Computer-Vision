
## Python Basics - Practice
total_products = 1000
rejected_products = 25
accepted_products = total_products - rejected_products
print("Total Products:", total_products)
print("Rejected Products:", rejected_products)
print("Accepted Products:", accepted_products)


#### Understanding the variables and data types in Python

product_name = "Widget"
product_price = 19.99
total_products = 1000
rejection_percentage = 2.5
inspection_completed = True

print(type(product_name))  # Output: <class 'str'>
print(type(product_price))  # Output: <class 'float'>
print(type(total_products))  # Output: <class 'int'>
print(type(rejection_percentage))  # Output: <class 'float'>
print(type(inspection_completed))  # Output: <class 'bool'>

print("\n #### My First Coding challenge ####")

print("Welcome to the Product Inspection System!")  
#print("Please enter the total number of products inspected:")
total_products = int(input("Enter total products: "))  # Taking input from the user and converting it to an integer

print("Please enter the number of rejected products:")
rejected_products = int(input())  # Taking input from the user and converting it to an integer

accepted_products = total_products - rejected_products
print("Total Products:", total_products)
print("Accepted Products:", accepted_products)
print("Rejected Products:", rejected_products)

rejection_percentage = (rejected_products / total_products) * 100
print("Rejection Percentage: {:.2f}%".format(rejection_percentage))  # Formatting the output to 2 decimal places

