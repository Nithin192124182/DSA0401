import pandas as pd
data=pd.read_csv("‪C:\Users\KANTA\Downloads\Sale Report.csv")

# Assuming property_data is your DataFrame
# You can load your data using something like: property_data = pd.read_csv('property_data.csv')

# 1. The average listing price of properties in each location.
average_price_per_location = property_data.groupby('location')['listing_price'].mean()

# 2. The number of properties with more than four bedrooms.
properties_with_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_with_more_than_four_bedrooms)

# 3. The property with the largest area.
property_with_largest_area = property_data[property_data['area_sqft'] == property_data['area_sqft'].max()]

print("Average listing price of properties in each location:")
print(average_price_per_location)

print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)

print("\nProperty with the largest area:")
print(property_with_largest_area)
