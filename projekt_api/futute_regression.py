import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


df = pd.read_csv('CSV/plik.csv')
df2 = df

# plot mintemp vs maxtemp
df.plot(kind='scatter',title='mintemp vs maxtemp', x='mintemp', y='maxtemp', alpha=0.5)
plt.show()

X = df['mintemp'].values.reshape(-1, 1)
y = df['maxtemp'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)  # training the algorithm

# To retrieve the intercept:
print(regressor.intercept_)
# For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred,title='Prediction', color='red', linewidth=2)
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(
    metrics.mean_squared_error(y_test, y_pred)))