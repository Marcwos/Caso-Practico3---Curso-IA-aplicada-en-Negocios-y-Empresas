import numpy as np
import matplotlib.pyplot as plt
import random

# Parámetros
N = 10000 # Número de rondas
d = 10    # Número de estrategias/brazos

X = np.array([np.random.binomial(1, random.uniform(0, 1), d) for _ in range(N)])

# Inicializar variables
strategies_selected_ts = []
total_reward_ts = 0
total_reward_bs = 0
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
rewards_strategies = [0] * d
regret = []

# Simulación
for n in range(0, N):
    # Muestreo de Thompson
    strategy_ts = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1,
                                         numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n, strategy_ts]
    if reward_ts == 1:
        numbers_of_rewards_1[strategy_ts] += 1
    else:
        numbers_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts += reward_ts

    # Mejor Estrategia
    for i in range(0, d):
        rewards_strategies[i] += X[n, i]
    total_reward_bs = max(rewards_strategies)

    # Arrepentimiento
    regret.append(total_reward_bs - total_reward_ts)

# Graficar
plt.plot(regret)
plt.title('Curva de Arrepentimiento - Muestreo de Thompson')
plt.xlabel('Ronda')
plt.ylabel('Arrepentimiento')
plt.grid(True)
plt.show()
