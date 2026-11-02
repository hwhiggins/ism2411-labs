# Self-Assessment Questions

# 1: In Exercise 5, the first bug I saw was the missing colon after the for
# loop. The traceback pointed directly to the line with the for loop. This 
# tells me that I am starting to understand how to use traceback messages to
# find where the error is. 

# 2. The apply_discount(price, tier) function takes the price of an
# item and the customer's discount tier. It checks the tier and applies the correct
# discount. It returns the price after the discount. Yes, a colleague could use it 
# without reading the body if they knew what the price and tier inputs should be.

# 3. I used AI to help explain what the traceback errors in exercise 5 meant. I copied
# and pasted only the error code in the terminal, not the broken code. I still had to 
# review the code to understand what to fix, so it helped me build my understanding.

# --- Exercise 1 ---

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price    # No discount

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale           # Changed = to += so the accumulator keeps adding each sale
print(f"Total: ${total}")

count = 0
for sale in sales:          # Added a colon after the for loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):       # Changed <= to < so the index doesnt go past the end
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100  # global x

def double_it():
    x = 999  # local x
    return x * 2

print(x)              # global x prints   
print(double_it())    # local x * 2 prints
print(x)              # global x prints again  