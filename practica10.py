from cinematica_robots import cinematica
import matplotlib.pyplot as plt

grafica = cinematica()
# print(cinematica.matriz_traslacion_x(grafica,10))
# print(cinematica.matriz_traslacion_y(grafica,10))
# print(cinematica.matriz_traslacion_z(grafica,10))

# print(cinematica.matriz_rotacion_x(grafica,10))
# print(cinematica.matriz_rotacion_y(grafica,10))
# print(cinematica.matriz_rotacion_z(grafica,10))

# print(cinematica.denavit_hatemberg(grafica,0,0,0,90))

grafica.configuracion_grafica_z(-5,5,-10,10,-10,10,"")
print(cinematica.robot_RR(grafica,45,0,7,0,45,0,5,0))

#plt.title("Cinematica de robots")
plt.show()