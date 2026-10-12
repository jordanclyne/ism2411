#1. The accumulator pattern includes three steps, which are initialize, loop, and update. 
#The first step is where a variable is initialized outside of the loop. 
# Inside the loop, the second step loops over each piece of data. 
# Finally, the variable is updated with each iteration. This is especially helpful for 
# functions such as summing or finding maximums. To find sums, the initialized variable will 
# accumulate the total of each piece of data with each loop. To filter or find maximums, each 
# loop will check the piece of data against a current condition and update the variable when 
# the condition is true.

#2. The code length of the while loop was one line longer than the for loop. 
# The for loop is useful because it runs automatically, but requires a known list.
# The while loop requires manual index and increment, but can run with unknown stopping conditions.
# The for loop has less risk, while an error with a while loop can lead to an infinite loop.

#3. I work in retail, and I enjoy tracking my sales each day to determine if we are busier one week 
# to the previous week. A loop would allow me to find the maximum and minimum sales over the
# year to determine when the slowest time of the year is for my job.
# The list would contain each day's sales. I would accumulate the maximum/minimum value. This means that for 
# each loop, the accumulator variable would be replaced with the highest or lowest value in the dataset.
# At the end, I would print the accumulator variable to display what the maximum and minimum are.



#Exercise 1: Sum a List and Exercise 2: Average
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0 
count = 0      # initialize
for sale in sales:
    total += sale   # update
    count = count + 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average}")

#Exercise 3: Max
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

#Exercise 4: Filtered Count
large_sales = 0
large_sales_total = 0
for sale in sales:
    if sale > 100:
        large_sales += 1
        large_sales_total += sale
print(f"Sales over $100: {large_sales}")
print(f"Total of those sales: ${large_sales_total}")

#Exercise 5: Break and Continue
for sale in sales:
    if sale > 100 and sale <=400:
        print(f"${sale}")
    elif sale < 100:
        continue
    else:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break

#Exercise 6: While Loop
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0            # index
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total (while loop): ${total}")
#The two versions are the same length, but I would use the while loop for production
#because the while loop is designed to run with unknown stopping conditions.

#Exercise 7: Discount Applied to All Items

discount = 0
for sale in sales:
    if sale >= 200:
        discount = 0.1
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(f"${sale} --> {discount*100:.0f}% discount -->")
    print(f"${discounted_price:.2f}")
