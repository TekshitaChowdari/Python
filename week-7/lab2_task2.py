def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    discount_amount = price * discount / 100
    final_price = price + tax - discount_amount
    return final_price


print("Only price:")
print(calculate_price(1000))

print("Price and custom tax rate:")
print(calculate_price(1000, 10))

print("All arguments:")
print(calculate_price(1000, 10, 5))
#output:-
#Only price:
#1180.0
#Price and custom tax rate:
#1100.0
#All arguments:
#1050.0
