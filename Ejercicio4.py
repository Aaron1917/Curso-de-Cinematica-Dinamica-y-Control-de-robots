import matplotlib.pyplot as plt  # Importamos la librerias
from matplotlib import cm
import numpy as np


# Declaramos las funciones para obtener las matrices de rotación


def matriz_rotacion_x(grados):
    # Función para obtener la matriz de rotación sobre el eje X a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = (np.pi / 180) * grados  # Transformamos a radianes
    # Declaramos la matriz de rotación para el eje x
    rotacion = np.array([[1, 0, 0],
                         [0, np.cos(rad), -np.sin(rad)],
                         [0, np.sin(rad), np.cos(rad)]])
    return rotacion  # Retornamos la matriz resultante


def matriz_rotacion_y(grados):
    # Función para obtener la matriz de rotación sobre el eje Y a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = grados / 180 * np.pi  # Transformamos a radianes
    # Declaramos la matriz de rotación para el eje x
    rotacion = np.array([[np.cos(rad), 0, np.sin(rad)],
                         [0, 1, 0],
                         [-np.sin(rad), 0, np.cos(rad)]])
    return rotacion  # Retornamos la matriz resultante


def matriz_rotacion_z(grados):
    # Función para obtener la matriz de rotación sobre el eje Z a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = grados / 180 * np.pi  # Transformamos a radianes
    # Declaramos la matriz de rotación para el eje x
    rotacion = np.array([[np.cos(rad), -np.sin(rad), 0],
                         [np.sin(rad), np.cos(rad), 0],
                         [0, 0, 1]])
    return rotacion  # Retornamos la matriz resultante


def configuracion_grafica():
    # Colocamos el título
    plt.title("Matrices de rotación")
    # Colocamos los limites en los ejes
    grafica.set_xlim(-5, 5)
    grafica.set_ylim(-5, 5)
    grafica.set_zlim(-5, 5)
    # Colocamos las etiquetas en cada eje
    grafica.set_xlabel("x")
    grafica.set_ylabel("y")
    grafica.set_zlabel("z")


def rota_barra(MR, _barra):
    # Guardamos los puntos en una variable
    p1 = _barra[0]
    p2 = _barra[1]
    p3 = _barra[2]
    p4 = _barra[3]
    p5 = _barra[4]
    p6 = _barra[5]
    p7 = _barra[6]
    p8 = _barra[7]
    # Multiplicamos los puntos por la matriz de rotación
    p1 = MR @ p1.T
    p2 = MR @ p2.T
    p3 = MR @ p3.T
    p4 = MR @ p4.T
    p5 = MR @ p5.T
    p6 = MR @ p6.T
    p7 = MR @ p7.T
    p8 = MR @ p8.T
    # Obtenemos una nueva barra
    new_barra = np.array([p1.T, p2.T, p3.T, p4.T,
                          p5.T, p6.T, p7.T, p8.T])
    return new_barra    # Retornamos la barra


def crea_barra(_bar):
    # Creamos las 12 aristas con las lines 3D en base a los 8 vértices
    grafica.plot3D([_bar[0, 0], _bar[1, 0]], [_bar[0, 1], _bar[1, 1]], [_bar[0, 2], _bar[1, 2]], color="black")
    grafica.plot3D([_bar[0, 0], _bar[3, 0]], [_bar[0, 1], _bar[3, 1]], [_bar[0, 2], _bar[3, 2]], color="black")
    grafica.plot3D([_bar[1, 0], _bar[2, 0]], [_bar[1, 1], _bar[2, 1]], [_bar[1, 2], _bar[2, 2]], color="black")
    grafica.plot3D([_bar[3, 0], _bar[2, 0]], [_bar[3, 1], _bar[2, 1]], [_bar[3, 2], _bar[2, 2]], color="black")

    grafica.plot3D([_bar[4, 0], _bar[0, 0]], [_bar[4, 1], _bar[0, 1]], [_bar[4, 2], _bar[0, 2]], color="black")
    grafica.plot3D([_bar[5, 0], _bar[1, 0]], [_bar[5, 1], _bar[1, 1]], [_bar[5, 2], _bar[1, 2]], color="black")
    grafica.plot3D([_bar[6, 0], _bar[2, 0]], [_bar[6, 1], _bar[2, 1]], [_bar[6, 2], _bar[2, 2]], color="black")
    grafica.plot3D([_bar[7, 0], _bar[3, 0]], [_bar[7, 1], _bar[3, 1]], [_bar[7, 2], _bar[3, 2]], color="black")

    grafica.plot3D([_bar[4, 0], _bar[5, 0]], [_bar[4, 1], _bar[5, 1]], [_bar[4, 2], _bar[5, 2]], color="black")
    grafica.plot3D([_bar[5, 0], _bar[6, 0]], [_bar[5, 1], _bar[6, 1]], [_bar[5, 2], _bar[6, 2]], color="black")
    grafica.plot3D([_bar[6, 0], _bar[7, 0]], [_bar[6, 1], _bar[7, 1]], [_bar[6, 2], _bar[7, 2]], color="black")
    grafica.plot3D([_bar[7, 0], _bar[4, 0]], [_bar[7, 1], _bar[4, 1]], [_bar[7, 2], _bar[4, 2]], color="black")


