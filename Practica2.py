import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Declaramos una figura
figura, grafica = plt.subplots()

# Declaramos los parámetros de las gráficas
x = np.arange(0, 2 * np.pi, 0.01)  # Definimos n vecto de 0 a 2pi con intervalo de0.1
print(len(x))
linea, = grafica.plot(x, np.sin(x))  # Graficamos una linea
punto, = grafica.plot([], [], 'bo')  # Graficamos un punto

# Descripción de la gráfica
plt.title("Gráfica de una señal seno", fontsize=20)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)


# Definimos una funcion para realizar una animación
def animacion(i):
    punto.set_xdata(x[i])
    punto.set_ydata(np.sin(x[i]))
    return linea, punto


animation = animation.FuncAnimation(figura, animacion, frames=624, interval=2, blit=True, save_count=50)
plt.show()
