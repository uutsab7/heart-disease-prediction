import pandas as pd
import joblib
from sklearn import *
import numpy as np
#reading the csv file
df = pd.read_csv('heartdata.csv')
df.info()
df.describe()

#
def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size] #all rows & testsetsizecolumn
    train_indices = shuffled[test_set_size:] #first
    return data.iloc[train_indices], data.iloc[test_indices]

#training 80% of our data and testing 20%
train, test = data_split(df, 0.2)
print(train)
print(test)

#converting to 2d array
X_train = train[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']].to_numpy()
X_test = test[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']].to_numpy()
print('2D array is -')
print(X_train)

Y_train = train[['target']].to_numpy().reshape(243,)
Y_test = test[['target']].to_numpy().reshape(60,)
print('1d array is-')
print(Y_train)



# from sklearn.linear_model import LogisticRegression

from sklearn.linear_model import LogisticRegression
clf= LogisticRegression(max_iter=10000)  
clf.fit(X_train, Y_train)
inputFeatures = [21,1,1,125,196,0,1,120,0,0,0,0,1]
infProb = clf.predict_proba([inputFeatures])[0][1]
print(infProb)
print('Accuray is' ,clf.score(X_test,Y_test)*100, "%")

#pickeling the above model
filename = 'model.sav'
joblib.dump(clf,filename)
