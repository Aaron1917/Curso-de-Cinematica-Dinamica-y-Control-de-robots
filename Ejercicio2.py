import math
import numpy as np

zetta = math.radians(60)  # Ángulo para eje z
epsilon = math.radians(50)  # Ángulo para eje y
delta = math.radians(80)  # Ángulo para eje x

Rx = np.array([[1, 0, 0],       # Declaramos la matriz de rotacion sobre el eje x
               [0, math.cos(delta), -math.sin(delta)],
               [0, math.sin(delta), math.cos(delta)]])

Ry = np.array([[math.cos(epsilon), 0, math.sin(epsilon)],       # Declaramos la matriz de rotacion sobre el eje y
               [0, 1, 0],
               [-math.sin(epsilon), 0, math.cos(epsilon)]])

Rz = np.array([[math.cos(zetta), -math.sin(zetta), 0],      # Declaramos la matriz de rotacion sobre el eje z
               [math.sin(zetta), math.cos(zetta), 0],
               [0, 0, 1]])

print(Rx)
print("La matriz de rotación es: ")
R = np.dot(np.dot(Rz, Ry), Rx)      # Multiplicamos las matrices de la forma ZYX
print(np.round(R, 5))           # Mostramos la matriz de rotación


def MatR2Euler(Rot):        # Declaramos la función
    beta_ = math.atan2(-Rot[2][0], math.sqrt(Rot[0][0] ** 2 + Rot[1][0] ** 2))       # Obtenemos beta
    if math.degrees(beta_) > 90.1 or math.degrees(beta_) < 89.9:      # Comprobamos que no exista una singularidad
        alpha_ = math.atan2(Rot[1][0] / math.cos(beta_), Rot[0][0] / math.cos(beta_))      # Obtenemos alpha
        gamma_ = math.atan2(Rot[2][1] / math.cos(beta_), Rot[2][2] / math.cos(beta_))      # Obtenemos gamma
    else:
        beta_ = alpha_ = gamma_ = 0
        print("Existe una singularidad")        # Mandamos un mensaje de advertencia
    return alpha_, beta_, gamma_       # Retornamos los valores obtenidos


def MatRot2FixedAngle(Rot):     # Declaramos la función
    theta_ = math.atan2(-Rot[2][0], math.sqrt(Rot[0][0] ** 2 + Rot[1][0] ** 2))     # Obtenemos theta
    if math.degrees(theta_) > 90.1 or math.degrees(theta_) < 89.9:      # Comprobamos que no exista una singularidad
        psi_ = math.atan2(Rot[1][0] / math.cos(theta_), Rot[0][0] / math.cos(theta_))       # Obtenemos psi
        phi_ = math.atan2(Rot[2][1] / math.cos(theta_), Rot[2][2] / math.cos(theta_))       # Obtenemos phi
    else:
        theta_ = psi_ = phi_ = 0
        print("Existe una singularidad")    # Mandamos un mensaje de advertencia
    return psi_, theta_, phi_   # Retornamos los valores obtenidos


def MatRot2AngleAxis(Rot):      # Declaramos la función
    theta_ = math.acos((Rot[0][0] + Rot[1][1] + Rot[2][2] - 1) / 2)     # Obtenemos el ángulo theta
    vec = np.array([[Rot[2][1] - Rot[1][2]],        # Obtenemos el eje de rotación
                    [Rot[0][2] - Rot[2][0]],
                    [Rot[1][0] - Rot[0][1]]])
    omega_u = np.multiply(vec, 1 / (2 * math.sin(theta_)))
    return theta_, omega_u      # Retornamos los valores obtenidos


def MatRot2Quaternion(Rot):     # Declaramos la función
    w_ = 0.5 * math.sqrt(1 + Rot[0][0] + Rot[1][1] + Rot[2][2])     # Obtenemos el valor de w
    z_ = (Rot[2][1] - Rot[1][2]) / (4 * w_)     # Obtenemos el valor de z
    y_ = (Rot[0][2] - Rot[2][0]) / (4 * w_)     # Obtenemos el valor de y
    x_ = (Rot[1][0] - Rot[0][1]) / (4 * w_)     # Obtenemos el valor de x
    return w_, x_, y_, z_       # Retornamos los valores obtenidos


def Euler2MatRot(roll_, pitch_, yaw_):      # Declaramos la función
    rx_ = np.array([[1, 0, 0],      # Obtenemos la matriz de rotación del eje x
                    [0, math.cos(yaw_), -math.sin(yaw_)],
                    [0, math.sin(yaw_), math.cos(yaw_)]])
    ry_ = np.array([[math.cos(pitch_), 0, math.sin(pitch_)],        # Obtenemos la matriz de rotación del eje y
                    [0, 1, 0],
                    [-math.sin(pitch_), 0, math.cos(pitch_)]])
    rz_ = np.array([[math.cos(roll_), -math.sin(roll_), 0],     # Obtenemos la matriz de rotación del eje z
                    [math.sin(roll_), math.cos(roll_), 0],
                    [0, 0, 1]])
    matRot = np.dot(np.dot(rz_, ry_), rx_)      # Combinamos la matriz de rotación
    return np.round(matRot, 5)      # Retornamos los valores obtenidos


