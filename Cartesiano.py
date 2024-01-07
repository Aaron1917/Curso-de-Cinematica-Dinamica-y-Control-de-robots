from cinematica_robots import cinematica
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

grafica = cinematica()
grafica.configuracion_grafica_x(-1, 10, -1, 10, -1, 10, "Robot Cartesiano")
cinematica.robot_cartesiano(grafica, (0, 0, .5 + 3, 0), (90, 6, 1 + 5, -90), (90, 1, .5 + 4, 0))


def actualizacion_juntas(val):
    grafica.grafica.cla()

    L1 = sld_L1.val
    L2 = sld_L2.val
    L3 = sld_L3.val
    # d4 = sld_d4.val

    grafica.configuracion_grafica_x(-1, 10, -1, 10, -1, 10, "Robot Cartesiano")
    cinematica.robot_cartesiano(grafica, (0, 0, .5 + L1, 0), (90, 6, 1 + L2, -90), (90, 1, .5 + L3, 0))

    plt.draw()
    plt.pause(1e-5)


# Agregamos slidersbar para mover los angulos del robot
ax1 = plt.axes([0.2, 0.01, 0.65, 0.03])
ax2 = plt.axes([0.2, 0.03, 0.65, 0.03])
ax3 = plt.axes([0.2, 0.05, 0.65, 0.03])
# ax4 = plt.axes([0.2, 0.07, 0.65, 0.03])

sld_L1 = Slider(ax1, r'$\L_1$', 0, 8, valinit=3)
sld_L2 = Slider(ax2, r'$\L_2$', 0, 6, valinit=5)
sld_L3 = Slider(ax3, r'$\L_3$', 0, 5, valinit=4)
# sld_d4 = Slider(ax4, r'$d_4$', 0, 4, valinit=2)

sld_L1.on_changed(actualizacion_juntas)
sld_L2.on_changed(actualizacion_juntas)
sld_L3.on_changed(actualizacion_juntas)
#sld_d4.on_changed(actualizacion_juntas)

plt.show()
