import numpy as np
sales_data = np.array([10, 1000, 100, 1800])
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print(f"Total sales for the year: {total_sales}")
print(f"Percentage increase in sales from Q1 to Q4: {percentage_increase:.2f}%")
