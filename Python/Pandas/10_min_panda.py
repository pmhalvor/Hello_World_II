import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
This was an article I foudn but never ended up completing...

"""

##############Object creation###########################
s = pd.Series([1,3,7,np.nan,9,13])

#creating a dataframe with numpy array, datetime index and labeled columns
dates = pd.date_range('20190122', periods=7)

df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20190122'),
                    'C' : pd.Series(1, index=list(range(4)), dtype = 'float32'),
                    'D' : np.array([3] * 4),
                    'E' : pd.Categorical(["test", "train", "try", "practice"]),
                    'F' : 'frank'})

# print(df2.dtypes)

#############Viewing Data#######################
# print(df.head()) #shows top five rows of DataFrame
# print(df.tail()) #shows bottom five rows of DataFrame
# print(df.index) #row names
# print(df.columns) #column names
# print(df.values) #array of values
# print(df.describe()) #mean, min, max of df
# print(df.T) #transform
# print(df.sort_index(axis=1, ascending=False) #prints reverse order of columns
# print(df.sort_values(by='B')) #sorts 'B' column largest to smallest


#################Selection######################
# print(df[['A','B']]) #selects only those two columns
# df[['A','B']] = df[['B','A']] #switches the two columns
# print(df[0:3]) #chooses only those 4 rows
