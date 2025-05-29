#Inteligencia Artificial aplicada a Negocios y Empresas
#Maximización de beneficios de una empresa de venta online con Muestreo Thompson

#Imporptar librerias

import numpy as np
import matplotlib.pyplot as plt
import random

#Configuracion de parametros

N = 10000
d = 9

#Creacion de la simulacion
conversion_rates = [0.05, 0.13, 0.9, 0.16, 0.11, 0.04, 0.20, 0.08, 0.01]
X = np.array(np.zeros([N, d]))
for i in range(N):
    for j in range(d):
        if np.random.rand() <= conversion_rates[j]:
            X[i,j] = 1


#Implementacion de la Seleccion Aleatoria y el Muestreo de Thompson
# Listas donde guardamos las estrategias seleccionadas
strategies_selected_rs = []  # Aleatorio
strategies_selected_ts = []  # Thompson

# Recompensa acumulada
total_reward_rs = 0
total_reward_ts = 0 

# Contadores de recompensas para cada estrategia
number_of_rewards_1 = [0] * d  # Veces que cada estrategia dio recompensa = 1
number_of_rewards_0 = [0] * d  # Veces que dio recompensa = 0

for n in range(0, N):
    #Estrategia aleatoria 
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs =X[n, strategy_rs]
    total_reward_rs += reward_rs
    for i in range(0, d):
        random_beta = random.betavariate(number_of_rewards_1[i], number_of_rewards_0[i])

plt.imshow(X, aspect='auto', cmap='coolwarm')
plt.title("Simulación de conversiones de usuarios")
plt.xlabel("Estrategia")
plt.ylabel("Usuario")
plt.colorbar(label="Conversión (0 = No, 1 = Sí)")
plt.show()
