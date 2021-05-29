
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.datasets import load_iris
import graphviz
iris = load_iris()
data_set = pd.read_csv('E:\minor 2 data set\Tou.csv')
    # cleaning data removin null values
data_set.pop('A')
data_set.pop('B')
data_set.pop('C')
data_set.pop('D')
data_set.pop('E')
data_set.pop('F')
data_set.pop('G')
print(data_set)
print("\n")
print("\n")
print("After data cleaning :")
print("\n")
X = data_set.iloc[:, : -1]
print(X)

y= data_set.iloc[:, 4]
#print(y)
labelencoder = LabelEncoder()
X = X.apply(LabelEncoder().fit_transform)
print(X)
print("\n")
regressor = DecisionTreeClassifier()
regressor.fit(X.iloc[:, 1:4], y)
Crops ={'Paddy': 7, 'Maize': 5, 'Jowar': 4, 'Tur': 11, 'Cotton': 1, 'Groundnut': 3, 'Soyabean': 9, 'Wheat': 12, 'Barley': 0, 'Gram': 2, 'Mustard': 6, 'Sugarcane':10, 'Safflower': 8}
Season = {'Kharif':0,'Rabi':1}
States = {'Uttar Pradesh': 4, 'Maharashtra': 2, 'Andhra Pradesh': 0,'Uttrakhand' : 5, 'Punjab': 3,'Gujarat':1}
X_input_values = np.array([Crops['Cotton'], Season['Kharif'], States['Maharashtra']])
Y_prediction = regressor.predict([X_input_values])
print(" Crop : Cotton , Season : Kharif, State : Maharastra")
print("\t")
print("Yeild decision  : "+Y_prediction)




