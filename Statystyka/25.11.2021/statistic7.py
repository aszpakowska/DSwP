import pandas
import scipy.stats as scs

data = pandas.read_csv('napoje.csv', sep=';', na_values='.')
data2 = pandas.read_csv('napoje_po_reklamie.csv', sep=';', na_values='.')


is2016 = data['rok']==2016
is2016_2 = data[is2016]
cola= is2016_2['cola']

is2016 = data['rok']==2016
is2016_2 = data[is2016]
fanta= is2016_2['fanta ']

is2016 = data['rok']==2016
is2016_2 = data[is2016]
pepsi= is2016_2['pepsi']


results = scs.ttest_ind(cola, data2['cola'])
print("Cola: ", results)
results2 = scs.ttest_ind(fanta, data2['fanta '])
print("Fanta: ", results2)
results3 = scs.ttest_ind(pepsi, data2['pepsi'])
print(results3)