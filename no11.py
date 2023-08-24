import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Sample data for months and corresponding sales
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1800, 1300, 1600, 2000]

# Line Plot
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(months, sales, marker='o')
plt.title('Monthly Sales Prediction (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Scatter Plot
plt.subplot(132)
plt.scatter(months, sales, color='blue', marker='o')
plt.title('Monthly Sales Prediction (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# Bar Plot
plt.subplot(133)
plt.bar(months, sales, color='green')
plt.title('Monthly Sales Data (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

plt.tight_layout()
plt.show()
