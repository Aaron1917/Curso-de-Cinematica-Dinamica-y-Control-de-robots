from cinematica_robots import cinematica
import matplotlib.pyplot as plt

plano = cinematica()

theta_i = 45
if theta_i > 0:
    min_ = 1
    max_ = theta_i + 1
    step = 1
else:
    min_ = -1
    max_ = theta_i - 1
    step = -1


for theta_i in range(min_, max_, step):
    plano.grafica.cla()
    plano.configuracion_grafica_z(-5, 5, -10, 10, -10, 10, "")
    cinematica.robot_RR(plano, theta_i, 0, 7, 0, 0, 0, 5, 0)
    plt.draw()
    plt.pause(1e-5)

theta_i = -45

if theta_i > 0:
    min_ = 1
    max_ = theta_i + 1
    step = 1
else:
    min_ = -1
    max_ = theta_i - 1
    step = -1

for theta_i in range(min_, max_, step):
    plano.grafica.cla()
    plano.configuracion_grafica_z(-5, 5, -10, 10, -10, 10, "")
    cinematica.robot_RR(plano, 45, 0, 7, 0, theta_i, 0, 5, 0)
    plt.draw()
    plt.pause(1e-5)

plt.show()
