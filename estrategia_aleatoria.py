import numpy as np
import matplotlib.pyplot as plt
import random

# Parámetros
N = 10000  # Número de rondas
d = 10    # Número de estrategias/brazos

X = np.array([np.random.binomial(1, random.uniform(0, 1), d) for _ in range(N)])

# Inicializar variables
strategies_selected_rs = []
total_reward_rs = 0
total_reward_bs = 0
rewards_strategies = [0] * d
regret = []

# Simulación
for n in range(0, N):
    # Estrategia Aleatoria
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]
    total_reward_rs += reward_rs

    for i in range(0, d):
        rewards_strategies[i] += X[n, i]
    total_reward_bs = max(rewards_strategies)

    # Arrepentimiento
    regret.append(total_reward_bs - total_reward_rs)

# Graficar
plt.plot(regret)
plt.title('Curva de Arrepentimiento - Estrategia Aleatoria')
plt.xlabel('Ronda')
plt.ylabel('Arrepentimiento')
plt.grid(True)
plt.show()
