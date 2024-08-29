import matplotlib.pyplot as plt
 
# Se muestran gráficamente los resultados del análisis de sentimiento
# Datos para el gráfico
users = ['Andrea', 'Dayluana', 'Javier', 'María', 'Nelly']
positive_counts = [6, 2, 1, 3, 2]
negative_counts = [7, 8, 2, 4, 3]
neutral_counts = [3, 4, 2, 3, 1]

# Configuración del gráfico de barras
barWidth = 0.2
r1 = range(len(users))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Crear el gráfico de barras
plt.bar(r1, positive_counts, color='g', width=barWidth, edgecolor='grey', label='Positivo')
plt.bar(r2, negative_counts, color='r', width=barWidth, edgecolor='grey', label='Negativo')
plt.bar(r3, neutral_counts, color='b', width=barWidth, edgecolor='grey', label='Neutral')

# Añadir etiquetas y título
plt.xlabel('Usuarios', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(users))], users)
plt.ylabel('Número de segmentos')
plt.title('Distribución de Sentimientos por Usuario (Segunda prueba de usabilidad en tablet)')

# Añadir leyenda
plt.legend()
plt.show()
