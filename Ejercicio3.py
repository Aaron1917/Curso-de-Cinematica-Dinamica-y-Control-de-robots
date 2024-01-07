import numpy as np  # Importamos las librerías
import matplotlib.pyplot as plt


# Declaramos las funciones para obtener las matrices de rotación


def matriz_rotacion_x(grados):
    # Función para obtener la matriz de rotación sobre el eje X a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = (np.pi / 180) * grados        # Tranformamos a radianes
    # Declaramos la matriz de rotacion para el eje x
    rotacion = np.array([[1, 0, 0],
                         [0, np.cos(rad), -np.sin(rad)],
                         [0, np.sin(rad), np.cos(rad)]])
    return rotacion     # Retornamos la matriz resultante


def matriz_rotacion_y(grados):
    # Función para obtener la matriz de rotación sobre el eje Y a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = grados / 180 * np.pi      # Tranformamos a radianes
    # Declaramos la matriz de rotacion para el eje x
    rotacion = np.array([[np.cos(rad), 0, np.sin(rad)],
                         [0, 1, 0],
                         [-np.sin(rad), 0, np.cos(rad)]])
    return rotacion     # Retornamos la matriz resultante


def matriz_rotacion_z(grados):
    # Función para obtener la matriz de rotación sobre el eje Z a un ángulo dado
    # Acepta solo ángulos positivos en grados
    rad = grados / 180 * np.pi      # Tranformamos a radianes
    # Declaramos la matriz de rotacion para el eje x
    rotacion = np.array([[np.cos(rad), -np.sin(rad), 0],
                         [np.sin(rad), np.cos(rad), 0],
                         [0, 0, 1]])
    return rotacion     # Retornamos la matriz resultante


def configuracion_grafica():
    plt.title("Matrices de rotación")
    grafica.set_xlim(-3, 3)     # Establecemos el límite en el eje X
    grafica.set_ylim(-3, 3)     # Establecemos el límite en el eje Y
    grafica.set_zlim(-3, 3)     # Establecemos el límite en el eje Z
    grafica.set_xlabel("x")     # Establecemos la etiqueta en el eje X
    grafica.set_ylabel("y")     # Establecemos la etiqueta en el eje Y
    grafica.set_zlabel("z")     # Establecemos la etiqueta en el eje Z


def linea_movil(matriz_rotacion, linea_):
    # Guardamos el parámetro correspondiente a su fila y columna
    mr_11 = matriz_rotacion[0, 0]
    mr_12 = matriz_rotacion[1, 0]
    mr_13 = matriz_rotacion[2, 0]
    mr_21 = matriz_rotacion[0, 1]
    mr_22 = matriz_rotacion[1, 1]
    mr_23 = matriz_rotacion[2, 1]
    mr_31 = matriz_rotacion[0, 2]
    mr_32 = matriz_rotacion[1, 2]
    mr_33 = matriz_rotacion[2, 2]
    # Guardamos el punto de origen de la linea
    ori_x = linea_[0, 0]
    ori_y = linea_[1, 0]
    ori_z = linea_[2, 0]
    # Obtenemos el módulo de la línea en cada uno de los ejes
    l_x = linea_[0, 1]
    l_y = linea_[1, 1]
    l_z = linea_[2, 1]
    # Obtenemos los 3 nuevos puntos despúes de ejecutar la rotación
    p_x1 = (mr_11 * ori_x) + (mr_12 * ori_y) + (mr_13 * ori_z)
    p_y1 = (mr_21 * ori_x) + (mr_22 * ori_y) + (mr_23 * ori_z)
    p_z1 = (mr_31 * ori_x) + (mr_32 * ori_y) + (mr_33 * ori_z)
    p_x2 = (mr_11 * l_x) + (mr_12 * l_y) + (mr_13 * l_z)
    p_y2 = (mr_21 * l_x) + (mr_22 * l_y) + (mr_23 * l_z)
    p_z2 = (mr_31 * l_x) + (mr_32 * l_y) + (mr_33 * l_z)
    # Obtenemos los parametros de nuestra nueva linea.
    new_linea = np.array([[p_x1, p_x2],
                          [p_y1, p_y2],
                          [p_z1, p_z2]])
    # Graficamos la linea obtenida
    grafica.plot3D(new_linea[0], new_linea[1], new_linea[2], color="purple")
    return new_linea        # retornamos la linea obtenida


def animacion_rotacion(ang_x, ang_y, ang_z, linea_):
    # Función para rotar una linea cualquiera en torno al eje X, Y, Z consecutivamente
    # Seccuencia para X
    linea_o = linea_    # Guardamos el valor de la linea original
    for i in range(ang_x):
        grafica.cla()
        configuracion_grafica()  # Llamamos la funcion configura gráfica
        MR_x = matriz_rotacion_x(i)     # Obtenemos la matriz de rotación
        linea_movil(MR_x, linea_)   # llamamos a la función para crear la linea
        # Graficamos la linea original
        grafica.plot3D(linea_o[0], linea_o[1], linea_o[2], color="black")
        plt.draw()      # dibujamos las gráficas
        plt.pause(0.01)     # colocamos un delay
    # Obtenemos la línea final de X
    linea_ = linea_movil(matriz_rotacion_x(ang_x), linea_)
    linea_x = linea_
    # Seccuencia para Y
    for j in range(ang_y):
        grafica.cla()
        configuracion_grafica()  # Llamamos la función configura gráfica
        MR_y = matriz_rotacion_y(j)     # Obtenemos la matriz de rotación
        linea_movil(MR_y, linea_)   # llamamos a la función para crear la linea
        # Graficamos la linea original y el final de la rotación en X
        grafica.plot3D(linea_o[0], linea_o[1], linea_o[2], color="black")
        grafica.plot3D(linea_x[0], linea_x[1], linea_x[2], color="blue")
        plt.draw()      # dibujamos las gráficas
        plt.pause(0.01)     # colocamos un delay
    # Obtenemos la línea final de Y
    linea_ = linea_movil(matriz_rotacion_y(ang_y), linea_)
    linea_y = linea_
    # Seccuencia para Z
    for k in range(ang_z):
        grafica.cla()
        configuracion_grafica()  # Llamamos la función configura gráfica
        MR_z = matriz_rotacion_z(k)     # Obtenemos la matriz de rotación
        linea_movil(MR_z, linea_)   # llamamos a la función para crear la linea
        # Graficamos la linea original y el final de la rotación en X & Y
        grafica.plot3D(linea_o[0], linea_o[1], linea_o[2], color="black")
        grafica.plot3D(linea_x[0], linea_x[1], linea_x[2], color="blue")
        grafica.plot3D(linea_y[0], linea_y[1], linea_y[2], color="green")
        plt.draw()      # dibujamos las gráficas
        plt.pause(0.01)     # colocamos un delay
    # Obtenemos la línea final de Z
    linea_ = linea_movil(matriz_rotacion_z(ang_z), linea_)
    return linea_       # Retornamos la linea final


# Declaramos la linea a rotar
linea = np.array([[0.0, 2.0],
                  [0.0, 2.1],
                  [0.0, 1.8]])

figura, grafica = plt.subplots()  # Definimos una gráfica
grafica = plt.axes(projection="3d")  # Configuramos la perspectiva 3D
# Llamamos a la función para animar la línea
linea = animacion_rotacion(90, 90, 90, linea)
# Imprimimos los valores de la linea
print(linea)
plt.show()      # Mostramos la gráfica
