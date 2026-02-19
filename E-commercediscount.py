# E-commerce Discount Engine

cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Discount based on cart value
if cart_value > 50000:
    discount = 15
elif cart_value > 20000:
    discount = 10
else:
    discount = 5

# Discount based on membership
if membership == "silver":
    discount = max(discount, 10)
elif membership == "gold":
    discount = max(discount, 20)
elif membership == "platinum":
    discount = max(discount, 25)

# Discount for festival season
if festival == "yes":
    discount = max(discount, 30)

# Final calculation
final_amount = cart_value - (cart_value * discount / 100)

print("Highest Discount Applied: - E-commercediscount.py:32", discount, "%")
print("Final Payable Amount: ₹ - E-commercediscount.py:33", final_amount)