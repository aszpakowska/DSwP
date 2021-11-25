import scipy.stats as scs
import numpy as np
import matplotlib.pyplot as plt

norm_generated = scs.norm.rvs(loc=1, scale=2, size=100)
fig, ax = plt.subplots(1, 1)
x = np.linspace(scs.norm.ppf(0.01), scs.norm.ppf(0.99), 100)
ax.plot(x, scs.norm.pdf(x), 'r-', lw=6, alpha=0.5, label='Standardowy')
x = np.linspace(scs.norm.ppf(0.01, loc=-1, scale=0.5), scs.norm.ppf(0.99, loc=-1, scale=0.5), 100)
ax.plot(x, scs.norm.pdf(x, loc=-1, scale=0.5), 'k-', lw=3, label='Normalny – z próby')
ax.hist(norm_generated, density=True, histtype='bar', alpha=0.3)
ax.legend(loc='best')
plt.show()