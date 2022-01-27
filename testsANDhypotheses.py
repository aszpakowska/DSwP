import pandas as pd
import scipy.stats as scs
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('CSV/plik.csv')
df = pd.DataFrame(df)

df2 = df
del df2['id']
del df2['city_id']
del df2['latitude']
del df2['longitude']

Berlin = df2[df2['city'] == 'Berlin']
Trondheim = df2[df2['city'] == 'Trondheim']
Krakow = df2[df2['city'] == 'Krakow']
Bratislava = df2[df2['city'] == 'Bratislava']
Budapest = df2[df2['city'] == 'Budapest']


test_results_temp_Trondheim = scs.normaltest(Trondheim['temp'])
test_results_temp_Berlin = scs.normaltest(Berlin['temp'])
test_results_temp_Krakow = scs.normaltest(Krakow['temp'])
test_results_temp_Bratislava = scs.normaltest(Bratislava['temp'])
test_results_temp_Budapest = scs.normaltest(Budapest['temp'])


print('Badanie normalności rozkładu, analiza równości wariancji')
print(f'test_results_temp_Trondheim: {test_results_temp_Trondheim}')
print(f'test_results_temp_Berlin: {test_results_temp_Berlin}')
print(f'test_results_temp_Krakow: {test_results_temp_Krakow}')
print(f'test_results_temp_Bratislava: {test_results_temp_Bratislava}')
print(f'test_results_temp_Budapest: {test_results_temp_Budapest}')

Berlin = df2[df2['city'] == 'Berlin'].tail(4).sort_values('timeoflastcheck')
Trondheim = df2[df2['city'] == 'Trondheim'].tail(
    4).sort_values('timeoflastcheck')
Krakow = df2[df2['city'] == 'Krakow'].tail(4).sort_values('timeoflastcheck')
Bratislava = df2[df2['city'] == 'Bratislava'].tail(
    4).sort_values('timeoflastcheck')
Budapest = df2[df2['city'] == 'Budapest'].tail(
    4).sort_values('timeoflastcheck')

cities = [Berlin, Trondheim, Krakow, Bratislava, Budapest]
for city in cities:
    del city['country']
    del city['city']
    del city['condition']
    del city['timeoflastcheck']

results1 = scs.bartlett(Berlin.values.flatten(), Krakow.values.flatten())
results2 = scs.bartlett(Bratislava.values.flatten(),
                        Trondheim.values.flatten())
results3 = scs.bartlett(Krakow.values.flatten(), Berlin.values.flatten())
print('******************************************')
print(f'results1: {results1}')
print(f'results2: {results2}')
print(f'results3: {results3}')

results1 = scs.ttest_ind(Berlin.values.flatten(), Krakow.values.flatten())
results2 = scs.ttest_ind(Bratislava.values.flatten(),
                         Trondheim.values.flatten())
results3 = scs.ttest_ind(Krakow.values.flatten(), Berlin.values.flatten())
print('**********Testy dla zmiennych zależnych, niezależnych************')
print("*************Test t-studenta************")
print(f'results1: {results1}')
print(f'results2: {results2}')
print(f'results3: {results3}')

results1 = scs.f_oneway(Berlin.values.flatten(), Krakow.values.flatten())
results2 = scs.f_oneway(Bratislava.values.flatten(),
                        Trondheim.values.flatten())
results3 = scs.f_oneway(Krakow.values.flatten(), Berlin.values.flatten())

print('*****************Testy dla wielu średnich***************')
print('***********ONE-WAY ANOVA***********')
print(f'results1: {results1}')
print(f'results2: {results2}')
print(f'results3: {results3}')