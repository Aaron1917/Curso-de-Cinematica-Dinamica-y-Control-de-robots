# Simulacion del movimiento de una función en 3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# Funciones de configuracion:
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


# Matrices de traslacion y rotacion
def matriz_traslacion(modulo, direccion):
    traslacion = np.zeros((4, 4))
    if direccion == "x":
        traslacion = np.array([[1, 0, 0, modulo],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
    elif direccion == "y":
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, modulo],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
    elif direccion == "z":
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, modulo],
                               [0, 0, 0, 1]])
    return traslacion


def matriz_rotacion(angulo, direccion):
    # Cambiamos el angulo de rotacion a radianes
    rad = angulo / 180 * np.pi
    # Dependiendo de la direccion de rotacion, definimos la matriz de rotación
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


def animacion_3D_rotacion(grados_x, grados_y, grados_z):
    X = Y = Z = np.zeros(40)
    for i in range(grados_x):
        i += 1
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
        i += 1
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
        i += 1
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


def animacion_3d_traslacion(x, y, z):
    n_x = n_y = n_z = 1
    X = Y = Z = np.zeros(40)
    if x < 0:
        x = x * -1
        n_x = -1
    if y < 0:
        y = y * -1
        n_y = -1
    if z < 0:
        z = z * -1
        n_z = -1
    for i in range(x):
        i = (i + 1) * n_x
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Funcion tipo sólido para traslacion")
        # Dibujando la grafica
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)

        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)
        W = np.ones(len(Z))  # Contruccion de vector de unos para agregarlos a las coordenadas
        index = 0

        for dato in zip(X, Y, Z, W):
            coordenadas_funcion = np.array([dato[0], dato[1], dato[2], dato[3]], dtype=object)
            traslacion_x = matriz_traslacion(i, 'x')
            resultado = traslacion_x @ coordenadas_funcion

            X[index] = resultado[0]
            Y[index] = resultado[1]
            Z[index] = resultado[2]
            index += 1
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        plt.draw()
        plt.pause(0.01)
    X_cp = X.copy()
    Y_cp = Y.copy()
    Z_cp = Z.copy()

    for j in range(y):
        j = (j + 1) * n_y
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Funcion tipo sólido para traslacion")
        # Dibujando la grafica
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        W = np.ones(len(Z))  # Contruccion de vector de unos para agregarlos a las coordenadas
        index = 0
        for dato in zip(X, Y, Z, W):
            coordenadas_funcion = np.array([dato[0], dato[1], dato[2], dato[3]], dtype=object)
            traslacion_y = matriz_traslacion(j, 'y')
            resultado = traslacion_y @ coordenadas_funcion

            X[index] = resultado[0]
            Y[index] = resultado[1]
            Z[index] = resultado[2]
            index += 1
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        plt.draw()
        plt.pause(0.01)

    X_cp = X.copy()
    Y_cp = Y.copy()
    Z_cp = Z.copy()
    for k in range(z):
        k = (k + 1) * n_z
        grafica.cla()
        configuracion_grafica(-10, 10, -10, 10, -10, 10, "Funcion tipo sólido para traslacion")
        # Dibujando la grafica
        X = X_cp.copy()
        Y = Y_cp.copy()
        Z = Z_cp.copy()
        W = np.ones(len(Z))  # Contruccion de vector de unos para agregarlos a las coordenadas
        index = 0
        for dato in zip(X, Y, Z, W):
            coordenadas_funcion = np.array([dato[0], dato[1], dato[2], dato[3]], dtype=object)
            traslacion_z = matriz_traslacion(k, 'z')
            resultado = traslacion_z @ coordenadas_funcion

            X[index] = resultado[0]
            Y[index] = resultado[1]
            Z[index] = resultado[2]
            index += 1
        grafica.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        plt.draw()
        plt.pause(0.01)


# Definimos una gráfica
figura = plt.figure()
# Configuramos la perspectiva en 3D
grafica = figura.add_subplot(projection="3d")
configuracion_grafica(-10, 10, -10, 10, -10, 10, "Función tipo sólido")
# animacion_3D_rotacion(45, 45, 45)
animacion_3d_traslacion(-10, -5, -10)
plt.show()
