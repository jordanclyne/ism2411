#inventory.py
#Author: Jordan Clyne
#Module 10 Lab: Inventory List Manager

# Reflection
#1. The most surprising thing about how lsits work in Python to me is that 
#lists begin indexing at 0, but end at index -1. The idea that they begin at
#index 0 is difficult for me to remember, since that is not how I am used to counting.

#2. I track the hourly sales during my job to determine what the busiest parts of the
# day are on average. Using a Python list to store each hour's sales would be helpful 
# for me because it would allow me to easily calculate averages, minimums, and maximums 
# instead of inputting each value into Excel separately. 

#Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2: Index Practice

print("---Exercise 2: Index Practice---")
print(inventory[0]) #always grabs the first item
print(inventory[-1]) #always grabs the last item

middle = len(inventory) // 2 #grabs the middle item (not hard coded)
print(inventory[middle])

#Exercise 3: Slicing 
print("---Exercise 3: Slicing---")
print(inventory[0:3]) #grabs first three items
print(inventory[-2:]) #grabs last two items
print(inventory[::2]) #grabs every other item

#Exercise 4: Modify
print("---Exercise 4: Modify---")
inventory.append("envelope") #adds an item to the end of the list
print(inventory)
inventory.remove("tape") #removes an item from the list
print(inventory)
inventory.sort() #sorts the list in alphabetical order
print(inventory)

#Exercise 5: Tuple Comparison
print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060) #NYC coordinates

try: 
    coords[0] = 99 #This will raise a TypeError because tuples are immutable
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

print(coords) #prints the original tuple

#Exercise 6: Average a List of Sales
print("---Exercise 6: Average a List of Sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sale: {average:.2f}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

#Exercise 7: Accumulator Pattern
print("---Exercise 7: Accumulator Pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
   discounted.append(round(price * 0.9, 2)) #apply a 10% discount and round to 2 decimal places

print(prices)
print(discounted)

#Exercise 8: Filter Above Threshold
print("---Exercise 8: Filter Above Threshold---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
threshold = 300
for sale in sales:
    if sale > threshold:
        high_sales.append(sale)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
