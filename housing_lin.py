    # Importing Libraries
    
    # Utility Libraries
    # Importing Libraries
    
    # Utility Libraries
import numpy as np
import pandas as pd
    
    # Visualisation Libraries
import seaborn as sns
import matplotlib.pyplot as plt
    
    # Data Processing Libraries
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import model_selection
from sklearn.metrics import mean_squared_error, r2_score
    
    # Algorithm Libraries
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
    
    # Math Library
import math
    
    # Importing Dataset
df = pd.read_csv("/kaggle/input/boston-housing-dataset/HousingData.csv")
    
    # Printing Dataset
df.head()
