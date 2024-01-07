# Generamos el inicializador
import matplotlib.pyplot as plt
import numpy as np


class cinematica:
    def __init__(self):
        self.figura = plt.figure()
        self.grafica = self.figura.add_subplot(projection="3d")

        # Definimos una funcion

    def configuracion_grafica(self, x_lim_inf, x_lim_sup, y_lim_inf, y_lim_sup, z_lim_inf, z_lim_sup, titulo):
        self.grafica.set_title(titulo)
        self.grafica.set_xlim(x_lim_inf, x_lim_sup)
        self.grafica.set_ylim(y_lim_inf, y_lim_sup)
        self.grafica.set_zlim(z_lim_inf, z_lim_sup)
        self.grafica.set_xlabel("x")
        self.grafica.set_ylabel("y")
        self.grafica.set_zlabel("z")

    def matriz_rotacion_z(self, grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[np.cos(rad), -np.sin(rad), 0, 0],
                             [np.sin(rad), np.cos(rad), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        return rotacion

    def matriz_rotacion_y(self, grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[np.cos(rad), 0, -np.sin(rad), 0],
                             [0, 1, 0, 0],
                             [np.sin(rad), 0, np.cos(rad), 0],
                             [0, 0, 0, 1]])
        return rotacion

    def matriz_rotacion_x(self, grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[1, 0, 0, 0],
                             [0, np.cos(rad), -np.sin(rad), 0],
                             [0, np.sin(rad), np.cos(rad), 0],
                             [0, 0, 0, 1]])
        return rotacion

    def matriz_traslacion_x(self, x):
        traslacion = np.array([[1, 0, 0, x],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        return traslacion

    def matriz_traslacion_y(self, y):
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, y],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        return traslacion

    def matriz_traslacion_z(self, z):
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, z],
                               [0, 0, 0, 1]])
        return traslacion

    def sistema_coordenadas_movil(self, matriz_rotacion):
        mr_11 = matriz_rotacion[0, 0]
        mr_12 = matriz_rotacion[1, 0]
        mr_13 = matriz_rotacion[2, 0]
        mr_21 = matriz_rotacion[0, 1]
        mr_22 = matriz_rotacion[1, 1]
        mr_23 = matriz_rotacion[2, 1]
        mr_31 = matriz_rotacion[0, 2]
        mr_32 = matriz_rotacion[1, 2]
        mr_33 = matriz_rotacion[2, 2]

        dx = matriz_rotacion[0, 3]
        dy = matriz_rotacion[1, 3]
        dz = matriz_rotacion[2, 3]

        self.grafica.plot3D([dx, dx + mr_11], [dy, dy + mr_12], [dz, dz + mr_13], color="purple")
        self.grafica.plot3D([dx, dx + mr_21], [dy, dy + mr_22], [dz, dz + mr_23], color="gray")
        self.grafica.plot3D([dx, dx + mr_31], [dy, dy + mr_32], [dz, dz + mr_33], color="cyan")

    def denavit_hatemberg(self, theta_i, d_i, a_i, alpha_i):
        # Matriz de transformación homógenea
        MTH = self.matriz_rotacion_z(theta_i) @ self.matriz_traslacion_z(d_i) @ self.matriz_traslacion_x(
            a_i) @ self.matriz_rotacion_x(alpha_i)
        return MTH

    def robot_RR(self, theta_1, d_1, a_1, alpha_1, theta_2, d_2, a_2, alpha_2):
        A0 = np.eye(4)  # nos da una matriz identidad de 4x4
        A_0_1 = self.denavit_hatemberg(theta_1, d_1, a_1, alpha_1)
        A_1_2 = self.denavit_hatemberg(theta_2, d_2, a_2, alpha_2)

        A_0_2 = A_0_1 @ A_1_2  # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2

        self.sistema_coordenadas_movil(A0)
        self.sistema_coordenadas_movil(A_0_1)
        self.sistema_coordenadas_movil(A_0_2)

        self.grafica.plot3D([A0[2, 3], A_0_1[2, 3]], [A0[0, 3], A_0_1[0, 3]], [A0[1, 3], A_0_1[1, 3]], color="blue")
        self.grafica.plot3D([A_0_1[2, 3], A_0_2[2, 3]], [A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]],
                            color="blue")

        return A_0_2
