import numpy as np
fuel_efficiency = np.array([30, 35, 25, 40, 28, 32])
average_fuel_efficiency = np.mean(fuel_efficiency)
car_model1 = 2  
car_model2 = 4  
percentage_improvement = ((fuel_efficiency[car_model2] - fuel_efficiency[car_model1]) / fuel_efficiency[car_model1]) * 100
print(f"Average fuel efficiency: {average_fuel_efficiency:.2f} mpg")
print(f"Percentage improvement between car model {car_model1} and {car_model2}: {percentage_improvement:.2f}%")
