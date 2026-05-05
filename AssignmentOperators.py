cart_total = 0

#Adding items to cart
item1_price = 2000
item2_price = 3000

cart_total += item1_price
cart_total += item2_price
print("Cart total after adding items:", cart_total)

#Applying discount (15%)
discount = 0.15
cart_total -= cart_total * discount
print("After discount:", cart_total)

#Adding delivery charge
delivery_charge = 40
cart_total += delivery_charge
print("After adding delivery charge:", cart_total)

#Applying GST (10%)
cart_total *= 1.10
print("After GST:", cart_total)

#Using wallet balance
wallet = 400
cart_total -= wallet
print("After using wallet:", cart_total)

#Splitting bill among 2 friends
split_amount = cart_total // 2
print("Each person pays:", split_amount)

#Remaining amount (if any)
remaining = cart_total % 2
print("Remaining amount:", remaining)