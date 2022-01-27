from conncection import *


data1 = df.groupby(df['city'])['maxtemp'].max()
print("Max temperature:", data1.max(), "in city: ", data1.idxmax())

data2 = df.groupby(df['city'])['mintemp'].min()
print("Min temperature:", data2.min(), "in city: ", data2.idxmin())

data3 = df.groupby(df['city'])['humidity'].max()
print("Max humidity:", data3.max(), "in city: ", data3.idxmax())

data4 = df.groupby(df['city'])['humidity'].min()
print("Min humidity:", data4.min(), "in city: ", data4.idxmin())

data5 = df.groupby(df['city'])['pressure'].max()
print("Max pressure:", data5.max(), "in city: ", data5.idxmax())

data6 = df.groupby(df['city'])['pressure'].min()
print("Min pressure:", data6.min(), "in city: ", data6.idxmin())

data7 = df.groupby(df['city'])['humidity'].mean()
print("**************Mean humidity:***************", data7)
#data7.to_sql('python_mean_humidity', conn, if_exists='replace', index = False)


data8 = df.groupby(df['city'])['pressure'].mean()
print("*************Mean pressure:*****************", data8)
# data8.to_sql('python_mean_pressure', conn, if_exists='replace', index=False)


data9 = df.groupby(df['city'])['temp'].mean()
print("***********Mean temperature:*****************", data9)
data9 = data9.to_frame()

data10 = df.groupby(df['city'])['temp'].median()
print("***********Median of temperature:*****************", data10)
#data10.to_sql('python_median_temp', conn, if_exists='append', index=False)

data11 = df.groupby(df['city'])['pressure'].median()
print("*************Median of pressure:*****************", data11)

data12 = df.groupby(df['city'])['humidity'].median()
print("**************Median of humidity:***************", data12)

data13 = df.groupby(df['city'])['humidity'].std()
print("**************standard deviation of humidity:***************", data13)

data14 = df.groupby(df['city'])['pressure'].std()
print("**************standard deviation of pressure:***************", data14)

data15 = df.groupby(df['city'])['temp'].std()
print("**************standard deviation of temperature:***************", data15)
