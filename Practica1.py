import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(0, 10, 100)
y = np.cos(x)

print(x)
print(y)

plt.ion()  # Inicializar animación

figura, grafica = plt.subplots(figsize=(8, 6))
linea = grafica.plot(x, y)  # Construyo la línea de forma senoidal
punto, = grafica.plot(0, 0, 'bo')  # Dibujo punto en 0,0

# Descripción de la gráfica
plt.title("Gráfica de una señal coseno", fontsize=20)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)

for dato in x:
    punto.set_xdata(dato)
    punto.set_ydata(np.cos(dato))

    figura.canvas.draw()
    figura.canvas.flush_events()
    time.sleep(0.01)
