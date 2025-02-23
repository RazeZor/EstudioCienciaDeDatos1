import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import csv 

os.system("cls")

try:
    with open("Pandas/archivosCSV/transferencias_futbol_complejo.csv", mode="r", encoding="utf-8") as archivo:
        data = csv.DictReader(archivo)
        BaseDeDatos = list(data)  
        df = pd.DataFrame(BaseDeDatos)

        print("✅ Base de datos exportada correctamente a Excel.")
except Exception as e:
    print(f" Error al abrir el archivo: {e}")
    BaseDeDatos = []



def Filtrar_jugadores_por_posición(bd):
    # para hacer esto vamos a ocuipar la libreria Pandas 
    try : 
        df= pd.DataFrame(bd)
        print("buscar a lo jugadores por posicion : ")
        print("""Las posiciones que existen Son : 

                [1]  Delantero
                [2]  Extremo
                [3]  Mediocampista
                [4]  Defensa
                [5]  Portero
              
              """)
        posicion = input("escribe la posicion de el jugador y te mostramos los jugadores de esa pos : ")
        
        if not posicion:
            print("ingresa nuevamente una posicion que exista ")
        print(f"mostrando los jugadores de la posicion {posicion}")
        filtro = df[df["Posición"] == posicion]
        print(filtro)


    except Exception as e :
        print(f"ah ocurrido un error {e}")
        

def  Jugadores_con_un_salario_mayor_a_50_millones_(bd):
    try:
        df = pd.DataFrame(bd)
        print("mostrando Jugadores con salario Mayor a 50 millones ")
        df["Salario_Anual_Millones"] = pd.to_numeric(df["Salario_Anual_Millones"],errors="coerce")
        salario = df["Salario_Anual_Millones"]
        filtro = df[salario > 50]
        print(filtro)
        
    except Exception as e :
        print("error {e}")


def Ordenar_jugadores_por_valor_transferencia(df):
    print("ordenar jugadores por transferencia")
    try:
        if not df.empty:   
            df["Valor_Transferencia_Millones"] = df["Valor_Transferencia_Millones"].astype(float)
            valor = df.sort_values(by="Valor_Transferencia_Millones", ascending=False)
            filtro = valor[["Jugador", "Valor_Transferencia_Millones"]]
            print(filtro)
        else:
            print(" El DataFrame está vacío.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def Transferencias_de_un_equipo_específico(bd, equipo):
    try:    
        df = pd.DataFrame(bd) 
        transferencias = df[df["Equipo_Origen"] == equipo]

        if transferencias.empty:
            print(f" No se encontraron transferencias desde {equipo}.")
        else:
            print(f"Transferencias desde {equipo}:\n")
            print(transferencias[["Jugador", "Equipo_Destino", "Valor_Transferencia_Millones"]])
    except Exception as e:
        print(f" Error al procesar los datos: {e}")
        
try:
    equipo = input("🔍 Ingresa un equipo en específico: ")
    Transferencias_de_un_equipo_específico(BaseDeDatos, equipo)
except Exception as e:
    print(f" Error al ingresar datos: {e}")
