import numpy as np
house_data = np.array([
    [4, 1500, 200000],
    [5, 2000, 250000],
    [3, 1800, 180000],
    # ... (continue)
])
bedroom_column = 0
sale_price_column = 2
houses_more_than_4_bedrooms = house_data[house_data[:, bedroom_column] > 4]
average_sale_price_more_than_4_bedrooms = np.mean(houses_more_than_4_bedrooms[:, sale_price_column])

print(f"The average sale price of houses with more than four bedrooms is: {average_sale_price_more_than_4_bedrooms}")
