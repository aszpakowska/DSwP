import numpy as np
import scipy.stats as scp

data = np.loadtxt("Wzrost.csv", delimiter=',', skiprows=0, unpack=True)
#print(data)

print("Miara koncentracji: ", scp.kurtosis(data))
print("Podstawowe statystyki opisowe rozkładu: ", scp.describe(data))
print("Skośność rozkładu: ", scp.skew(data))
#Miara koncentracji - Informuje ona o poziomie spłaszczenia rozkładu. Wartość 0
#informuje o spłaszczeniu zbliżonym do normalnego, natomiast liczba dodatnia mówi o większej koncentracji
#wokół średniej, a liczba ujemna o większym spłaszczeniu rozkładu.

#skośność - Gdy wartość jest bliska zero, oznacza, że rozkład jest symetryczny. Gdy
#wartość jest mniejsza od zera – rozkład lewostronnie skośny, gdy większa od zera – rozkład prawostronnie
#skośny.