import pandas
import scipy.stats as scs
data = pandas.read_csv('napoje.csv', sep=';', na_values='.')
cola = data['cola']
pepsi = data['pepsi']
okocim = data['okocim']
lech=data['lech']
region = data['regionalne']
fanta = data['fanta ']


results1 = scs.ttest_ind(pepsi, cola)
results2 = scs.ttest_ind(fanta, region)
results3 = scs.ttest_ind(okocim, lech)

print("Result cola-pepsi: ", results1)
print("Results okocim-lech: ", results3)
print("Results fanta-regionalne: ", results2)
