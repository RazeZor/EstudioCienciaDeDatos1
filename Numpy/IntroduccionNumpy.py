import numpy as np # forma de llamar la biblioteca 
import os 
import random 

# instalacion con pip 

os.system("cls")
print("creacion de array con numpy ")
array = np.array([1,2,3,4,5,6])
print(array)

input("Presiona enter para avanzar ")

print("llenar con 0 : ")
ArrayZero = np.zeros(81) # creacion de 81 zeros 
print(ArrayZero)

input("Presiona enter para avanzar ")
print("crear un array vacio que recibe tantos numeros como uno le entregue  ")
ArrayVacio = np.empty(10)
print(ArrayVacio)
print("cuando usas np.empty(10), NumPy asigna espacio en memoria para un array de tamaño 10, pero no inicializa los valores.")

input("Presiona enter para avanzar ")

a = np.ones((2, 2))     # Matriz de unos 
b = np.eye(3)           # Matriz identidad
c = np.full((3, 3), 7)  # Matriz llena de un valor específico
d = np.linspace(0, 10, 5)  # 5 valores equidistantes entre 0 y 10
print(a,"se llenara con 1-1 en fila y 1-1 con columna ")
print(b)
print(c) # aqui creo una matiz de 3 x 3 pero que se llenen con el 7 

print(d) # el tipico beetwing que uno hace en programacion

r1 = np.random.rand(3, 3)      # Matriz de números aleatorios entre 0 y 1
r2 =np.random.randint(0, 100, (3, 3))  # Enteros entre 0 y 10
r3 =np.random.normal(0, 1, (3, 3))  # Distribución normal

print(r1)
print(r2)
print(r3)