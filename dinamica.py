import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate


def funcion(x_vector, t, T_, F_, g_, m_):  # de modo: a, b, th, r
    return [-1 * (g_ / x_vector[3]) * math.cos(x_vector[2]) - (2 / x_vector[3]) * x_vector[0] * x_vector[1] + (
                T_ / m_ * x_vector[3] ** 2), x_vector[3] * x_vector[0] ** 2 - g_ * math.sin(x_vector[2]) + (F_ / m_),
            x_vector[0], x_vector[1]]


# definimos constantes
d = 4  # r              m
v = 0.001  # r punto        m/s
o = 0.1  # theta punto    rad/s
print(np.pi)
the = np.pi / 4  # theta          rad
T = 0.0  # par            N*m
F = 0.0  # fuerza         N
g = 9.81  # gravedad       m/s^2
m = 1.0  # masa           kg

x_init = (o, v, the, d)
tiempo = np.linspace(0, 10, 400)
#

x_solucion = integrate.odeint(funcion, x_init, tiempo, args=(T, F, g, m))

fig , axs = plt. subplots(2)
fig2, axs2 = plt.subplots(2)
fig.suptitle(r"Simulación robot 2 GDL para $\theta$")
fig2.suptitle(r"Simulación robot 2 GDL para $r$")
axs[0].plot(tiempo, x_solucion[:, 2])
axs[1].plot(tiempo, x_solucion[:, 0])
axs2[0].plot(tiempo, x_solucion[:, 3])
axs2[1].plot(tiempo, x_solucion[:, 1])
axs[0].set(xlabel="Tiempo (s)")
axs[0].set(ylabel=r"$\theta$"+"\n"+"Distancia (rad)")
axs[1].set(xlabel="Tiempo (s)")
axs[1].set(ylabel=r"$\dot{\theta}$"+"\n"+"Velocidad (rad/s)")
axs2[0].set(xlabel="Tiempo (s)")
axs2[0].set(ylabel=r"$r$"+"\n"+"Distancia (m)")
axs2[1].set(xlabel="Tiempo (s)")
axs2[1].set(ylabel=r"$\dot{r}$"+"\n"+"Velocidad (m/s)")
plt.show()