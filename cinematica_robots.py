# Generamos el inicializador
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


# from matplotlib import cm


class cinematica:
    def __init__(self):
        self.figura = plt.figure()
        self.grafica = self.figura.add_subplot(projection="3d")

    # Simulación de el movimiento de una función en 3 dimensiones
    # Definimos una función

    def configuracion_grafica_z(self, z_lim_inf, z_lim_sup, x_lim_inf, x_lim_sup, y_lim_inf, y_lim_sup, titulo):
        self.grafica.set_title(titulo)
        self.grafica.set_xlim(z_lim_inf, z_lim_sup)
        self.grafica.set_ylim(x_lim_inf, x_lim_sup)
        self.grafica.set_zlim(y_lim_inf, y_lim_sup)
        self.grafica.set_xlabel("z")
        self.grafica.set_ylabel("x")
        self.grafica.set_zlabel("y")

    def configuracion_grafica_x(self, x_lim_inf, x_lim_sup, y_lim_inf, y_lim_sup, z_lim_inf, z_lim_sup, titulo):
        self.grafica.set_title(titulo)
        self.grafica.set_xlim(x_lim_inf, x_lim_sup)
        self.grafica.set_ylim(y_lim_inf, y_lim_sup)
        self.grafica.set_zlim(z_lim_inf, z_lim_sup)
        self.grafica.set_xlabel("x")
        self.grafica.set_ylabel("y")
        self.grafica.set_zlabel("z")
        # self.grafica.view_init(elev=25, azim=30)

    def sistema_coordenadas(self, x_i, y_i, z_i, x_f, y_f, z_f):
        x = [x_i, x_f]
        y = [y_i, y_f]
        z = [z_i, z_f]
        self.grafica.plot3D(x, [y_i, y_i], [z_i, z_i], color="red")
        self.grafica.plot3D([x_i, x_i], y, [z_i, z_i], color="green")
        self.grafica.plot3D([x_i, x_i], [y_i, y_i], z, color="blue")

    @staticmethod
    def matriz_rotacion_z(grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[np.cos(rad), -np.sin(rad), 0, 0],
                             [np.sin(rad), np.cos(rad), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
        return rotacion

    @staticmethod
    def matriz_rotacion_y(grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[np.cos(rad), 0, -np.sin(rad), 0],
                             [0, 1, 0, 0],
                             [np.sin(rad), 0, np.cos(rad), 0],
                             [0, 0, 0, 1]])
        return rotacion

    @staticmethod
    def matriz_rotacion_x(grados):
        rad = grados / 180 * np.pi
        rotacion = np.array([[1, 0, 0, 0],
                             [0, np.cos(rad), -np.sin(rad), 0],
                             [0, np.sin(rad), np.cos(rad), 0],
                             [0, 0, 0, 1]])
        return rotacion

    @staticmethod
    def matriz_traslacion_x(x):
        traslacion = np.array([[1, 0, 0, x],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        return traslacion

    @staticmethod
    def matriz_traslacion_y(y):
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, y],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
        return traslacion

    @staticmethod
    def matriz_traslacion_z(z):
        traslacion = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, z],
                               [0, 0, 0, 1]])
        return traslacion

    def sistema_coordenadas_movil_z(self, matriz_rotacion, escala = 1):
        mr_11 = matriz_rotacion[0, 0]
        mr_12 = matriz_rotacion[1, 0]
        mr_13 = matriz_rotacion[2, 0]
        mr_21 = matriz_rotacion[0, 1]
        mr_22 = matriz_rotacion[1, 1]
        mr_23 = matriz_rotacion[2, 1]
        mr_31 = matriz_rotacion[0, 2]
        mr_32 = matriz_rotacion[1, 2]
        mr_33 = matriz_rotacion[2, 2]

        dx = matriz_rotacion[1, 3]
        dy = matriz_rotacion[2, 3]
        dz = matriz_rotacion[0, 3]

        self.grafica.plot3D([dy, dy + mr_13 * escala], [dz, dz + mr_11 * escala], [dx, dx + mr_12 * escala],
                            color="g")  # purple
        self.grafica.plot3D([dy, dy + mr_23 * escala], [dz, dz + mr_21 * escala], [dx, dx + mr_22 * escala],
                            color="b")
        self.grafica.plot3D([dy, dy + mr_33 * escala], [dz, dz + mr_31 * escala], [dx, dx + mr_32 * escala],
                            color="r")


    def sistema_coordenadas_movil_x(self, matriz_rotacion, escala = 1):
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

        self.grafica.plot3D([dx, dx + mr_11 * escala], [dy, dy + mr_12 * escala], [dz, dz + mr_13 * escala],
                            color="r")
        self.grafica.plot3D([dx, dx + mr_21 * escala], [dy, dy + mr_22 * escala], [dz, dz + mr_23 * escala],
                            color="g")
        self.grafica.plot3D([dx, dx + mr_31 * escala], [dy, dy + mr_32 * escala], [dz, dz + mr_33 * escala],
                            color="b")

    def denavit_hatemberg(self, theta_i, d_i, a_i, alpha_i):
        # Matriz de transformacion homogenea
        MTH = self.matriz_rotacion_z(theta_i) @ self.matriz_traslacion_z(d_i) @ self.matriz_traslacion_x(a_i) @ self.matriz_rotacion_x(alpha_i)
        return MTH

    def drawCube(self, matrizTH, side_length = 0.5, faceColor=None, aristColor=None):
        x = matrizTH[0, 3]
        y = matrizTH[1, 3]
        z = matrizTH[2, 3]
        # dibuja aristas alrrededor de un punto dada una longitud
        vertices = [
            [x - side_length / 2, y - side_length / 2, z - side_length / 2],
            [x + side_length / 2, y - side_length / 2, z - side_length / 2],
            [x + side_length / 2, y + side_length / 2, z - side_length / 2],
            [x - side_length / 2, y + side_length / 2, z - side_length / 2],
            [x - side_length / 2, y - side_length / 2, z + side_length / 2],
            [x + side_length / 2, y - side_length / 2, z + side_length / 2],
            [x + side_length / 2, y + side_length / 2, z + side_length / 2],
            [x - side_length / 2, y + side_length / 2, z + side_length / 2]
        ]
        # Define las cara del cubo
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[3], vertices[7], vertices[4]]
        ]
        self.grafica.add_collection3d(Poly3DCollection(faces, linewidths=1, edgecolors=aristColor, facecolors=faceColor, alpha=0.1))
        self.grafica.scatter(x, y, z, color='b', s=5)  # Punto central
        # self.grafica.set_xlabel('X')
        # self.grafica.set_ylabel('Y')
        # self.grafica.set_zlabel('Z')
        # self.grafica.set_title('Cubo alrededor del punto')

    def drawPrisma(self, matrizTH, sides = (0.5, 0.5, 0.5), offset = (0.0, 0.0, 0.0), color=None):
        x = matrizTH[0, 3] + offset[0]
        y = matrizTH[1, 3] + offset[1]
        z = matrizTH[2, 3] + offset[2]
        side_x = sides[0]
        side_y = sides[1]
        side_z = sides[2]
        # dibuja aristas alrrededor de un punto dada una longitud
        vertices = [
            [x - side_x / 2, y - side_y / 2, z - side_z / 2],
            [x + side_x / 2, y - side_y / 2, z - side_z / 2],
            [x + side_x / 2, y + side_y / 2, z - side_z / 2],
            [x - side_x / 2, y + side_y / 2, z - side_z / 2],
            [x - side_x / 2, y - side_y / 2, z + side_z / 2],
            [x + side_x / 2, y - side_y / 2, z + side_z / 2],
            [x + side_x / 2, y + side_y / 2, z + side_z / 2],
            [x - side_x / 2, y + side_y / 2, z + side_z / 2]
        ]
        # Define las cara del cubo
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[3], vertices[7], vertices[4]]
        ]
        self.grafica.add_collection3d(Poly3DCollection(faces, linewidths=1, edgecolors=color , alpha=0.1))
        #self.grafica.scatter(x, y, z, color='b', s=5)  # Punto central
        # self.grafica.set_xlabel('X')
        # self.grafica.set_ylabel('Y')
        # self.grafica.set_zlabel('Z')
        # self.grafica.set_title('Cubo alrededor del punto')

    def robot_IRB2600(self, theta):
        scl = 100
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(theta[0], 280, 0, -90)
        A_0_0 = self.matriz_traslacion_x(150)@self.matriz_rotacion_y(90)
        A_1_2 = self.denavit_hatemberg(theta[1]-90, 0, 815, 0)
        A_2_3 = self.denavit_hatemberg(theta[2], 0, 0, 90)
        A_3_4 = self.denavit_hatemberg(theta[3], 795, 0, -90)
        A_4_5 = self.denavit_hatemberg(theta[4], 0, 0, 90)
        A_5_6 = self.denavit_hatemberg(theta[5], 85, 0, 0)

        A_0_1_0 = A_0_1 @ A_0_0
        A_0_2 = A_0_1_0 @ A_1_2
        A_0_3 = A_0_2 @ A_2_3
        A_0_4 = A_0_3 @ A_3_4
        A_0_5 = A_0_4 @ A_4_5
        A_0_6 = A_0_5 @ A_5_6

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_1_0[0, 3]], [A_0_1[1, 3], A_0_1_0[1, 3]], [A_0_1[2, 3], A_0_1_0[2, 3]],
                            color="blue")

        self.grafica.plot3D([A_0_1_0[0, 3], A_0_2[0, 3]], [A_0_1_0[1, 3], A_0_2[1, 3]], [A_0_1_0[2, 3], A_0_2[2, 3]],
                            color="blue")

        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
                            color="blue")

        self.sistema_coordenadas_movil_x(A_0, scl)
        self.sistema_coordenadas_movil_x(A_0_1_0, scl)
        self.sistema_coordenadas_movil_x(A_0_1, scl)
        self.sistema_coordenadas_movil_x(A_0_2, scl)
        self.sistema_coordenadas_movil_x(A_0_3, scl)
        self.sistema_coordenadas_movil_x(A_0_4, scl)
        self.sistema_coordenadas_movil_x(A_0_5, scl)
        self.sistema_coordenadas_movil_x(A_0_6, scl)

        return A_0_6

    def robot_IRB2600_inicial(self, theta):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(theta[0], 280, 0, -90)
        A_0_0 = self.matriz_traslacion_x(150)@self.matriz_rotacion_y(90)
        A_1_2 = self.denavit_hatemberg(theta[1]-90, 0, 815, 0)
        A_2_3 = self.denavit_hatemberg(theta[2], 0, 0, 90)
        A_3_4 = self.denavit_hatemberg(theta[3], 795, 0, -90)
        A_4_5 = self.denavit_hatemberg(theta[4], 0, 0, 90)
        A_5_6 = self.denavit_hatemberg(theta[5], 85, 0, 0)

        A_0_1_0 = A_0_1 @ A_0_0
        A_0_2 = A_0_1_0 @ A_1_2
        A_0_3 = A_0_2 @ A_2_3
        A_0_4 = A_0_3 @ A_3_4
        A_0_5 = A_0_4 @ A_4_5
        A_0_6 = A_0_5 @ A_5_6

        return A_0_6


    def robot_RR(self, theta_1, d_1, a_1, alpha_1, theta_2, d_2, a_2, alpha_2):
        A0 = np.eye(4)  # nos da una matriz identidad de 4x4
        A_0_1 = self.denavit_hatemberg(theta_1, d_1, a_1, alpha_1)
        A_1_2 = self.denavit_hatemberg(theta_2, d_2, a_2, alpha_2)

        A_0_2 = A_0_1 @ A_1_2  # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2

        self.sistema_coordenadas_movil_z(A0)
        self.sistema_coordenadas_movil_z(A_0_1)
        self.sistema_coordenadas_movil_z(A_0_2)

        self.grafica.plot3D([A0[2, 3], A_0_1[2, 3]], [A0[0, 3], A_0_1[0, 3]], [A0[1, 3], A_0_1[1, 3]], color="blue")
        self.grafica.plot3D([A_0_1[2, 3], A_0_2[2, 3]], [A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]],
                            color="blue")

        return A_0_2

    def robot_1(self, param1, param2, param3, param4):
        A0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_1_21 = self.denavit_hatemberg(param2[0], param2[1], 0, 0)
        A_1_22 = self.denavit_hatemberg(0, 0, param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_21 = A_0_1 @ A_1_21
        A_0_22 = A_0_1 @ A_1_21 @ A_1_22
        # A_1_3 = A_1_2 @ A_2_3
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4

        self.sistema_coordenadas_movil_x(A0)
        self.sistema_coordenadas_movil_x(A_0_1)
        # self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_21)
        self.sistema_coordenadas_movil_x(A_0_22)
        self.sistema_coordenadas_movil_x(A_0_3)
        self.sistema_coordenadas_movil_x(A_0_4)

        self.grafica.plot3D([A0[0, 3], A_0_1[0, 3]], [A0[1, 3], A_0_1[1, 3]], [A0[2, 3], A_0_1[2, 3]], color="blue")
        # self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
        #                     color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_21[0, 3]], [A_0_1[1, 3], A_0_21[1, 3]], [A_0_1[2, 3], A_0_21[2, 3]],
                             color="blue")
        self.grafica.plot3D([A_0_21[0, 3], A_0_22[0, 3]], [A_0_21[1, 3], A_0_22[1, 3]], [A_0_21[2, 3], A_0_22[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
        #                     color="blue")
        return A_0_3

    def robot_2(self, param1, param2, printLinks=True, printAxes= True):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])

        A_0_2 = A_0_1 @ A_1_2

        if printLinks:
            self.grafica.plot3D([A_0[2, 3], A_0_1[2, 3]], [A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], color="blue")
            self.grafica.plot3D([A_0_1[2, 3], A_0_2[2, 3]], [A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]],
                                color="blue")
        if printAxes:
            self.sistema_coordenadas_movil_z(A_0)
            self.sistema_coordenadas_movil_z(A_0_1)
            self.sistema_coordenadas_movil_z(A_0_2)
        return A_0_2


    def robot_4(self, param1, param2, param3, param4):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        self.sistema_coordenadas_movil_x(A_0_4)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        return A_0_4

    def robot_5(self, param1, param2, param3):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        #A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        # A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4

        self.sistema_coordenadas_movil_z(A_0)
        self.sistema_coordenadas_movil_z(A_0_1)
        self.sistema_coordenadas_movil_z(A_0_2)
        self.sistema_coordenadas_movil_z(A_0_3)
        #self.sistema_coordenadas_movil_z(A_0_4)

        self.grafica.plot3D([A_0[2, 3], A_0_1[2, 3]], [A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[2, 3], A_0_2[2, 3]], [A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[2, 3], A_0_3[2, 3]], [A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_3[2, 3], A_0_4[2, 3]], [A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]],
        #                     color="blue")

        return A_0_3

    def robot_6(self, param1, param2, param3, param4, param5):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5

        # self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        self.sistema_coordenadas_movil_x(A_0_4)
        self.sistema_coordenadas_movil_x(A_0_5)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        return A_0_5

    def robot_7(self, param1, param2, param3, param4, param5, param6, param7, param8):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])
        A_5_6 = self.denavit_hatemberg(param6[0], param6[1], param6[2], param6[3])
        A_6_7 = self.denavit_hatemberg(param7[0], param7[1], param7[2], param7[3])
        A_7_8 = self.denavit_hatemberg(param8[0], param8[1], param8[2], param8[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5
        A_0_6 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6
        A_0_7 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6 @ A_6_7
        A_0_8 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6 @ A_6_7 @ A_7_8

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        # self.sistema_coordenadas_movil_x(A_0_4)
        self.sistema_coordenadas_movil_x(A_0_5)
        self.sistema_coordenadas_movil_x(A_0_6)
        self.sistema_coordenadas_movil_x(A_0_7)
        self.sistema_coordenadas_movil_x(A_0_8)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_6[0, 3], A_0_7[0, 3]], [A_0_6[1, 3], A_0_7[1, 3]], [A_0_6[2, 3], A_0_7[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_7[0, 3], A_0_8[0, 3]], [A_0_7[1, 3], A_0_8[1, 3]], [A_0_7[2, 3], A_0_8[2, 3]],
                            color="blue")
        return A_0_8

    def robot_8(self, param1, param2, param3, param4, param5):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])
        # A_5_6 = self.denavit_hatemberg(param6[0], param6[1], param6[2], param6[3])

        # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2
        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5
        # A_0_6 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        self.sistema_coordenadas_movil_x(A_0_4)
        self.sistema_coordenadas_movil_x(A_0_5)
        # self.sistema_coordenadas_movil_x(A_0_6)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
        #                     color="blue")
        return A_0_5

    def robot_9(self, param1, param2, param3, param4, param5):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])
        #A_5_6 = self.denavit_hatemberg(param6[0], param6[1], param6[2], param6[3])

        # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2
        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5
        # A_0_6 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        # self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        # self.sistema_coordenadas_movil_x(A_0_4)
        self.sistema_coordenadas_movil_x(A_0_5)
        # self.sistema_coordenadas_movil_x(A_0_6)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
        #                     color="blue")
        return A_0_5

    def robot_10(self, param1, param2, param3, param4):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        # A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])
        # A_5_6 = self.denavit_hatemberg(param6[0], param6[1], param6[2], param6[3])

        # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2
        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        # A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5
        # A_0_6 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        self.sistema_coordenadas_movil_x(A_0_4)
        # self.sistema_coordenadas_movil_x(A_0_5)
        # self.sistema_coordenadas_movil_x(A_0_6)

        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
        #                     color="blue")
        # self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
        #                     color="blue")
        return A_0_4

    def robot_11(self, param1, param2, param3, param4, param5):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])
        A_3_4 = self.denavit_hatemberg(param4[0], param4[1], param4[2], param4[3])
        A_4_5 = self.denavit_hatemberg(param5[0], param5[1], param5[2], param5[3])
        # A_5_6 = self.denavit_hatemberg(param6[0], param6[1], param6[2], param6[3])

        # matriz que relaciona el sistema de coordenadas 0 con el sistema de coordenadas 2
        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3
        A_0_4 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4
        A_0_5 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5
        # A_0_6 = A_0_1 @ A_1_2 @ A_2_3 @ A_3_4 @ A_4_5 @ A_5_6


        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        # self.grafica.plot3D([A_0_5[0, 3], A_0_6[0, 3]], [A_0_5[1, 3], A_0_6[1, 3]], [A_0_5[2, 3], A_0_6[2, 3]],
        #                     color="blue")

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        # self.sistema_coordenadas_movil_x(A_0_4)
        self.sistema_coordenadas_movil_x(A_0_5)
        # self.sistema_coordenadas_movil_x(A_0_6)

        return A_0_5

    def robot_cartesiano(self, param1, param2, param3):
        A_0 = np.eye(4)
        A_0_1 = self.denavit_hatemberg(param1[0], param1[1], param1[2], param1[3])
        A_1_2 = self.denavit_hatemberg(param2[0], param2[1], param2[2], param2[3])
        A_2_3 = self.denavit_hatemberg(param3[0], param3[1], param3[2], param3[3])

        A_0_2 = A_0_1 @ A_1_2
        A_0_3 = A_0_1 @ A_1_2 @ A_2_3

        self.sistema_coordenadas_movil_x(A_0)
        self.sistema_coordenadas_movil_x(A_0_1)
        self.sistema_coordenadas_movil_x(A_0_2)
        self.sistema_coordenadas_movil_x(A_0_3)
        # self.sistema_coordenadas_movil_x(A_0_4)
        # self.sistema_coordenadas_movil_x(A_0_5)
        self.drawCube(A_0_1, 1)
        self.drawCube(A_0_2, 1)
        self.drawCube(A_0_3, 1)
        self.drawPrisma(A_0, (7.5, 0.5, 0.5), (7.5 / 2, 0, 0), color='k')
        self.drawPrisma(A_0, (7.5, 0.5, 0.5), (7.5 / 2, 6, 0), color='k')
        self.drawPrisma(A_0_1, (0.5, 0.5, 6.0), (0.0, 0.0, 3.0), color='r')
        self.drawPrisma(A_0_1, (0.5, 0.5, 6.0), (0.0, 6.0, 3.0), color='r')
        self.drawPrisma(A_0_1, (0.5, 6.5, 0.5), (0.0, 3.0, 6.0), color='r')#6.25
        self.drawPrisma(A_0_2, (1, 1, .5), (-0.75, 0.0, 0.0), color='g')
        self.drawPrisma(A_0_3, (0.5, 0.5, 5.0), (0.0, 0.0, 2.5), color='b')

        """
        self.grafica.plot3D([A_0[0, 3], A_0_1[0, 3]], [A_0[1, 3], A_0_1[1, 3]], [A_0[2, 3], A_0_1[2, 3]],
                            color="blue", linestyle="--")
        self.grafica.plot3D([A_0_1[0, 3], A_0_2[0, 3]], [A_0_1[1, 3], A_0_2[1, 3]], [A_0_1[2, 3], A_0_2[2, 3]],
                            color="blue", linestyle="--")
        self.grafica.plot3D([A_0_2[0, 3], A_0_3[0, 3]], [A_0_2[1, 3], A_0_3[1, 3]], [A_0_2[2, 3], A_0_3[2, 3]],
                            color="blue", linestyle="--")
        self.grafica.plot3D([A_0_3[0, 3], A_0_4[0, 3]], [A_0_3[1, 3], A_0_4[1, 3]], [A_0_3[2, 3], A_0_4[2, 3]],
                            color="blue")
        self.grafica.plot3D([A_0_4[0, 3], A_0_5[0, 3]], [A_0_4[1, 3], A_0_5[1, 3]], [A_0_4[2, 3], A_0_5[2, 3]],
                            color="blue")
        """
        return A_0_3
