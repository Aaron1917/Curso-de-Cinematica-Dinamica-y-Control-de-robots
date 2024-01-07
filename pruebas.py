# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
#
# from cinematica_robots import cinematica
#
# grafica = cinematica()
# grafica.configuracion_grafica_z(-5, 5, -10, 10, -10, 10, "Robot 2 g.d.l. RR")
#
# cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)
#
#
# def actualizacion_juntas(val):
#     grafica.grafica.cla()
#     grafica.configuracion_grafica_z(-5, 5, -10, 10, -10, 10, "Robot 2 g.d.l. RR")
#
#     theta_1 = sld_ang_1.val
#     theta_2 = sld_ang_2.val
#
#     cinematica.robot_RR(grafica, theta_1, 0, 7, 0, theta_2, 0, 5, 0)
#     plt.draw()
#     plt.pause(1e-5)
#
#
# # Agregamos Slider para mover los ángulos del robot
# ax1 = plt.axes([0.2, 0.05, 0.65, 0.03])
# ax2 = plt.axes([0.2, 0.01, 0.65, 0.03])
#
# sld_ang_1 = Slider(ax1, r'$\theta_1$', 0, 180, valinit=45)
# sld_ang_2 = Slider(ax2, r'$\theta_2$', 0, 180, valinit=45)
#
# sld_ang_1.on_changed(actualizacion_juntas)
# sld_ang_2.on_changed(actualizacion_juntas)
#
# plt.show()

import math

print(math.asin(43.18651110315231))


def cinematica_inversa(x, y, z):
    # siendo los eslabones
    l3 = 3
    l4 = 3
    l5 = 3
    l6 = 2
    l7 = 2
    val = math.sqrt(x ** 2 + y ** 2 + (z - 6) ** 2 - 9) - 4
    print(val)
    print("------------------------")
    print(((x ** 2 + y ** 2) ** 2)/(x ** 2 + y ** 2 + (z - 6) ** 2))
    print( math.atan2(3, (x ** 2 + y ** 2 + (z - 6) ** 2 - 9)))
    alpha_2 = math.asin(((x ** 2 + y ** 2) ** 2)/(x ** 2 + y ** 2 + (z - 6) ** 2)) + math.atan2(3, (x ** 2 + y ** 2 + (z - 6) ** 2 - 9))
    print(alpha_2)
    print("++++++++++++++++++++++++++++++")
    print(x)
    print((4 + val) * math.sin(alpha_2) - 3 * math.cos(alpha_2))
    theta_2 = math.asin(x/((4 + val) * math.sin(alpha_2) - 3 * math.cos(alpha_2)))
    theta_2 = round((theta_2 * 180) / np.pi, 1)
    alpha_2 = round((alpha_2 * 180) / np.pi, 1)
    return theta_2, alpha_2, val