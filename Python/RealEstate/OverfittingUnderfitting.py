from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    """
    Function to quickly estimate Mass Average Error based on number of leaves.

    Argument:

        max_leaf_nodes:
            Limit to number of leaves on tree

        train_X:
            training set of X

        val_X:
            valuation data for X

        train_y:
            training set for y

        val_y:
            evalutation data for x

    """

    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

def load_data(filename):
    """
    Function that loads your data from a file and gives you the array of
    coloumns.

    Arguments:
        filename:
            string of file location

    """

    # Import file, create dataframe, define model, fit model:
    melborne_file_path = filename
    df = pd.read_csv(filename)

    # Filter rows with missing price values
    filtered_df = df.dropna(axis=0)

    print(list(filtered_df))
    return filtered_df


df = load_data("C:/Users/perha/Desktop/Programming/Python/RealEstate/melb_data.csv/melb_data.csv")

# specific features for the house
melborne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] #Dont use cars here
X = df[melborne_features]
y = df.Price


# Splitting data into training and testing sets with help from sklearn tools
from sklearn.model_selection import train_test_split
# train_test_split return 4 arrays, a train and test for each X and y
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


import matplotlib.pyplot as plt

max_list = [5,25, 50,137,250,275, 300, 325, 350, 375, 400, 425, 450, 475, 490, 500, 510, 525, 550, 575, 600, 650, 700, 1000,1500]
max_list = range(5, 1000, 5)
mae_list = []
best_mae = get_mae(2, train_X,val_X,train_y,val_y)
best_nodes=2
for max_leaf_nodes in max_list:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    # print("Max leaf nodes: %d \t\t Mean Absolute Error: %d"%(max_leaf_nodes, my_mae))
    mae_list.append(my_mae)
    if (my_mae<best_mae):
        best_mae=my_mae
        best_nodes=max_leaf_nodes


"""
# For a plot of the best values
plt.plot(max_list, mae_list)
plt.xlabel("Max Nodes per Decision Tree")
plt.ylabel("Mass Absolute Error")
plt.title("Underfitting and Overfitting Max Nodes ")
plt.show()
"""



# Build your final model off of the best max nodes and all of your data
final_model = DecisionTreeRegressor(max_leaf_nodes=best_nodes,random_state=0)
final_model.fit(X,y)