def Euler2Quaternion(yaw_, pitch_, roll_):      # Declaramos la función
    q3 = np.sin(roll_ / 2) * np.cos(pitch_ / 2) * np.cos(yaw_ / 2) - np.cos(roll_ / 2) * np.sin(pitch_ / 2) * np.sin(
        yaw_ / 2)       # Obtenemos el valor de z
    q2 = np.cos(roll_ / 2) * np.sin(pitch_ / 2) * np.cos(yaw_ / 2) + np.sin(roll_ / 2) * np.cos(pitch_ / 2) * np.sin(
        yaw_ / 2)       # Obtenemos el valor de y
    q1 = np.cos(roll_ / 2) * np.cos(pitch_ / 2) * np.sin(yaw_ / 2) - np.sin(roll_ / 2) * np.sin(pitch_ / 2) * np.cos(
        yaw_ / 2)       # Obtenemos el valor de x
    q0 = np.cos(roll_ / 2) * np.cos(pitch_ / 2) * np.cos(yaw_ / 2) + np.sin(roll_ / 2) * np.sin(pitch_ / 2) * np.sin(
        yaw_ / 2)       # Obtenemos el valor de w
    return q0, q1, q2, q3       # Retornamos los valores obtenidos


def Quaternion2Euler(q0, q1, q2, q3):       # Declaramos la función
    roll_ = math.atan2(2 * ((q0 * q1) + (q2 * q3)), 1 - 2 * ((q1 ** 2) + (q2 ** 2)))        # Obtenemos el valor de roll
    pitch_ = math.asin(2 * (q0 * q2 - q3 * q1))     # Obtenemos el valor de pitch
    yaw_ = math.atan2(2 * ((q0 * q3) + (q1 * q2)), 1 - 2 * ((q2 ** 2) + (q3 ** 2)))     # Obtenemos el valor de yaw
    roll_ = round(roll_, 5)     # Limitamos el número de decimales
    pitch_ = round(pitch_, 5)
    yaw_ = round(yaw_, 5)
    return roll_, pitch_, yaw_      # Retornamos los valores obtenidos


def Quaternion2MatRot(q0, q1, q2, q3):      # Declaramos la función
    # Obtenemos la matriz de rotación en función de los valores de las variables del cuaternion
    Rot = np.array([[1 - 2 * (q1 ** 2) - 2 * (q2 ** 2), 2 * q2 * q3 - 2 * q0 * q1, 2 * q1 * q3 + 2 * q0 * q2],
                    [2 * q2 * q3 + 2 * q0 * q1, 1 - 2 * (q1 ** 2) - 2 * (q3 ** 2), 2 * q1 * q2 - 2 * q0 * q3],
                    [2 * q1 * q3 - 2 * q0 * q2, 2 * q1 * q2 + 2 * q0 * q3, 1 - 2 * (q2 ** 2) - 2 * (q3 ** 2)]])
    return Rot      # Retornamos los valores obtenidos


print("\nConversión de matriz de rotación a ángulos de Euler para el orden Z,Y,X\n")
roll, pitch, yaw = MatR2Euler(R)        # Llamamos la función
# Convertimos los valores a grados
roll = math.degrees(roll)  # alpha, X
pitch = math.degrees(pitch)  # beta, Y
yaw = math.degrees(yaw)  # gamma, Z
# Imprimimos los valores obtenidos
print(f"El valor de alpha es: {roll} X \nEl valor de beta es: {pitch} Y \nEl valor de gamma es: {yaw} Z \n")

print("Conversión de matriz de rotación a Ángulos fijos ψ, θ, ϕ\n")
psi, theta, phi = MatRot2FixedAngle(R)      # Llamamos la función
# Imprimimos los valores obtenidos
print(f"El valor de psi es: {psi} rad\nEl valor de theta es: {theta} rad\nEl valor de phi es: {phi} rad\n")

print("Conversión de matriz de rotación a Ángulo de eje θ ω \n")
theta, omega = MatRot2AngleAxis(R)      # Llamamos la función
theta = math.degrees(theta)     # Convertimos los valores a grados
# Imprimimos los valores obtenidos
print(f"El valor del ángulo es: {theta}\nEl vector del eje es: \n{omega}\n")

print("Conversión de matriz de rotación a Cuaterniones\n")
w, x, y, z = MatRot2Quaternion(R)       # Llamamos la función
# Imprimimos los valores obtenidos
print(f"El valor de w = {w}\nEl valor de x = {x}\nEl valor de y = {y}\nEl valor de z = {z}\n")

# Adicionalmente podemos comprobar resultados de las operaciones con los respectivas
# conversiones que se realizarón
print("\nDe ángulo de Euler a Matriz de rotación\n")
print(Euler2MatRot(math.radians(roll), math.radians(pitch), math.radians(yaw)))
print("\nDe ángulo de Euler a Cuaternión\n")
print(Euler2Quaternion(math.radians(roll), math.radians(pitch), math.radians(yaw)))
print("\nDe Cuaternión a ángulo de Euler\n")
print(Quaternion2Euler(w, x, y, z))
print("en radianes")
print("\nDe Cuaternión a Matriz de rotación\n")
print(Quaternion2MatRot(w, x, y, z))
