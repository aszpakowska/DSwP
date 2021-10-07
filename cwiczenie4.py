import pandas as pd
import matplotlib.pyplot as plt
from pandas import plotting

data = pd.read_csv('brain_size.csv', sep=';', na_values=".")

srednia = pd.DataFrame(data,columns=['VIQ']).mean()
print("Średnia: ", srednia,"\n")
print("Felame/Male Counter: \n", data['Gender'].value_counts())


plotting.scatter_matrix(data[['VIQ','PIQ','FSIQ']])
plt.title('First')
plt.show()

woman = data[data.Gender == 'Female']
plotting.scatter_matrix(woman[['VIQ','PIQ','FSIQ']])
plt.title("Second")
plt.show()

