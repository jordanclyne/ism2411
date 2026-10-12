#1. The first bug I found was the = that was written instead of +=.
#I noticed this while looking through the code since it did not logically make sense.
#This tells me that by debugging insticts are to try to figure bugs out mentally 

#2. apply_discount(price, tier) applies a discount to a price dependent on the predetermined discount tier
# Its inputs are price and tier and it returns the final price after discount
#A colleague could probably use it without reading the body

#3. AI Use Disclosure: I used ChatGPT to help me locate bugs in the broken_sales.py file.
#The AI use did not build my understanding because I was capable of finding all of the bugs on my own.
#Using AI made the process take longer and took away my ability to find and understand the errors myself.






#Exercise 1:
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#Exercise 2:
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Exercise 3:
def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4:
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

#Exercise 6:

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

#Exercise 5:
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale 
    #Error: total is set equal to each sale so that the final value of total is equal to the last sale
    #Fix: change the assignment operator to an addition assignment operator
print(f"Total: ${total}")

count = 0
for sale in sales: 
    #SyntaxError: missing colon at the end of the for loop
    #Fix: add a colon at the end of the for loop since it is a required part of for loop syntax
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #Fix: replace <= with < to stop the index out of range error
    #Error: The way the code is currently written will lead the final value of i to be 5, which is not an index that exists in the list.
    print(sales[i])
    i += 1
