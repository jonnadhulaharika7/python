#prices of items
item_price1 = 1000 #shoes
item_price2 = 500  #shirts
quantity1 = 2
quantity2 =1

#calculation
total_item1 = item_price1 * quantity1
total_item2 = item_price2 * quantity2

total_bill = total_item1 + total_item2

discount = total_bill * 5 / 100 # 5% discount
final_amount = total_bill - discount

#display results
print("Total bill:",    total_bill)
print("Discount:",      discount)
print("Final amount:",  final_amount)
