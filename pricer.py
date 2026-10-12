#Exercise 5
#"12" has class string, 12 has class integer, 12.0 has class float, True has class Boolean
#Adding "5" + "3" as strings leads to the result of 53 because the two strings are concatenated
#Adding 5 + 3 as integers leads to the result of 8 because mathematicaladdition is occuring

#Reflection Questions
# 1. The program was unable to run and delivered a TypeError message. It said that there was an unsupported operand type for str and float
#     This occurred because Python is unable to perform mathematical operations on strings
# 2. Python does this because it considers "5" and "3" as strings and cannot perform mathematical operations on strings
#     input() automatically returns strings, so input must be converted to floats or ints before performing math
# 3. I would use these in a very similar way to how they were used in this lab. Since I plan on becoming an accountant and handling/calculating numbers,
#      it is not unlikely that I would have to build tools to track the inflow and outflow of money. I may have to creat a tool that balances accounts and 
#      returns the amount of money that a company owes or is owed.

#Exercise 1
product = "shoes"
unit_price = 25.00
quantity = 12
in_stock = True
print(type(product))
print(type(unit_price))
print(type(quantity))  
print(type(in_stock))

#Exercise 2
print(f"{quantity} units of {product} at ${unit_price} each = ${(unit_price * quantity):.2f}")

#Exercise 3
product = input("Enter the product name: ")
unit_price = (input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))

print(f" {quantity} units of {product} at ${unit_price} each = ${float(unit_price) * int(quantity):.2f}")

#Exercise 4

unit_cost = 15.50
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

print(f"Product: {product}")
print(f"Price: ${unit_price:.2f}")
print(f"Qty: {quantity}")
print(f"Revenue: ${revenue:.2f}")
print(f"Margin: {margin:.2f}%")
