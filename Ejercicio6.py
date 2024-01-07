from cinematica_robots import cinematica
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

grafica = cinematica()
grafica.configuracion_grafica_x(-10, 10, -10, 10, -10, 10, "Robot 1 RPP")
cinematica.robot_1(grafica, (45, 0, 0, 0), (0, 5, 0, -90), (90, 5, 0, 0))


def actualizacion_juntas(val):
    grafica.grafica.cla()
    grafica.configuracion_grafica_x(-10, 10, -10, 10, -10, 10, "Robot 1 RPP")

    theta_1 = sld_angulo_1.val
    d2 = sld_d2.val
    d3 = sld_d3.val

    cinematica.robot_1(grafica, (theta_1, 0, 0, 0), (0, 2 + d2, 0, -90), (90, 2 + d3, 0, 0))

    plt.draw()
    plt.pause(1e-5)


# Agregamos slidersbar para mover los angulos del robot
ax1 = plt.axes([0.2, 0.01, 0.65, 0.03])
ax2 = plt.axes([0.2, 0.03, 0.65, 0.03])
ax3 = plt.axes([0.2, 0.05, 0.65, 0.03])

sld_angulo_1 = Slider(ax1, r'$\theta_1$', 0, 360, valinit=45)
sld_d2 = Slider(ax2, r'$d_2$', 0, 4, valinit=3)
sld_d3 = Slider(ax3, r'$d_3$', 0, 4, valinit=3)

sld_angulo_1.on_changed(actualizacion_juntas)
sld_d2.on_changed(actualizacion_juntas)
sld_d3.on_changed(actualizacion_juntas)

plt.show()
