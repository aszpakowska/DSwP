# okocim – lech, żywiec – fanta oraz regionalne – cola
import pandas
import scipy.stats as scs

data = pandas.read_csv('napoje.csv', sep=';', na_values='.')
cola = data['cola']
zywiec = data['żywiec']
okocim = data['okocim']
lech=data['lech']
region = data['regionalne']
fanta = data['fanta ']

bartlett_test_results1 = scs.bartlett(okocim, lech)
print("Okocim - lech: ", bartlett_test_results1)
bartlett_test_results2 = scs.bartlett(zywiec, fanta)
print("Żywiec- fanta: ", bartlett_test_results2)
bartlett_test_results3 = scs.bartlett(region, cola)
print("Regionalne-cola: ", bartlett_test_results3)