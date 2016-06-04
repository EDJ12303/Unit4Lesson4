# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 22:23:12 2016

@author: Erin
"""
import numpy as np
from sklearn import datasets
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


#read csv that I downloaded from Thinkful mirror
df = pd.read_csv('C:/Users/Erin/thinkful/Unit4Lesson4/iris_data.csv', index_col=0)
iris = datasets.load_iris()
X = iris.data[:,:2] #first two features
Y = iris.target

#scatterplot of sepal length vs. width by species
plt.scatter(X[:,0], X[:,1], c=Y)

#generate random point using elements in enumerate
sepallength = []
for el in enumerate(X):
    sepallength.append(el[1][0])
    
sepalwidth = []
for el in enumerate(X):
    sepalwidth.append(el[1][1])
    
random = []
random.append(np.random.uniform(min(sepallength), max(sepallength)))
random.append(np.random.uniform(min(sepalwidth), max(sepalwidth)))
print random

#calculate distance from to new point to all points
#use Euclidean distance because the measurements are numeric and in the same units
#euclidean distance is the square root of the sum of the squared differences
distances = []
count = 0
for el in X:
    euclid = np.sqrt((el[0]-random[0])**2 + (el[1]-random[1])**2 )
    distances.append([euclid, Y[count]])
    count = count + 1


#sort each point by its distance from the new point and subset the 10 nearest points (so, k=10)
distances.sort()
top10 = distances[:10]
print top10

#what is the majority class of the top 10?
majorityclass = []
for el in top10:
    majorityclass.append(el[1])
Counter(majorityclass)
print "The majority class is:"
print Counter(majorityclass).most_common()[0][0]

