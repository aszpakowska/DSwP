import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt
mu = 2
x = np.arange(scs.poisson.ppf(0.01, mu), scs.poisson.ppf(0.99, mu))
rv = scs.poisson(mu)
fig,ax = plt.subplots(1 ,1)
ax.vlines(x,0,rv.pmf(x), colors='b', linestyles='-', lw=1, label='frozenpmf')
ax.legend(loc='best', frameon=False)
plt.show()