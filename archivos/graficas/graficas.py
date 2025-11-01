import matplotlib.pyplot as plt
import numpy as np
import math
y = [1,3,5,7,9,11,13]
x = [2,3,4,7,8,12,15]
for i in range (100):
    x.append(i)
for i in range(100):
    y.append(math.cos(      ))
# Datos
##x = np.linspace(0, 10, 100)
#y = np.sin(x)

# Crear la gráfica
plt.scatter(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('sin(X)')

# Mostrar la gráfica
plt.show()