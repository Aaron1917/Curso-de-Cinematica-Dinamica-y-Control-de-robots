from cinematica_robots import cinematica
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

grafica = cinematica()
grafica.configuracion_grafica(-10, 10, -10, 10, -10, 10, "Robot 1 RPP")
cinematica.robot_RR(grafica, 45, 0, 7, 0, 45, 0, 5, 0)

