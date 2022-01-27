import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('CSV/plik.csv')
df2 = df

X2 = df2['mintemp'].values.reshape(-1, 1)
y2 = df2['maxtemp'].values.reshape(-1, 1)

y2 = y2.reshape(-1,)

X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2, random_state=0)

regressor2 = LogisticRegression(solver='lbfgs', max_iter=3000)
regressor2.fit(X_train2, y_train2)  # training the algorithm

y_pred2 = regressor2.predict(X_test2)

df2 = pd.DataFrame({'Actual': y_test2.flatten(),
                   'Predicted': y_pred2.flatten()})
print(df2)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test2, y_pred2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test2, y_pred2))
print('Root Mean Squared Error:', np.sqrt(
    metrics.mean_squared_error(y_test2, y_pred2)))