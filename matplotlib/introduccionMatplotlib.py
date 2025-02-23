# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
# Crear la figura y los ejes
fig,ax = plt.subplots()
# Dibujar puntos  ax.scatter(x = [1, 2, 3], y = [3, 2, 1]) manejo de forma real
# Guardar el gráfico en formato png plt.savefig('diagrama-dispersion.png')

# creacion de grafico de lineas 
#ax.plot(["miguel", "pablo", "ignacio"], [2, 5, 7])

#grafico de barras
#ax.bar(["nacho","javier","samuel"],[5,1,9])


# Diagramas de sectores
#ax.pie([5,3]) # va a depender de la cantidad de Valores 

# diagrama Interactivo 

# horas trabajadas por dia 
# Definir días de la semana
 
dias_de_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]

# Ingresar salarios para Miguel y José
salario_miguel = []
salario_jose = []

for dia in dias_de_semana:
    salario = int(input(f"Ingrese el salario de Miguel para el día {dia}: "))
    salario_miguel.append(salario)

for dia in dias_de_semana:
    salario = int(input(f"Ingrese el salario de Jose para el día {dia}: "))
    salario_jose.append(salario)

ax.plot(dias_de_semana, salario_miguel, marker='o', color='tab:red', label="Miguel")
ax.plot(dias_de_semana, salario_jose, marker='s', color='tab:blue', label="José")

# Personalizar el gráfico
ax.set_title('Indice de salarios ', loc="left", fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
ax.set_xlabel("Días de la semana")
ax.set_ylabel("Salario ($)")
ax.legend()
ax.grid(True)

# Mostrar el gráfico
plt.show()