# Simulacion de el movimeinto
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def configuracion_grafica():
    plt.title("Matrices de rotacion")
    grafica.set_xlim(-1, 1)
    grafica.set_ylim(-1, 1)
    grafica.set_zlim(-1, 1)
    grafica.set_xlabel("x")
    grafica.set_ylabel("y")
    grafica.set_zlabel("z")
    grafica.view_init(elev=25, azim=30)


def sistema_coordenadas(x_inicial, y_inicial, z_inicial, x_final, y_final, z_final):
    x = [x_inicial, x_final]
    y = [y_inicial, y_final]
    z = [z_inicial, z_final]
    grafica.plot3D(x, [y_inicial, y_inicial], [z_inicial, z_inicial], color='red')
    grafica.plot3D([x_inicial, x_inicial], y, [z_inicial, z_inicial], color='blue')
    grafica.plot3D([x_inicial, x_inicial], [y_inicial, y_inicial], z, color='green')


def matriz_rotacion_z(grados):
    rad = grados / 180 * np.pi
    rotacion = np.array([[np.cos(rad), -np.sin(rad), 0],
                         [np.sin(rad), np.cos(rad), 0],
                         [0, 0, 1]])
    return rotacion


def matriz_rotacion_y(grados):
    rad = grados / 180 * np.pi
    rotacion = np.array([[np.cos(rad), 0, np.sin(rad)],
                         [0, 1, 0],
                         [-np.sin(rad), 0, np.cos(rad)]])
    return rotacion


def matriz_rotacion_x(grados):
    rad = grados / 180 * np.pi
    rotacion = np.array([[1, 0, 0],
                         [0, np.cos(rad), -np.sin(rad)],
                         [0, np.sin(rad), np.cos(rad)]])
    return rotacion


def sistema_coordenadas_movil(matriz_rotacion):
    mr_11 = matriz_rotacion[0, 0]
    mr_12 = matriz_rotacion[1, 0]
    mr_13 = matriz_rotacion[2, 0]

    mr_21 = matriz_rotacion[0, 1]
    mr_22 = matriz_rotacion[1, 1]
    mr_23 = matriz_rotacion[2, 1]

    mr_31 = matriz_rotacion[0, 2]
    mr_32 = matriz_rotacion[1, 2]
    mr_33 = matriz_rotacion[2, 2]

    grafica.plot3D([0, mr_11], [0, mr_12], [0, mr_13], color='purple')
    grafica.plot3D([0, mr_21], [0, mr_22], [0, mr_23], color='green')
    grafica.plot3D([0, mr_31], [0, mr_32], [0, mr_33], color='red')


def animacion_sistema_coordenadas(grados_x, grados_y, grados_z):
    for i in range(grados_x):
        coordenadas_funcion = np.array([[0],
                                        [0.5],
                                        [0.5]])
        rotacion_x = matriz_rotacion_x(i)
        coordenadas_funcion = np.dot(rotacion_x, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="red")
        plt.draw()
        # plt.pause(0.01)
    coordenadas_funcion_x = coordenadas_funcion
    for j in range(grados_y):
        coordenadas_funcion = coordenadas_funcion_x
        rotacion_y = matriz_rotacion_y(j)
        coordenadas_funcion = np.dot(rotacion_y, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="blue")
        plt.draw()
        # plt.pause(0.01)
    coordenadas_funcion_y = coordenadas_funcion
    for k in range(grados_z):
        coordenadas_funcion = coordenadas_funcion_y
        rotacion_z = matriz_rotacion_z(k)
        coordenadas_funcion = np.dot(rotacion_z, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="green")
        plt.draw()
        # plt.pause(0.01)


def animacion_movimiento_particula(grados_x, grados_y, grados_z):
    for i in range(grados_x):
        grafica.cla()
        configuracion_grafica()  # llamamos a la funcion configura grafica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibuja el sistema de coordenadas en el origen
        coordenadas_funcion = np.array([[0],
                                        [0.5],
                                        [0.5]])
        rotacion_x = matriz_rotacion_x(i)
        coordenadas_funcion = np.dot(rotacion_x, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="red")
        plt.draw()
        plt.pause(0.01)
    coordenadas_funcion_x = coordenadas_funcion
    for j in range(grados_y):
        grafica.cla()
        configuracion_grafica()  # llamamos a la funcion configura grafica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibuja el sistema de coordenadas en el origen
        coordenadas_funcion = coordenadas_funcion_x
        rotacion_y = matriz_rotacion_y(j)
        coordenadas_funcion = np.dot(rotacion_y, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="blue")
        plt.draw()
        plt.pause(0.01)
    coordenadas_funcion_y = coordenadas_funcion
    for k in range(grados_z):
        grafica.cla()
        configuracion_grafica()  # llamamos a la funcion configura grafica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibuja el sistema de coordenadas en el origen
        coordenadas_funcion = coordenadas_funcion_y
        rotacion_z = matriz_rotacion_z(k)
        coordenadas_funcion = np.dot(rotacion_z, coordenadas_funcion)
        x = coordenadas_funcion[0, 0]
        y = coordenadas_funcion[1, 0]
        z = coordenadas_funcion[2, 0]
        grafica.scatter(x, y, z, 'o', color="green")
        plt.draw()
        plt.pause(0.01)


figura, grafica = plt.subplots()  # Definimos una grafica
grafica = plt.axes(projection="3d")  # Configuramos la perpectiva

configuracion_grafica()  # llamamos a la funcion configura grafica
sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibuja el sistema de coordenadas en el origen
animacion_movimiento_particula(360, 360, 360)

plt.show()
