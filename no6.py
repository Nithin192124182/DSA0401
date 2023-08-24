def calculate_total_cost(item_prices, quantities, discount_rate, tax_rate):
    total_subtotal = sum(price * quantity for price, quantity in zip(item_prices, quantities))
    discount_amount = total_subtotal * (discount_rate / 100)
    taxable_amount = total_subtotal - discount_amount
    tax_amount = taxable_amount * (tax_rate / 100)
    total_cost = taxable_amount + tax_amount
    return total_cost

item_prices = [10.99, 5.49, 2.99,45.44,34.55,3.45,6.5]
quantities = [3, 2, 4, 4, 7, 10, 11]
discount_rate = 10.0
tax_rate = 7.0

total_cost = calculate_total_cost(item_prices, quantities, discount_rate, tax_rate)
print("Total cost including discounts and taxes: $", total_cost)
