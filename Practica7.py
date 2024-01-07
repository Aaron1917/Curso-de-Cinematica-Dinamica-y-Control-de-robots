# Simulacion del movimiento de una función en 3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def configuracion_grafica(x_lim_inf, xlim_sup, y_lim_inf, ylim_sup, z_lim_inf, zlim_sup, titulo):
    plt.title(titulo)
    # Definimos los limites de la gráfica
    grafica.set_xlim(x_lim_inf, xlim_sup)
    grafica.set_ylim(y_lim_inf, ylim_sup)
    grafica.set_zlim(z_lim_inf, zlim_sup)

    # Definimos los ejes de la gráfica
    grafica.set_xlabel("X")
    grafica.set_ylabel("Y")
    grafica.set_zlabel("Z")
    # grafica.view_init(elev=45, azim=45)


def matriz_rotacion(angulo, direccion):
    # Cambiamos el angulo de rotacion a radianes
    rad = angulo / 180 * np.pi
    # Dependiendo de la direccion de rotacion, definimos la matriz de rotacion
    rotacion = np.zeros((3, 3))
    if direccion == "x":
        rotacion = np.array([[1, 0, 0],
                             [0, np.cos(rad), -np.sin(rad)],
                             [0, np.sin(rad), np.cos(rad)]])
    elif direccion == "y":
        rotacion = np.array([[np.cos(rad), 0, np.sin(rad)],
                             [0, 1, 0],
                             [-np.sin(rad), 0, np.cos(rad)]])
    elif direccion == "z":
        rotacion = np.array([[np.cos(rad), -np.sin(rad), 0],
                             [np.sin(rad), np.cos(rad), 0],
                             [0, 0, 1]])
    # Retornamos la matriz de rotacion
    return rotacion


def animacion_funcion_3D(grados_x, grados_y, grados_z):
    for i in range(grados_x):
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Función tipo sólido")
        # Establecemos las coordenadas del sólido
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)

        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)
        indice = 0
        for datos in zip(X, Y, Z):
            coordenadas_funcion = np.array([datos[0], datos[1], datos[2]])
            rotacion = matriz_rotacion(i, "x")

            resultado = rotacion @ coordenadas_funcion
            X[indice] = resultado[0]
            Y[indice] = resultado[1]
            Z[indice] = resultado[2]
            indice += 1
        # Creamos una figura en 3D
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                             cmap=cm.coolwarm, linewidth=0,
                             antialiased=False)
        plt.draw()
        plt.pause(0.1)

    X_cp = X.copy()
    Y_cp = Y.copy()
    Z_cp = Z.copy()

    for i in range(grados_y):
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Función tipo sólido")
        # Establecemos las coordenadas del sólido
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        indice = 0
        for datos in zip(X, Y, Z):
            coordenadas_funcion = np.array([datos[0], datos[1], datos[2]])
            rotacion = matriz_rotacion(i, "y")

            resultado = rotacion @ coordenadas_funcion
            X[indice] = resultado[0]
            Y[indice] = resultado[1]
            Z[indice] = resultado[2]
            indice += 1
        # Creamos una figura en 3D
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                             cmap=cm.coolwarm, linewidth=0,
                             antialiased=False)
        plt.draw()
        plt.pause(0.1)
    X_cp = X.copy()
    Y_cp = Y.copy()
    Z_cp = Z.copy()
    for i in range(grados_z):
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Función tipo sólido")
        # Establecemos las coordenadas del sólido
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        indice = 0
        for datos in zip(X, Y, Z):
            coordenadas_funcion = np.array([datos[0], datos[1], datos[2]])
            rotacion = matriz_rotacion(i, "z")

            resultado = rotacion @ coordenadas_funcion
            X[indice] = resultado[0]
            Y[indice] = resultado[1]
            Z[indice] = resultado[2]
            indice += 1
        # Creamos una figura en 3D
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1,
                             cmap=cm.coolwarm, linewidth=0,
                             antialiased=False)
        plt.draw()
        plt.pause(0.1)


# Definimos una gráfica
figura = plt.figure()
# Configuramos la perspectiva en 3D
grafica = figura.add_subplot(projection="3d")
configuracion_grafica(-10, 10, -10, 10, -10, 10, "Función tipo sólido")
animacion_funcion_3D(45, 45, 45)
plt.show()
