import scipy.stats as scs

norm_generated = scs.norm.rvs(loc=2, scale=30, size=200)
results = scs.ttest_1samp(norm_generated,2.5)

print(results)