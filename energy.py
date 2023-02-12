import matplotlib.pyplot as plt
import numpy as np

# Constante da mola (k)
k = 2.0

# Posição inicial da massa (x0)
x0 = 1.0

# Velocidade inicial da massa (v0)
v0 = 0.0

# Tempo (t)
t = np.linspace(0, 10, 100)

# Função para calcular a posição da massa (x)
def x(t):
  return x0 * np.cos(np.sqrt(k) * t) + (v0 / np.sqrt(k)) * np.sin(np.sqrt(k) * t)

# Função para calcular a velocidade da massa (v)
def v(t):
  return -x0 * np.sin(np.sqrt(k) * t) * np.sqrt(k) + v0 * np.cos(np.sqrt(k) * t)

# Função para calcular a energia total (E)
def E(t):
  return 0.5 * k * x(t) ** 2 + 0.5 * v(t) ** 2

# Plot da posição da massa (x)
plt.plot(t, x(t), label='Posição da massa')

# Plot da velocidade da massa (v)
plt.plot(t, v(t), label='Velocidade da massa')

# Plot da energia total (E)
plt.plot(t, E(t), label='Energia total')

# Configurações do gráfico
plt.xlabel('Tempo (t)')
plt.ylabel('Energia (E)')
plt.legend()
plt.show()
