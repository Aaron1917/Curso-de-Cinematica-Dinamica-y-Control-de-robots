import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


def derivada(x_vector, t_, k_, b_,m_, F_):
    return x_vector[1], - (k_ / m_) * x_vector[0] - (b_ / m_) * x_vector[1] + (1 / m_) * F_


# Definimos las constantes
m = 10          # Masa del sistema 10 kg
k = 45           # Constante del resorte 1 N/m
b = 11           # Constante del amortiguador 1 N s/m
F = 10          # Fuerza 10 N

# Simulación
tiempo =np.linspace(0, 180, 200)
x_iniciales = (0, 0) # Condiciones iniciales del modelo
x_solución = odeint(derivada, x_iniciales, tiempo, args=(k, b, m, F))

fig , axs = plt. subplots(2)
fig.suptitle("Simulación Sistema masa resorte amortiguador")
axs[0].plot(tiempo, x_solución[:, 0])       # Indica la posición
axs[1].plot(tiempo, x_solución[:, 1])       # indica la velocidad
axs[0].set(xlabel="Tiempo (s)")
axs[0].set(ylabel=r"$x$"+"\n"+"Distancia (m)")
axs[1].set(xlabel="Tiempo (s)")
axs[1].set(ylabel=r"$\dot{x}$"+"\n"+"velocidad (m/s)")
plt.show()