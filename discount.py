#1. As 350 passes through the discount tiers, it would first be checked against the first condition
#and because it is not greater than/equal to 500, it would be False and move to the next tier/the first elif.
#It would be checked against that condition, and because 350 is greater than 200, this condition would be met.
#This means that the rest of the discount tiers would not be considered because a True value has been found.
#Discount will be equal to 0.10.
#2. The single statement uses an and operator, which means that both have to be true for the entire statement to be true.
#If two separate statements were used and nested, it would produce the same result because the statements are organized so that 
#the first has to be true for the second to be checked. However, if the statements were not nested, the same result would not be
#produced because one is not dependent on the other and both don't have to be true.
#3. When determining whether or not I earn free shipping on my online orders, I encounter tiered conditional logic.
#Knowing Python helps me understand the computer's logic when determining if I earn free shipping based on whether or not
#my order reaches a certain price.



#Exercise 1: Discount tiers

total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:   #Default value--if all other conditions fail
    discount = 0

#Exercise 3: Combine Conditions
region = "South"
extra_discount = 0 #could also be an else statement
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")


final = total * (1 - (discount + extra_discount))
print(f"Discount: {(discount)*100:.0f}%")
print(f"Final discount: {(discount + extra_discount)*100:.0f}%")
print(f"Final price: ${final:.2f}")

#Exercise 2: Approval Flag

if final > 1000: #strictly greater than
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(status)

#Exercise 4: Refactor a Nested If

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03
#The flat version is easier to read because it resembles natural language

#Exercise 5: Anomaly Flagging
amount = 0

if amount <=0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

#Exercise 6: Boolean Logic

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False #bool

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 10 and not has_outstanding_balance:
    vip_upgrade = True
else:
    vip_upgrade = False

