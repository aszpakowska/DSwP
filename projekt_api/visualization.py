import matplotlib.pyplot as plt

from conncection import *

temp = pd.read_sql("SELECT * FROM temp_summary", engine)
temp.to_csv('CSV/temp_summary.csv')

plt.figure(1)
temp.plot(kind='bar', x='city', y='avg_temp', color='cyan', figsize=(15, 15), alpha=0.5)
plt.show()

humidity = pd.read_sql("SELECT * FROM humidity_summary", engine)
humidity.to_csv('CSV/humidity_summary.csv')
plt.figure(2)
humidity.plot(kind='bar', x='city', y='avg_humidity', color='magenta', figsize=(15, 15), alpha=0.5)
plt.show()

pressure = pd.read_sql("SELECT * FROM PRESSURE_SUMMARY", engine)
pressure.to_csv('CSV/pressure_summary.csv')
plt.figure(3)
pressure.plot(kind='bar', x='city', y='avg_pressure', color='orange', figsize=(15, 15), alpha=0.5)
plt.show()
