import scipy.stats as scs
import pandas as pd

napoje_data = pd.read_csv('napoje.csv', sep=';', na_values='.')
lech= napoje_data['lech']
cola=napoje_data['cola']
regionalne=napoje_data['regionalne']

lechresult=scs.ttest_1samp(lech,60500)
colaresult=scs.ttest_1samp(cola,222000)
regionalneresult=scs.ttest_1samp(regionalne,43500)
if regionalneresult[1] > 0.5 and colaresult[1]>0.5 and lechresult[1]>0.5:
    print("nie ma podstaw do odrzucenia ")
else:
    print("mozna odrzucic ")