# Jacobiano

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
from cinematica_robots import cinematica


posiciones_iniciales = np.zeros(2)
posiciones_deseadas = np.eye(4)

grafica = cinematica()
grafica.configuracion_grafica_z(-1000, 1000, -1000, 1000, -100, 1000, "Robot Jacobiano")
cinematica.robot_2(grafica, [45, 0, 700, 0], [45, 0, 500, 0])


def jacobians(valor_deseado, posicion_inicial):
    desplazamiento = 0.001
    bandera = True
    Jacobiano = np.zeros([12, 2])
    error = np.ones([12, 1])

    theta_1 = posicion_inicial[0]
    theta_2 = posicion_inicial[1]

    theta_1d = theta_1 + desplazamiento
    theta_2d = theta_2 + desplazamiento

    iteraciones = 0

    while bandera:
        iteraciones += 1
        Matriz_TH = cinematica.robot_2(grafica, [theta_1d, 0, 700, 0], [theta_2d, 0, 500, 0], True, True)
        derivada_TH = Matriz_TH - valor_deseado
        error[0, 0] = derivada_TH[0, 0]
        error[1, 0] = derivada_TH[0, 1]
        error[2, 0] = derivada_TH[0, 2]
        error[3, 0] = derivada_TH[0, 3]
        error[4, 0] = derivada_TH[1, 0]
        error[5, 0] = derivada_TH[1, 1]
        error[6, 0] = derivada_TH[1, 2]
        error[7, 0] = derivada_TH[1, 3]
        error[8, 0] = derivada_TH[2, 0]
        error[9, 0] = derivada_TH[2, 1]
        error[10, 0] = derivada_TH[2, 2]
        error[11, 0] = derivada_TH[2, 3]

        tv1 = [theta_1d, theta_1]
        tv2 = [theta_2, theta_2d]


        for i in range(2):
            TH_NEW = cinematica.robot_2(grafica, [tv1[i], 0, 700, 0], [tv2[i], 0, 500, 0], False, False)
            dp = (TH_NEW - Matriz_TH)/desplazamiento

            Jacobiano[0, i] = dp[0,0]
            Jacobiano[1, i] = dp[0, 1]
            Jacobiano[2, i] = dp[0, 2]
            Jacobiano[3, i] = dp[0, 3]
            Jacobiano[4, i] = dp[1, 0]
            Jacobiano[5, i] = dp[1, 1]
            Jacobiano[6, i] = dp[1, 2]
            Jacobiano[7, i] = dp[1, 3]
            Jacobiano[8, i] = dp[2, 0]
            Jacobiano[9, i] = dp[2, 1]
            Jacobiano[10, i] = dp[2, 2]
            Jacobiano[11, i] = dp[2, 3]

        R = np.linalg.pinv(Jacobiano) @ (-error)
        print(R)
        theta_1 += R[0, 0]
        theta_2 += R[1, 0]

        theta_1 = theta_1 % 360
        theta_2 = theta_2 % 360

        theta_1d = theta_1 + desplazamiento
        theta_2d = theta_2 + desplazamiento

        print(f"El T1: {theta_1}")
        print(f"El T2: {theta_2}")
        if      abs(error[0, 0]) < 0.00001 and \
                abs(error[1, 0]) < 0.00001 and \
                abs(error[2, 0]) < 0.00001 and \
                abs(error[3, 0]) < 0.00001 and \
                abs(error[4, 0]) < 0.00001 and \
                abs(error[5, 0]) < 0.00001 and \
                abs(error[6, 0]) < 0.00001 and \
                abs(error[7, 0]) < 0.00001 and \
                abs(error[8, 0]) < 0.00001 and \
                abs(error[9, 0]) < 0.00001 and \
                abs(error[10, 0]) < 0.00001 and \
                abs(error[11, 0]) < 0.00001:
            bandera = False

        if iteraciones > 100:
            bandera = False
            theta_1 = posicion_inicial[0]
            theta_2 = posicion_inicial[1]

    print(iteraciones)
    print([theta_1, theta_2])
    return [theta_1, theta_2]


