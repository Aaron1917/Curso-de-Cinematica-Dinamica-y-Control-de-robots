import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear datos de ejemplo
x = [1, 5, 2, 10, 3]
y = [2, 3, 9, 5, 9]
z = [0, 3, 1, 5, 5.6]

# Crear la figura y el objeto de ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Trazar la línea 3D
ax.plot(x, y, z, label='Línea 3D')

# Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico
plt.show()