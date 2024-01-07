from cinematica_robots import cinematica
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import math

grafica = cinematica()
grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")
cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)


def actualizacion_juntas(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_z(-10, 10, -10, 10, -10, 10, "Robot 2 g.d.l RR")

    theta_1 = sld_angulo_1.val
    theta_2 = sld_angulo_2.val

    Matriz_TH = cinematica.robot_RR(grafica, theta_1, 0, 7, 0, theta_2, 0, 5, 0)

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


# Agregamos slidersbar para mover los angulos del robot
ax1 = plt.axes([0.2, 0.05, 0.65, 0.03])
ax2 = plt.axes([0.2, 0.01, 0.65, 0.03])

Matriz_TH = cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)
tabla = plt.table(cellText=np.round(Matriz_TH, 3), bbox=[0.9, 15, 0.3, 4.5], loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(8)

sld_angulo_1 = Slider(ax1, r'$\theta_1$', 0, 180, valinit=45)
sld_angulo_2 = Slider(ax2, r'$\theta_2$', 0, 360, valinit=45)

sld_angulo_1.on_changed(actualizacion_juntas)
sld_angulo_2.on_changed(actualizacion_juntas)

plt.show()
