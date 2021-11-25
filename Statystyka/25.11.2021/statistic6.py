import pandas
import scipy.stats as scs

data = pandas.read_csv('napoje.csv', sep=';', na_values='.')


is2015 = data['rok']==2015
is2015_2 = data[is2015]
region1= is2015_2['regionalne']

is2001 = data['rok'] == 2001
is2001_2 = data[is2001]
region2 = is2001_2['regionalne']


results = scs.ttest_ind(region1, region2)
print(results)