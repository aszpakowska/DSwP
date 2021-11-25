import scipy.stats as scs


p=0.3
data=scs.bernoulli.rvs(p=p,size=100)
data1=scs.poisson.rvs(size=100,mu=2)
data2=scs.binom.rvs(p=p,n=100)
print(data)
print(data1)
print(data2)
mean, var, skew, kurt = scs.bernoulli.stats(p,moments='mvsk')
print('~~~~~~~~~~~~~~bernoulli~~~~~~~~~~~~')
print("Średnia: ", mean)
print("Wariancja: ", var)
print("Skośność: ", skew)
print("Kurtoza: ", kurt)

mean1, var1, skew1, kurt1 = scs.poisson.stats(mu=2,moments='mvsk')
print('~~~~~~~~~~~~~~~poisson~~~~~~~~~~~~~~')

print("Średnia: ", mean1)
print("Wariancja: ", var1)
print("Skośność: ", skew1)
print("Kurtoza: ", kurt1)

mean2, var2, skew2, kurt2 = scs.binom.stats(p=p,moments='mvsk',n=100)
print('~~~~~~~~~~~~~~binom~~~~~~~~~~~~~~')

print("Średnia: ", mean2)
print("Wariancja: ", var2)
print("Skośność: ", skew2)
print("Kurtoza: ", kurt2)