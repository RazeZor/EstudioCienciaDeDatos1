import numpy as np 
import os 
os.system("cls")

matriz = np.arange(1,82).reshape(9, 9)

def imprimirMatriz(matriz):
    for fila in range(9):  
        for col in range(9):
            print(matriz[fila][col], end=" ")  
        print()  

imprimirMatriz(matriz)
def Insertar(dato,matriz,posy,posx):
    matriz[posy][posx] = dato # agregamos dentro de las coordenadas 
    imprimirMatriz(matriz)


while True:
    try:
        dato = int(input("ingresa el tipo de dato que tu quieras insertar, tiene que ser un numero "))
        print(f"tu dato es el numero {dato} y fue correctamente Ingresado ")
        posy= int(input("ingresa la posicion del eje y "))
        if posy < 0 or posy >= 9: # negative programming 
            print("exedes el limite ")
            continue
        posx = int(input(" ingresa la posicion del eje x  "))
        if posx < 0 or posx >= 9:
            print("exedes el limite ingresa nuevamente ")
            continue
        print(f"tus cordeenadas son {posy} , {posx} ")
        input()
        Insertar(dato,matriz,posy,posx)
        break
    except ValueError:
        print("el tipo de dato no es un numero UwU")