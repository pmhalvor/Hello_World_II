import pandas as pd
import numpy as np


# Reading the file
melborne_file_path = "C:/Users/perha/Desktop/Programming/Python/RealEstate/melb_data.csv/melb_data.csv"
melborne_data = pd.read_csv(melborne_file_path)


# Check the columns in file
print(list(melborne_data))


# Find specific attributes
print("Describe landsize\n", melborne_data['Landsize'].describe())
print("\nAverage price", "{:.2f}\n".format( melborne_data['Price'].mean()))


"""
This is just me being stupid, the correct way follows after:

print(melborne_data['Bedroom2'][1])
array_of_rooms = np.array(melborne_data['Bedroom2'])
print(array_of_rooms)

butt = melborne_data.size()

rooms_and_price = np.zeros((2,butt))
rooms_and_price[0] = melborne_data['Price']
rooms_and_price[1] = melborne_data['Bedroom2']

if( rooms_and_price[1][:] > 2):
    my_mean = sum(rooms_and_price[0])/melborne_data['Price'].length()
# for i in melborne_data:
"""


# Dot selection for easier halnding
y = melborne_data.Price
# print(y)
print("\nAverage price", "{:.2f}\n".format(y.mean()))


# Pulling specific features
melborne_features = ['Rooms', 'Bathroom', 'Landsize', 'Car']
X = melborne_data[melborne_features]

# .describe() gives summary of all information
print(X.describe())
# .head() gives the first few values of selected coloumns
print(X.head())
