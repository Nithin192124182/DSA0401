import numpy as np
sales_data = np.array([
    [100, 150, 120],
    [80, 95, 110],
    [120, 130, 140]
])
average_prices_per_product = np.mean(sales_data, axis=1)
average_price_overall = np.mean(average_prices_per_product)

print(f"The average price of all products sold in the past month is: {average_price_overall}")
