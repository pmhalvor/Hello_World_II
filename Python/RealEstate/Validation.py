import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor


# Import file, create dataframe, define model, fit model:
melborne_file_path = "C:/Users/perha/Desktop/Programming/Python/RealEstate/melb_data.csv/melb_data.csv"
melborne_data = pd.read_csv(melborne_file_path)

# Filter rows with missing price values
filtered_melbourne_data = melborne_data.dropna(axis=0)

melborne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] #Dont use cars here
X = melborne_data[melborne_features]
y = melborne_data.Price


# Splitting data into training and testing sets with help from sklearn tools
from sklearn.model_selection import train_test_split
# train_test_split return 4 arrays, a train and test for each X and y
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


# Redefine and refit model with new train data
melborne_model = DecisionTreeRegressor(random_state=1)
melborne_model.fit(train_X, train_y)


# Find mean absolute error (MAE) of trainning data:
from sklearn.metrics import  mean_absolute_error
# Using import
predicted_homes_prices = melborne_model.predict(train_X)
# print(np.c_[train_y, melborne_model.predict(train_X)])
print("\nMEA training values:",round(mean_absolute_error(train_y, predicted_homes_prices), 2))
# My way
length_of_df = train_y.count()
my_calc_error = sum(abs(train_y - predicted_homes_prices))/(length_of_df +1)
print("\nMEA training values:",round(my_calc_error, 2), "(my method)")


# Find MEA of valuation data:
predicted_homes_prices = melborne_model.predict(val_X)
print("\nMEA testing values: ",round(mean_absolute_error(val_y, predicted_homes_prices), 2))

"""
Output:

MEA training values: 957.26

MEA training values: 957.16 (my method)

MEA testing values:  241632.17


As expected our training values are a lot closer than the testing values.
I'd still expect a 1-1 correclation in the traning though. What causes the large
differences? Are there just some houses that are so extremely different, or rare
cases, that even when the model uses that data, there's no correlation with the
rest?



"""