def anim_bar(ang_x, ang_y, ang_z, _barra):
    for i in range(ang_x):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_x = matriz_rotacion_x(i)     # Obtenemos la matriz de rotación
        bar_x = rota_barra(MR_x, _barra)        # Rotamos la barra
        crea_barra(bar_x)       # Graficamos la barra
        plt.draw()      # Dibujamos las lineas
        plt.pause(0.01)     # Agregamos una pausa
    for j in range(ang_y):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_y = matriz_rotacion_y(j)     # Obtenemos la matriz de rotación
        bar_y = rota_barra(MR_y, bar_x)     # Rotamos la barra
        crea_barra(bar_y)       # Graficamos la barra
        plt.draw()      # Dibujamos las lineas
        plt.pause(0.01)     # Agregamos una pausa
    for k in range(ang_z):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_z = matriz_rotacion_z(k)     # Obtenemos la matriz de rotación
        bar_z = rota_barra(MR_z, bar_y)     # Rotamos la barra
        crea_barra(bar_z)       # Graficamos la barra
        plt.draw()      # Dibujamos las lineas
        plt.pause(0.01)     # Agregamos una pausa
    return bar_z        # Retornamos la barra


def rota_puntos(matriz_rotacion, surface_):
    new_surface = np.zeros(surface_.shape)  # Creamos una matriz nueva de las mismas dimenciones
    for i in range(surface_.shape[1]):      # Iniciamos un for
        for j in range(surface_.shape[2]):  # Iniciamos otro for anidado
            # Creamos un vector transpuesto
            vector = np.array([[surface_[0, i, j]],
                               [surface_[1, i, j]],
                               [surface_[2, i, j]]])
            # Multiplicamos la matriz por el vector
            vector = matriz_rotacion @ vector
            # Guardamos los valores de la superficie
            new_surface[0, i, j] = vector[0, 0]
            new_surface[1, i, j] = vector[1, 0]
            new_surface[2, i, j] = vector[2, 0]

    return new_surface      # Retornamos la superficie


def dibuja_superficie(ang_x, ang_y, ang_z, surface_):
    # Rotamos la superficie en el eje x
    for i in range(ang_x):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_X = matriz_rotacion_x(i)     # Obtenemos la matriz de rotación
        surface_x = rota_puntos(MR_X, surface_)     # Rotamos la superficie
        # Graficamos la superficie
        grafica.plot_surface(surface_x[0], surface_x[1], surface_x[2], rstride=1, cstride=1, cmap=cm.coolwarm,
                             linewidth=0, antialiased=False)
        plt.pause(0.1)      # Generamos una pausa
    for i in range(ang_y):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_Y = matriz_rotacion_y(i)     # Obtenemos la matriz de rotación
        surface_y = rota_puntos(MR_Y, surface_x)    # Rotamos la superficie
        # Graficamos la superficie
        grafica.plot_surface(surface_y[0], surface_y[1], surface_y[2], rstride=1, cstride=1, cmap=cm.coolwarm,
                             linewidth=0, antialiased=False)
        plt.pause(0.1)      # Generamos una pausa
    for i in range(ang_z):
        grafica.cla()
        configuracion_grafica()     # Configuramos la gráfica
        MR_Z = matriz_rotacion_z(i)     # Obtenemos la matriz de rotación
        surface_z = rota_puntos(MR_Z, surface_y)    # Rotamos la superficie
        # Graficamos la superficie
        grafica.plot_surface(surface_z[0], surface_z[1], surface_z[2], rstride=1, cstride=1, cmap=cm.coolwarm,
                             linewidth=0, antialiased=False)
        plt.pause(0.1)      # Generamos una pausa
    return surface_z


figura, grafica = plt.subplots()  # Definimos una grafica
grafica = plt.axes(projection="3d")  # Configuramos la perspectiva 3D

# Definimos los 8 puntos que conformarían una barra
mi_barra = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

anim_bar(45, 45, 45, mi_barra)  # Llamamos la funcion para rotar la barra
plt.pause(5)        # agregamos un pausa de 5segundos

# Creamos la función de la superficie
X = np.arange(-5, 5, 0.25)  # Generamos un vector
Y = np.arange(-5, 5, 0.25)  # Generamos un vector

X, Y = np.meshgrid(X, Y)  # Generamos los puntos intermediso entre ambos ejes
R = np.sqrt(X ** 2 + Y ** 2)  # Calculamos la función
Z = np.sin(R)  # Calculamos z

superficie = np.array([X, Y, Z])    # Creamos la matriz de superficie

dibuja_superficie(45, 45, 45, superficie)   # Se llama a la función que sibuja la superficie
plt.show()
