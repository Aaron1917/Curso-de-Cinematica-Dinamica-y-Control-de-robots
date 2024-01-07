# modelo dinmico
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def dynamic_model(x_, time, tau1, tau2):
    m1 = 0.4272
    m2 = 0.3442
    l1 = 0.1933
    l2 = 0.1458
    lc1 = 0.0741
    lc2 = 0.04849
    I1 = 0.0036
    I2 = 0.0021
    g = 9.8

    m11 = (m1 * (lc1 ** 2)) + (m2 * (l1 ** 2)) + (m2 * (lc2 ** 2)) + (2 * m2 * l1 * lc2 * np.cos(x_[2])) + I1 + I2
    m12 = (m2 * (lc2 ** 2)) + (m2 * l1 * lc2 * np.cos(x_[2])) + I2
    m21 = (m2 * (lc2 ** 2)) + (m2 * l1 * lc2 * np.cos(x_[2])) + I2
    m22 = (m2 * (lc2 ** 2)) + I2

    c11 = -m2 * l1 * lc2 * np.sin(x_[2]) * x_[3]
    c12 = -m2 * l1 * lc2 * np.sin(x_[2]) * (x_[1] + x_[3])
    c21 = m2 * l1 * lc2 * np.sin(x_[2]) * x_[1]
    c22 = 0

    g1 = ((m1 * lc1 * m2 * l1) * g * np.sin(x_[0])) + (m2 * lc2 * g * np.sin(x_[0] + x_[2]))
    g2 = m2 * lc2 * g * np.sin(x_[0] + x_[2])

    D4 = (m11 * m22) + (m12 * m21)
    D5 = tau1 - c11 * x_[1] - c12 * x_[3] - g1
    D6 = tau2 - c21 * x_[1] - c22 * x_[3] - g2

    x_[0] = x_[1]
    x_[1] = ((m22 * D5) - (m12 * D6)) / D4
    x_[2] = x_[3]
    x_[3] = ((-m21 * D5) + (m11 * D6)) / D4

    return x_[0], x_[1], x_[2], x_[3]


# tiempo
time = np.linspace(0, 1.2, 500)
# condiciones
x = (0, 0, 0, 0)
tau = (0, 0.032)

x_solved = odeint(dynamic_model, x, time, args=(tau[0], tau[1]))

f = plt.figure(figsize=(16, 9))
plt.plot(time, x_solved[:, 0], label='x1')
plt.plot(time, x_solved[:, 1], label='x2')
plt.plot(time, x_solved[:, 2], label='x3')
plt.plot(time, x_solved[:, 3], label='x4')
plt.legend(loc='best')
plt.show()