def actualizacion_juntas(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_z(-1000, 1000, -1000, 1000, -100, 1000, "Robot 2")
    th1 = sld_theta1.val
    th2 = sld_theta2.val

    Matriz_TH = cinematica.robot_2(grafica, [th1, 0, 700, 0], [th2, 0, 500, 0])
    dibuja_tabla(Matriz_TH)

    plt.draw()
    plt.pause(1e-5)


def calcula(val):
    grafica.configuracion_grafica_z(-1000, 1000, -1000, 1000, -100, 1000, "Robot 2")

    # Matriz_TH = cinematica.robot_2(grafica, [posiciones_iniciales[0], 0, 700, 0], [posiciones_iniciales[1], 0, 500, 0])
    jaco = jacobians(posiciones_deseadas, posiciones_iniciales)

    Matriz_TH = cinematica.robot_2(grafica, [jaco[0], 0, 700, 0], [jaco[1], 0, 500, 0])
    dibuja_tabla(Matriz_TH)


def salvar_final(val):
    x, y = 0, 0
    # while x < 4:
    #     while y < 4:
    #         posiciones_deseadas[x, y] = float(tabla._cells[(x, y)]._text.get_text())
    #         y += 1
    #     y = 0
    #     x += 1
    x = sld_x.val
    y = sld_y.val
    Matriz = cinematica.robot_2(grafica, [posiciones_iniciales[0], 0, 700, 0], [posiciones_iniciales[1], 0, 500, 0])
    posiciones_deseadas = Matriz @ cinematica.matriz_traslacion_x(x) @ cinematica.matriz_traslacion_z(y)
    print(posiciones_deseadas)
    print(posiciones_iniciales)


def salvar_inicio(val):
    posiciones_iniciales[0] = sld_theta1.val
    posiciones_iniciales[1] = sld_theta2.val
    print(posiciones_iniciales)


def dibuja_tabla(Matriz_TH):
    x = 0
    y = 0
    while x < 4:
        while y < 4:
            tabla._cells[(x, y)]._text.set_text(np.round(Matriz_TH[x, y], 3))
            y += 1
        y = 0
        x += 1


ax1 = plt.axes([0.1, 0.1, 0.3, 0.03])
ax2 = plt.axes([0.1, 0.08, 0.3, 0.03])
ax3 = plt.axes([0.1, 0.9, 0.3, 0.03])
ax4 = plt.axes([0.1, 0.88, 0.3, 0.03])
ax_b_init = plt.axes([0.85, 0.9, 0.12, 0.04])
ax_b_end = plt.axes([0.85, 0.84, 0.12, 0.04])
ax_button = plt.axes([0.85, 0.78, 0.12, 0.04])
ax_table = plt.axes([0.58, 0.17, 0.08, 0.03])
# ax_it_text = plt.axes([0.1, 0.1, 0.08, 0.1])

boton = Button(ax_button, "Calcular", image=None, color='0.85', hovercolor='0.95')
binicial = Button(ax_b_init, "Inicio", image=None, color='0.85', hovercolor='0.95')
bfinal = Button(ax_b_end, "Final", image=None, color='0.85', hovercolor='0.95')

sld_theta1 = Slider(ax1, r'$\theta_1$', -180, 180, valinit=0)
sld_theta2 = Slider(ax2, r'$\theta_2$', -180, 180, valinit=0)
sld_x = Slider(ax3, r'$X$', -900, 900, valinit=0)
sld_y = Slider(ax4, r'$Z$', -900, 900, valinit=0)

grafica.configuracion_grafica_z(-1000, 1000, -1000, 1000, -100, 1000, "Robot 2")
posicion_inicial = [45, 45]
valor_inicial = cinematica.robot_2(grafica, [45, 0, 700, 0], [45, 0, 500, 0])
valor_deseado = valor_inicial @ cinematica.matriz_traslacion_y(50)

# print(valor_inicial)
# print(valor_deseado)

posiciones = jacobians(valor_deseado, posicion_inicial)
print(posiciones)

Matriz_TH = cinematica.robot_2(grafica, [posiciones[0], 0, 700, 0], [posiciones[1], 0, 500, 0])
tabla = plt.table(cellText=np.round(Matriz_TH, 3), bbox=[2.6, 0, 2.6, 5], loc='center')

tabla.auto_set_font_size(False)
tabla.set_fontsize(8)
ax_table.axis('off')

boton.on_clicked(calcula)
binicial.on_clicked(salvar_inicio)
bfinal.on_clicked(salvar_final)
sld_theta1.on_changed(actualizacion_juntas)
sld_theta2.on_changed(actualizacion_juntas)

plt.show()
