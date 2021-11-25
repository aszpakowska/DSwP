import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt

n = 20
p = 0.4
k = np.arange(0, 20)
binominal = scs.binom.pmf(k, n, p)
print(binominal)
print(sum(binominal))