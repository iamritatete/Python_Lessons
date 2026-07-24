import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

data = pd.read_csv("C:\\Users\\Amrita Tete\\Documents\\SimpliLearn\\Code\\dataset\\Lesson_03_Supervised_Learning_ Regression_and_its_Application\\position_salaries.csv")

# data.info()

X=data.iloc[:, 0:1].values
y=data.iloc[:, 1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#training the model
#sk trial