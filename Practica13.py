import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from cinematica_robots import cinematica

grafica = cinematica()
grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")
cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)


def cinematica_inversa(x, y, a1, a2):
    theta_2 = math.acos((x ** 2 + y ** 2 - a1 ** 2 - a2 ** 2) / (2 * a1 * a2))
    theta_1 = math.atan2(y, x) - math.atan2(a2 * math.sin(theta_2), a1 + a2 * math.cos(theta_2))
    theta_1 = round((theta_1 * 180) / np.pi, 1)
    theta_2 = round((theta_2 * 180) / np.pi, 1)
    return theta_1, theta_2


def actualizacion_juntas(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")

    theta_1 = sld_x.val
    theta_2 = sld_y.val

    cinematica.robot_RR(grafica, theta_1, 0, 7, 0, theta_2, 0, 5, 0)
    plt.draw()
    plt.pause(1e-5)


def actualizacion_juntas2(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")
    # Como usuarios ingresamos los valores de x & y
    x = sld_x.val
    y = sld_y.val
    # Obtenemos la cinematica inversa
    theta_1, theta_2 = cinematica_inversa(x, y, 7, 5)
    # Obtenemos la cinematica directa para obtener MTH
    Matriz_TH = cinematica.robot_RR(grafica, theta_1, 0, 7, 0, theta_2, 0, 5, 0)
    sld_x.eventson = False
    sld_x.set_val(Matriz_TH[0, 3])
    sld_x.eventson = True
    i = 0
    j = 0
    while i < 4:
        while j < 4:
            tabla._cells[(i, j)]._text.set_text(np.round(Matriz_TH[i, j], 2))
            j += 1
        j = 0
        i += 1

    plt.draw()
    plt.pause(1e-5)

def actualizacion_juntas3(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")
    # Como usuarios ingrsamos los valores de x & y
    x = sld_x.val
    y = sld_y.val

    # Obtenemos la cinemática inversa
    theta_1, theta_2 = cinematica_inversa(x, y, 7, 5)
    # Obtenemos la cinemática directa para obtener MTH
    Matriz_TH = cinematica.robot_RR(grafica, theta_1, 0, 7, 0, theta_2, 0, 5, 0)
    # Llenamos la tabla
    sld_y.eventson = False
    sld_y.set_val(Matriz_TH[1, 3])
    sld_y.eventson = True
    i = 0
    j = 0
    while i < 4:
        while j < 4:
            tabla._cells[(i, j)]._text.set_text(np.round(Matriz_TH[i, j], 2))
            j += 1
        j = 0
        i += 1

    plt.draw()
    plt.pause(1e-5)


# Agregamos slidersbar para mover los ángulos del robot
ax1 = plt.axes([0.2, 0.05, 0.65, 0.03])
ax2 = plt.axes([0.2, 0.01, 0.65, 0.03])

Matriz_TH = cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)
tabla = plt.table(cellText=np.round(Matriz_TH, 3), bbox=[0.9, 15, 0.3, 4.5], loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(8)

sld_x = Slider(ax1, r'$x$', -12, 12, valinit=5)
sld_y = Slider(ax2, r'$y$', 0, 10, valinit=10)

sld_x.on_changed(actualizacion_juntas3)
sld_y.on_changed(actualizacion_juntas2)

plt.show()
