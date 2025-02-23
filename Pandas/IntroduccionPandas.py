import csv
import pandas as pd # importar por pip 
import os
from tabulate import tabulate # importar por pip 

os.system("cls")


try:
    with open("Pandas/transferencias_futbol.csv", mode="r", encoding="utf-8") as archivo:
        data = csv.DictReader(archivo)
        archivo_enlistado = list(data)  
except FileNotFoundError:
    print("El archivo no fue encontrado. Verifica la ruta.")
    archivo_enlistado = []  


def MostrarArchivos(archivo):
    for datos in archivo:
        print(datos)


def CrearTablaPandas(archivo):
    try:
        if archivo:
            df = pd.DataFrame(archivo)  
            print(df.head())  # esto era lo que me faltaba
        else:
            print("No hay datos para mostrar.")
    except:
        print("ah ocurrido un error inesperado ")


#Filtrar transferencias de un jugador
def FiltrarTransferencia(archivo):
    try:
        if archivo:
            df = pd.DataFrame(archivo)  
            #Se usa mucho para explorar los datos cuando trabajamos con CSV o bases de datos.
            print("mostrando Transderencia Solo de Messi ")
            print(df[df["Jugador"] == "Lionel Messi"])

        else:
            print("No hay datos para mostrar.")
    except:
        print("ah ocurrido un error inesperado ")
        

def OrdenarPorPrecioTransferencia(archivo):
    try:
        if archivo:
            df = pd.DataFrame(archivo)

            # Convertir a numérico
            df["Valor_Transferencia_Millones"] = pd.to_numeric(df["Valor_Transferencia_Millones"], errors='coerce')

            # Ordenar
            ordenado = df.sort_values(by="Valor_Transferencia_Millones", ascending=False)

            # Mostrar tabla formateada
            print(tabulate(ordenado, headers="keys", tablefmt="fancy_grid"))  
    except Exception as e:
        print(f"Ocurrió un error: {e}")



def OrdenarPorPrecioMenoraMayorTransferencia(archivo):
    try: 
        if archivo:
            df = pd.DataFrame(archivo)

            #el pd.to_numeric supongo que ayuda a pasar todos los datos a numeros apra evitar conflictos 
            # importante el uso de esta funcion para evitar siempre errores. 
            df["Valor_Transferencia_Millones"] = pd.to_numeric(df["Valor_Transferencia_Millones"], errors='coerce')
            ordenadoMayorAMenor = df.sort_values(by="Valor_Transferencia_Millones", ascending=True)

            print(ordenadoMayorAMenor["Valor_Transferencia_Millones"])
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
        
def OrdenarPorPrecioTransferenciaExcel(archivo):
    try:
        if archivo:
            df = pd.DataFrame(archivo)

            # Convertir la columna de precios a numérico
            df["Valor_Transferencia_Millones"] = pd.to_numeric(df["Valor_Transferencia_Millones"], errors='coerce')

            # Ordenar de mayor a menor
            ordenado = df.sort_values(by="Valor_Transferencia_Millones", ascending=False)

            # Guardar en Excel
            ordenado.to_excel("transferencias_ordenadas.xlsx", index=False)

            print("✅ Archivo Excel guardado correctamente como 'transferencias_ordenadas.xlsx'")
    except Exception as e:
        print(f"⚠️ Ocurrió un error: {e}")






