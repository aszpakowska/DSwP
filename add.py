#series to dataframe
from statistic import *
from connection import *

data7 = data7.to_frame()
data7.reset_index(level=0, inplace=True)
data7
data7.to_sql('python_mean_humidity', conn, if_exists='replace', index=False)

data8 = data8.to_frame()
data8.reset_index(level=0, inplace=True)
data8
data8.to_sql('python_mean_pressure', conn, if_exists='replace', index=False)

data9 = data9.to_frame()
data9.reset_index(level=0, inplace=True)
data9
data9.to_sql('python_mean_temperature', conn, if_exists='replace', index=False)

data10 = data10.to_frame()
data10.reset_index(level=0, inplace=True)
data10
data10.to_sql('python_median_temperature', conn, if_exists='replace', index=False)

data11 = data11.to_frame()
data11.reset_index(level=0, inplace=True)
data11
data11.to_sql('python_median_pressure', conn, if_exists='replace', index=False)


data12 = data12.to_frame()
data12.reset_index(level=0, inplace=True)
data12
data12.to_sql('python_median_humidity', conn, if_exists='replace', index=False)


data13 = data13.to_frame()
data13.reset_index(level=0, inplace=True)
data13
data13.to_sql('python_std_humidity', conn, if_exists='replace', index=False)

data14 = data14.to_frame()
data14.reset_index(level=0, inplace=True)
data14
data14.to_sql('python_std_pressure', conn, if_exists='replace', index=False)


data15 = data15.to_frame()
data15.reset_index(level=0, inplace=True)
data15
data15.to_sql('python_std_temperature', conn, if_exists='replace', index=False)