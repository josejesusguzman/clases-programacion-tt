import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('datasets\\iris.csv', names=[
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm',
    'Species'
])

datax = iris['SepalLengthCm'].values
datay = iris['SepalWidthCm'].values

plt.plot(datax, datay, 'ro')
plt.axis([0, 10, 0, 10])
plt.title("Datasets de plantas")
plt.xlabel("Longitud de pétalo")
plt.ylabel("Anchura de pétalo")

plt.show()
