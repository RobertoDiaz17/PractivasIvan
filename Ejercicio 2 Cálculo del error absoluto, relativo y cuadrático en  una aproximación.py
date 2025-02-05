import numpy as np  # Importa la librería NumPy para operaciones numéricas.
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para graficar.

def leibniz_pi(n):
    """
    Calcula una aproximación de pi usando la serie de Leibniz.

    Args:
        n: El número de términos a usar en la serie.

    Returns:
        La aproximación de pi.
    """
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))  # Calcula la suma de la serie y multiplica por 4.

true_pi = np.pi  # Obtiene el valor de pi de NumPy.
N_values = [10, 100, 1000, 10000]  # Define los valores de N (número de términos) a usar.
errors_abs = []  # Inicializa una lista para almacenar los errores absolutos.
errors_rel = []  # Inicializa una lista para almacenar los errores relativos.

for N in N_values:  # Itera sobre los valores de N.
    approx_pi = leibniz_pi(N)  # Calcula la aproximación de pi para el valor de N actual.
    error_abs = abs(true_pi - approx_pi)  # Calcula el error absoluto.
    error_rel = error_abs / true_pi  # Calcula el error relativo.
    errors_abs.append(error_abs)  # Agrega el error absoluto a la lista.
    errors_rel.append(error_rel)  # Agrega el error relativo a la lista.
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}")  # Imprime los errores para cada N.

plt.figure()  # Crea una nueva figura para el gráfico.
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')  # Grafica los errores absolutos.
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')  # Grafica los errores relativos.
plt.xscale('log')  # Establece la escala del eje x a logarítmica.
plt.yscale('log')  # Establece la escala del eje y a logarítmica.
plt.xlabel('N')  # Etiqueta el eje x.
plt.ylabel('Error')  # Etiqueta el eje y.
plt.legend()  # Muestra la leyenda del gráfico.
plt.title('Errores en la aproximación de pi')  # Establece el título del gráfico.
plt.show()  # Muestra el gráfico.