# Jacbiano
# IRB 2600ID - 15/1.8

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from cinematica_robots import cinematica

grafica = cinematica()
grafica.configuracion_grafica_x(-1000, 1000, -1000, 1000, -10, 1500, "Robot IRB2600")
Matriz_TH = cinematica.robot_IRB2600(grafica, [0, 0, 0, 0, 0, 0])


def jacobians(valor_deseado, posicion_inicial):
    desplazamiento = 0.01
    bandera = True
    Jacobiano = np.zeros([12, 6])
    error = np.ones([12, 1])
    theta_1 = posicion_inicial[0]
    theta_2 = posicion_inicial[1]
    theta_3 = posicion_inicial[2]
    theta_4 = posicion_inicial[3]
    theta_5 = posicion_inicial[4]
    theta_6 = posicion_inicial[5]

    theta_1d = theta_1 + desplazamiento
    theta_2d = theta_2 + desplazamiento
    theta_3d = theta_3 + desplazamiento
    theta_4d = theta_4 + desplazamiento
    theta_5d = theta_5 + desplazamiento
    theta_6d = theta_6 + desplazamiento

    iteraciones = 0
    while bandera:
        iteraciones += 1
        Matriz_TH = cinematica.robot_IRB2600(grafica, [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6])
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
        error[10, 0] = derivada_TH[2, 3]

        tv1 = [theta_1d, theta_1, theta_1, theta_1, theta_1, theta_1]
        tv2 = [theta_2, theta_2d, theta_2, theta_2, theta_2, theta_2]
        tv3 = [theta_3, theta_3, theta_3d, theta_3, theta_3, theta_3]
        tv4 = [theta_4, theta_4, theta_4, theta_4d, theta_4, theta_4]
        tv5 = [theta_5, theta_5, theta_5, theta_5, theta_5d, theta_5]
        tv6 = [theta_6, theta_6, theta_6, theta_6, theta_6, theta_6d]

        for i in range(6):
            TH_NEW = cinematica.robot_IRB2600_inicial(grafica, [tv1[i], tv2[i]], tv3[i], tv4[i], tv5[i], tv6[i])
            dp = (TH_NEW - Matriz_TH)/desplazamiento
            Jacobiano[0,i] = dp[0,0]
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

        R = np.linalg.pinv(Jacobiano)@(-error)
        theta_1 += R[0, 0]
        theta_2 += R[1, 0]
        theta_3 += R[2, 0]
        theta_4 += R[3, 0]
        theta_5 += R[4, 0]
        theta_6 += R[5, 0]

        theta_1 = theta_1 % 360
        theta_2 = theta_2 % 360
        theta_3 = theta_3 % 360
        theta_4 = theta_4 % 360
        theta_5 = theta_5 % 360
        theta_6 = theta_6 % 360

        theta_1d = theta_1 + desplazamiento
        theta_2d = theta_2 + desplazamiento
        theta_3d = theta_3 + desplazamiento
        theta_4d = theta_4 + desplazamiento
        theta_5d = theta_5 + desplazamiento
        theta_6d = theta_6 + desplazamiento

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
            theta_3 = posicion_inicial[2]
            theta_4 = posicion_inicial[3]
            theta_5 = posicion_inicial[4]
            theta_6 = posicion_inicial[5]
    print(iteraciones)
    print([theta_1, theta_2, theta_3, theta_4, theta_5, theta_6])
    return [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6]


def actualizacion_juntas(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_x(-1000, 1000, -1000, 1000, -10, 1500, "Robot IRB2600")
    th1 = sld_theta1.val
    th2 = sld_theta2.val
    th3 = sld_theta3.val
    th4 = sld_theta4.val
    th5 = sld_theta5.val
    th6 = sld_theta6.val

    Matriz_TH = cinematica.robot_IRB2600(grafica, [th1, th2, th3, th4, th5, th6])

    x = 0
    y = 0
    while x < 4:
        while y < 4:
            tabla._cells[(x, y)]._text.set_text(np.round(Matriz_TH[x, y], 3))
            y += 1
        y = 0
        x += 1

    plt.draw()
    plt.pause(1e-5)


ax1 = plt.axes([0.15, 0.1, 0.3, 0.03])
ax2 = plt.axes([0.15, 0.08, 0.3, 0.03])
ax3 = plt.axes([0.15, 0.06, 0.3, 0.03])
ax4 = plt.axes([0.6, 0.1, 0.3, 0.03])
ax5 = plt.axes([0.6, 0.08, 0.3, 0.03])
ax6 = plt.axes([0.6, 0.06, 0.3, 0.03])
ax_table = plt.axes([0.63, 0.3, 0.07, 0.03])

sld_theta1 = Slider(ax1, r'$\theta_1$', -180, 180, valinit=0)
sld_theta2 = Slider(ax2, r'$\theta_2$', -180, 180, valinit=0)
sld_theta3 = Slider(ax3, r'$\theta_3$', -180, 180, valinit=0)
sld_theta4 = Slider(ax4, r'$\theta_4$', -180, 180, valinit=0)
sld_theta5 = Slider(ax5, r'$\theta_5$', -180, 180, valinit=0)
sld_theta6 = Slider(ax6, r'$\theta_6$', -180, 180, valinit=0)

# valor_inicial = cinematica.robot_IRB2600(grafica, [])

grafica.configuracion_grafica_x(-1000, 1000, -1000, 1000, -10, 1500, "Robot IRB2600")
Matriz_TH = cinematica.robot_IRB2600(grafica, [0, 0, 0, 0, 0, 0])
tabla = plt.table(cellText=np.round(Matriz_TH, 3), bbox=[2.6, 0, 2.6, 5], loc='center')

tabla.auto_set_font_size(False)
tabla.set_fontsize(8)
ax_table.axis('off')

sld_theta1.on_changed(actualizacion_juntas)
sld_theta2.on_changed(actualizacion_juntas)
sld_theta3.on_changed(actualizacion_juntas)
sld_theta4.on_changed(actualizacion_juntas)
sld_theta5.on_changed(actualizacion_juntas)
sld_theta6.on_changed(actualizacion_juntas)

plt.show()
