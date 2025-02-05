import matplotlib.pyplot as plt

def calcular_errores(x, y, valor_real):
    """
    Calcula la diferencia, error absoluto, error relativo y error porcentual entre dos valores y un valor real.

    Args:
        x: Un valor numérico.
        y: Otro valor numérico.
        valor_real: El valor real de la cantidad que se está aproximando.

    Returns:
        Una tupla conteniendo el error absoluto y el error relativo.
    """
    diferencia = x - y  # Calcula la diferencia entre x e y.
    error_abs = abs(valor_real - diferencia)  # Calcula el error absoluto entre el valor real y la diferencia.
    error_rel = error_abs / abs(valor_real) if valor_real != 0 else float('inf') # Calcula el error relativo. Maneja el caso de valor_real = 0 para evitar división por cero.
    error_pct = error_rel * 100  # Calcula el error porcentual.
    return diferencia, error_abs, error_rel, error_pct  # Retorna la diferencia, el error absoluto y el error relativo.

valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]  # Define una lista de tuplas con valores para x, y y valor_real.

resultados = []  # Lista para almacenar los resultados de cada cálculo

for x, y, real in valores:  # Itera sobre la lista de valores.
    diferencia, error_abs, error_rel, error_pct = calcular_errores(x, y, real)  # Llama a la función calcular_errores con los valores actuales.
    resultados.append([x, y, diferencia, error_abs, error_rel, error_pct])  # Agrega los resultados a la lista

# Crear la tabla
print("Tabla de resultados:")
print("----------------------------------------------------------------------------------")
print("      x                 y              Diferencia      Error Absoluto Error Relativo  Error Porcentual")
print("----------------------------------------------------------------------------------")
for x, y, diferencia, error_abs, error_rel, error_pct in resultados:
    print(f"{x:10.7f}   {y:10.7f}      {diferencia:10.7f}       {error_abs:10.7f}     {error_rel:10.7f}     {error_pct:10.7f}%")
print("----------------------------------------------------------------------------------")

# Crear el gráfico de barras
n_grupos = len(valores)  # Número de grupos (uno por cada conjunto de datos)
error_abs_vals = [error_abs for _, _, _, error_abs, _, _ in resultados]  # Valores de error absoluto
error_rel_vals = [error_rel for _, _, _, _, error_rel, _ in resultados]  # Valores de error relativo
error_pct_vals = [error_pct for _, _, _, _, _, error_pct in resultados]  # Valores de error porcentual

indice = range(n_grupos)  # Índice para las barras

plt.bar(indice, error_abs_vals, label='Error Absoluto')  # Barras de error absoluto
plt.bar(indice, error_rel_vals, label='Error Relativo', bottom=error_abs_vals)  # Barras de error relativo sobre las de error absoluto
plt.bar(indice, error_pct_vals, label='Error Porcentual', bottom=[error_abs_vals[i] + error_rel_vals[i] for i in range(n_grupos)])  # Barras de error porcentual sobre las de error absoluto y relativo

plt.xlabel('Conjunto de datos')  # Etiqueta del eje x
plt.ylabel('Valor del error')  # Etiqueta del eje y
plt.title('Gráfico de barras de errores')  # Título del gráfico
plt.xticks(indice, ('1', '2'))  # Etiquetas de las barras (números de conjunto de datos)
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar el gráfico