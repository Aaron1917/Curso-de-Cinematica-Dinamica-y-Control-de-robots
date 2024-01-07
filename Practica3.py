import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def rotacion(grados, datos, linea_3D):
    rad = grados / 180 * np.pi
    matriz_rotacion_z = np.array([[np.cos(rad), -np.sin(rad), 0],
                                  [np.sin(rad), np.cos(rad), 0],
                                  [0, 0, 1]])
    datos = matriz_rotacion_z @ datos
    # Actualizo la posición de los datos de la lines
    linea_3D.set_data(datos[0], datos[1])
    linea_3D.set_3d_properties(datos[2])
    return linea_3D


# Declaramos la figura
figura = plt.figure()
grafica = Axes3D(figura)

# Declaramos los datos para la graficación
x = np.arange(0, 6, 1)
y = x
z = x * 0

datos = np.array([x, y, z])
grados = 360
linea_3D = plt.plot(datos[0], datos[1], datos[2])[0]

# Configuramos las propiedades de la figura como lo son los ejes
grafica.set_xlim(-10, 10)
grafica.set_ylim(-10, 10)
grafica.set_zlim(0, 10)

grafica.set_xlabel('x(t)')
grafica.set_ylabel('y(t)')
grafica.set_zlabel('z(t)')

linea_animada = animation.FuncAnimation(figura, rotacion,
                                        frames=360, fargs=(datos, linea_3D),
                                        interval=50, repeat=False, blit=False)
plt.show()

print(len(x))
