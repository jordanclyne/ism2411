#Self-Assessment Questions
#1. If you forgot to divide the percentage by 100, Python would produce a wrong answer silently.
#   None of the coding itself is incorrect, but the logic is wrong. Python would run but the answer would be very incorrect.
#2. The modulo operator would also be useful when determining where a value falls in a cycle.
#   In the context of business, this would be helpful for determining what days employees who are on a specific work/rest cycle work on.
#3. I feel least confident about :,.2f, :.1%, etc. I understand what these do, but I don't understand how they work and how to know when to use them.
#   I would feel more confident about this concept by specifically studying what these are and what they mean in code.

#Revenue, Margins, and Discount Calculator

#Exercise 1: 
price = 50
quantity = 12
revenue = price * quantity
#,.2f has two jobs -> thousands separator and EXACTLY 2 decimal places
print(f"Revenue: ${revenue:,.2f}")

#Exercise 2:
cost = 32
price = 50
margin = (price - cost) / price #margin stays as a decimal
print(f"Margin: {margin:.1%}")

#Exercise 3:
#Product A wins if margin_a > margin_b
#Product A margin 60%, Product B margin (80-60)/80 = 25%
margin_a = 0.6
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

#Exercise 4: Logic Combo

price = 150
margin = 0.35
is_premium = price > 100 and margin > 0.3 #Remember to review basic logic operators: and, or, not

#Exercise 5: Division + Mod

print(17/3) #5.666666666666667
print(17//3) #5
print(17%3) #2

#Exercise 6:
name = input("Product name: ")
retail_price = float(input("Enter retail price: "))
cost = float(input("Enter cost: "))
quantity_sold = int(input("Enter quantity sold: "))
discount_pct = int(input("Enter discount percentage: "))
print("=" * 50)
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1 - discount_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)

print(f"Product name: {name}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")

#Exercise 7: 
print("=" * 50)
BOX_SIZE = 24 # ALL UPPER CASE MEANS CONSTANT/SHOULD NEVER BE CHANGED
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE #Floor division is not abstract math
loose_items = items_ordered % BOX_SIZE #Modulo is not abstract math
exact_fit = loose_items == 0 # == is the equivalancy operator, = is the assignment operator
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

