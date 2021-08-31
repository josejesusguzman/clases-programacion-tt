# Visualizar datos aleatoreos en una grafica
import random 
import matplotlib.pyplot as plt

# Generar la data aleatorea
x = range(0,100)
y = [random.randint(0, 100) for i in range(0,100)]

# Mostrar la grafica
plt.plot(x, y)
plt.show()