# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from collections import OrderedDict
from sklearn.ensemble import RandomForestClassifier#,ExtraTreesClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
#import copy
import warnings
warnings.filterwarnings('ignore')
#import random

titanic = sns.load_dataset('titanic')
df = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

#データの前処理:単一代入法によって、欠損値を補完する
df = df[["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Cabin","Embarked"]]
X = df[['Pclass', 'Age', 'Sex', 'SibSp', 'Parch', 'Fare','Cabin','Embarked']].values
Y = df['Survived'].values

train,test=train_test_split(df,test_size=0.4,random_state=0)

#Sexで男性を1、女性を0に置換する
df["Sex"][df["Sex"] == "male"] = 0
df["Sex"][df["Sex"] == "female"] = 1
#Embarkedの欠損値をSで補完する
df["Embarked"] = df["Embarked"].fillna("S")
#EmbarkedをSを0、Cを1、Qを2に置換する
df["Embarked"][df["Embarked"] == "S" ] = 0
df["Embarked"][df["Embarked"] == "C" ] = 1
df["Embarked"][df["Embarked"] == "Q" ] = 2

#訓練用データと検証用データのAgeを平均値で補完する
train_mean=train.copy()
train_mean["Age"] = train_mean["Age"].fillna(train_mean["Age"].mean())
test_mean=test.copy()
test_mean["Age"] = test_mean["Age"].fillna(test_mean["Age"].mean())
 
#RandomForestClassifier:決定木のアンサンブル学習で補完したデータを使って学習させる
RANDOM_STATE=123
X,y=make_classification(n_samples=500,n_features=25,n_informative=15,n_clusters_per_class=1,random_state=RANDOM_STATE)
ensemble_clfs=[
    ("RandomForestClassifier,max_features='sqrt'",RandomForestClassifier(warm_start=True,oob_score=True,max_features='sqrt',random_state=RANDOM_STATE)),("RandomForestClassifier,max_features='log2'",RandomForestClassifier(warm_start=True,max_features='log2',oob_score=True,random_state=RANDOM_STATE)),("RandomForestClassifier,max_features=None",RandomForestClassifier(warm_start=True,max_features='None',oob_score=True,random_state=RANDOM_STATE))
               ]
error_rate=OrderedDict((label,[])for label,_ in ensemble_clfs)
min_estimates=15
max_estimates=175


for label, clf in ensemble_clfs:
    for i in range(min_estimates,max_estimates+1):
        clf.set_params(n_estimators=i)
        clf.fit(X,y)
        
        oob_error=1-clf.oob_score_
        error_rate[label].append((i,oob_error))
        
for label,clf in ensemble_clfs:
    for i in range(min_estimates,max_estimates+1):
        clf.set_params(n_estimators=i)
        clf.fit(X,y)
        oob_error=1-clf.oob_score_
        error_rate[label].append((i,oob_error))
    
forest=RandomForestClassifier(criterion='entropy',n_estimators=10,random_state=1,n_jobs=2)
forest.fit(x_train,y_train)      

#交差検定で精度を確認する

#提出用の形式に変換する
        
        
