import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def configuracion_grafica():
    plt.title("Matrices de rotación")
    grafica.set_xlim(-5, 5)
    grafica.set_ylim(-5, 5)
    grafica.set_zlim(-5, 5)
    grafica.set_xlabel("x")
    grafica.set_ylabel("y")
    grafica.set_zlabel("z")
    grafica.view_init(elev=25, azim=30)


def sistema_coordenadas(x_i, y_i, z_i, x_f, y_f, z_f):
    x = [x_i, x_f]
    y = [y_i, y_f]
    z = [z_i, z_f]
    grafica.plot3D(x, [y_i, y_i], [z_i, z_i], color="red")
    grafica.plot3D([x_i, x_i], y, [z_i, z_i], color="blue")
    grafica.plot3D([x_i, x_i], [y_i, y_i], z, color="green")


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
    rotacion = np.array([[0, 0, 1],
                         [np.cos(rad), -np.sin(rad), 0],
                         [np.sin(rad), np.cos(rad), 0]])
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

    grafica.plot3D([0, mr_11], [0, mr_12], [0, mr_13], color="purple")
    grafica.plot3D([0, mr_21], [0, mr_22], [0, mr_23], color="gray")
    grafica.plot3D([0, mr_31], [0, mr_32], [0, mr_33], color="cyan")


def animacion_sistema_cordenadas(grados_x, grados_y, grados_z):
    for i in range(grados_x):
        grafica.cla()
        configuracion_grafica()  # Llamamos la funcion configura gráfica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibua sistema de coordenadas en origen
        rotacionx = matriz_rotacion_x(i)  # Rota derminados grafos la rotacion en z
        sistema_coordenadas_movil(rotacionx)
        plt.draw()
        plt.pause(0.01)
    for j in range(grados_y):
        grafica.cla()
        configuracion_grafica()  # Llamamos la funcion configura gráfica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibua sistema de coordenadas en origen
        rotaciony = matriz_rotacion_y(j)  # Rota derminados grafos la rotacion en z
        sistema_coordenadas_movil(rotaciony)
        plt.draw()
        plt.pause(0.01)
    for k in range(grados_z):
        grafica.cla()
        configuracion_grafica()  # Llamamos la funcion configura gráfica
        sistema_coordenadas(0, 0, 0, 1, 1, 1)  # Dibua sistema de coordenadas en origen
        rotacionz = matriz_rotacion_z(k)  # Rota derminados grafos la rotacion en z
        sistema_coordenadas_movil(rotacionz)
        plt.draw()
        plt.pause(0.01)


def dibuja_barra():
    grafica.cla()
    configuracion_grafica()
    sistema_coordenadas(0, 0, 0, 1, 1, 1)
    coordenadas_funcion= np.array([[0], [0.5], [0.5]])
    x = coordenadas_funcion[0]
    y = coordenadas_funcion[1]
    z = coordenadas_funcion[2]
    dx = np.ones(20)
    dy = np.ones(20)
    dz = np.ones(20)*4
    grafica.bar3d(x, y, z, dx, dy, dz)
    plt.draw()


def funcion1():
    grafica.cla()
    configuracion_grafica()
    sistema_coordenadas(0, 0, 0, 1, 1, 1)
    x = np.arange(-5, 5, 0.25)      # Generamos un vector
    y = np.arange(-5, 5, 0.25)      # Generamos un vector

    x, y = np.meshgrid(x, y)        # Generamos los puntos intermediso entre ambos ejes
    R = np.sqrt(x**2+y**2)       # Calculamos la función
    z = np.sin(R)

    surface = grafica.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

figura, grafica = plt.subplots()  # Definimos una grafica
grafica = plt.axes(projection="3d")  # Configuramos la perspectiva 3D

# funcion1()
# dibuja_barra()
animacion_sistema_cordenadas(45, 45, 45)
plt.show()
