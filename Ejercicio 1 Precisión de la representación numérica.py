import numpy as np  # Se importa numpy, aunque en este código no se usa.

# Inicializamos epsilon con 1.0
epsilon = 1.0

# Contador de iteraciones para rastrear cuántas veces se divide epsilon
iteracion = 0

# Bucle para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:  # Mientras la suma aún sea distinguible de 1.0
    epsilon /= 2  # Se divide epsilon por 2 en cada iteración
    iteracion += 1  # Se incrementa el contador de iteraciones
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon}")

# Para obtener la verdadera precisión de máquina, multiplicamos por 2,
# ya que la última iteración hizo que epsilon fuera demasiado pequeño.
epsilon *= 2

# Se muestra la precisión de máquina encontrada
print(f"Precisión de máquina final: {epsilon}")
