import scipy.stats as sps
import pandas

data = pandas.read_csv('napoje.csv', sep=';', na_values='.')
#pepsi;fanta ;żywiec;okocim;regionalne;cola;lech
test_results1 = sps.normaltest(data['pepsi'])
test_results2 = sps.normaltest(data['fanta '])
test_results3 = sps.normaltest(data['żywiec'])
test_results4 = sps.normaltest(data['okocim'])
test_results5 = sps.normaltest(data['regionalne'])
test_results6 = sps.normaltest(data['cola'])
test_results7 = sps.normaltest(data['lech'])

print("Pepsi:", test_results1)
print("Fanta:", test_results2)
print("Żywiec:", test_results3)
print("Okocim:", test_results4)
print("Regionalne:", test_results5)
print("Cola:", test_results6)
print("Lech:", test_results7)
print("If p value is lower than 0.055 then value is not normal, we could see that the reional beer is not normal")