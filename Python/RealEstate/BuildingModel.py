import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

melborne_file_path = "C:/Users/perha/Desktop/Programming/Python/RealEstate/melb_data.csv/melb_data.csv"
melborne_data = pd.read_csv(melborne_file_path)


# Set random state number to ensure the same results for each run
# # The more randomness allowed, the less relevant model of your data you have
melborne_model = DecisionTreeRegressor(random_state=1)


# values for arrays til fit model
melborne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] #Dont use cars here
X = melborne_data[melborne_features]
y = melborne_data.Price


# Check statistics of featured columns
print(X.describe())
print(X.head())


# Fit model
melborne_model.fit(X,y)


# Make predictions for data in learning set
print("\n\nPredictions for price of first 5 houses:")
print("\n Actual   ", " Predicted")
print(np.c_[y, melborne_model.predict(X)])
'''
Output:
Predictions for price of first 5 houses:
[[1480000. 1480000.]
 [1035000. 1035000.]
 [1465000. 1465000.]
 [ 850000.  850000.]
 [1600000. 1600000.]]


As we can see, the results for this are 100% correct since we are testing on the
 same data our model learned from. This is why we need another set of data to
 use in the evalutation step.
'''
