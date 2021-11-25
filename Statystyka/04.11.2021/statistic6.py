import scipy.stats as scs
import numpy as np

norm_generated = scs.norm.rvs(loc=0, scale=2, size=100)
mean, var, skew, kurt = scs.norm.stats(loc=0, scale=2, moments = 'mvsk')
print(norm_generated)
print('Size = 100')
print('Średnia wygenerowana:', np.mean(norm_generated))
print('Średnia teoretyczna:', mean)
print('Odchylenie wygenerowane:', np.std(norm_generated))
print('Odchylenie teoretyczne:', np.sqrt(var))

print('Size = 100 000')
norm_generated = scs.norm.rvs(loc=0, scale=2, size=100000)
print('Średnia wygenerowana:', np.mean(norm_generated))
print('Odchylenie wygenerowane:', np.std(norm_generated))