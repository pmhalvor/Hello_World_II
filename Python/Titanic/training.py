import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Training (891 Entries) & (417 Entries) data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
all_data = [train_data, test_data]

#feature 1: Pclass
# print(train_data[["Pclass", "Survived"]])

#feature 2: Gender
# print(train_data[["Sex", "Survived"]].groupby(["Sex"]).mean())

#feature 3: family size
for data in all_data:
    data['family_size'] = data['SibSp'] + data['Parch'] + 1
# print(train_data[["family_size", "Survived"]].groupby("family_size").mean())

#feature 3.1: single riders?
for data in all_data:
    data['is_alone'] = 0 #for each passenger creates new T/F column 'is_alone'
    data.loc[data['family_size'] == 1, 'is_alone'] = 1
print(train_data[['is_alone', 'Survived']].groupby(['is_alone']).mean())

#feature 4: Embarked
for data in all_data:
    data['Embarked'] = data['Embarked'].fillna('S')
print(train_data[['Embarked', 'Survived']].groupby(['Embarked']).mean())

#feature 5: Fare
for data in all_data:
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())
train_data['category_fare'] = pd.qcut(train_data['Fare'], 4)
print(train_data[['category_fare', 'Survived']].groupby(['category_fare']).mean())

#feature 6: Age
for data in all_data:
    age_avg = data['Age'].mean()
    age_std = data['Age'].std()
    age_null = data['Age'].isnull().sum()

    random_list = np.random.randint(age_avg - age_std, age_avg + age_std, size = age_null)
    data['Age'][np.isnan(data['Age'])] = random_list
    data['Age'] = data['Age'].astype(int)

train_data['category_age'] = pd.cut(train_data['Age'], 5)
print(train_data[['category_age', 'Survived']].groupby(['category_age'], as_index = False).mean())
