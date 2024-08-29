import matplotlib.pyplot as plt

# Datos para el gráfico
labels = ['Positivo', 'Negativo', 'Neutral']
first_test = [15, 20, 14]  # Ajustado
second_test = [11, 21, 13]  # Real

x = range(len(labels))

# Crear el gráfico de barras
plt.bar(x, first_test, width=0.4, label='Primera Prueba', align='center')
plt.bar(x, second_test, width=0.4, label='Segunda Prueba', align='edge')

# Añadir etiquetas y título
plt.xlabel('Categoría de Sentimiento', fontweight='bold')
plt.ylabel('Número de Segmentos', fontweight='bold')
plt.title('Distribución Proporcional de Sentimientos en Pruebas')

# Añadir leyenda
plt.xticks(x, labels)
plt.legend()
plt.show()
