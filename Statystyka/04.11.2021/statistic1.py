import numpy as np
import pandas as pd

val = round(1/6, 2)
d = {'Value':[1,2,3,4,5,6], 'Probability':[val, val, val, val, val,val]}
data = pd.DataFrame(data=d)

print("Maksymalny wzrost:", data.max())
print("Maksymalny wzrost, funkcja:", np.max(data))
print("Minimalny wzrost:", data.min())
print("Minimalny wzrost, funkcja:", np.min(data))
print("Średni wzrost:", data.mean())
print("Średni wzrost, funkcja:", np.mean(data))
print("Odchylenie standardowe, wzrost:", data.std())
print("Odchylenie standardowe, wzrost, funkcja:", np.std(data))
print("Mediana:", np.median(data))