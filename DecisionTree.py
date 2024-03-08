import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
x,y = load_breast_cancer(return_X_y=True)
x_train,x_test,y_train,y_test = train_test_split(x,y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x_train, y_train)

print("accuracy : ",dtree.score(x_test,y_test))
