from conexionBD import ConexionBD
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tabulate as tb 
import tkinter as tk 
from tkinter import messagebox
# Obtener la conexión
conexion = ConexionBD()
def BuscarPorID():
         # buscar fecha por id 
        try:
            id_venta = int(input("ingresa el id de la venta que deseas buscar : "))
            consulta = f"select * from ventas where id = {id_venta}"
            df = pd.read_sql(consulta, conexion)
            Consulta_tabla = tb.tabulate(df.values, headers=df.columns, tablefmt='psql')
            
            print(Consulta_tabla)
        except Exception as e:
            print(f"error en la consulta {e}")


def VentasPorPrecioConMatplotlib():
    try:
        print("Mostrando ventas por precio...")
        
        # Consulta SQL corregida
        consulta = """
        SELECT p.nombre, v.total, p.precio 
        FROM ventas v
        JOIN productos p ON p.id = v.producto_id;
        """
        
        # Cargar datos en pandas
        df = pd.read_sql(consulta, conexion)

        # Mostrar tabla con tabulate
        tabla = tb.tabulate(df.values, headers=df.columns, tablefmt='psql')
        print(tabla)


        fig, ax = plt.subplots()
        ax.plot(df["nombre"], df["precio"], marker='o', color='tab:red', label="Precio")
        ax.set_title('Ventas por Precio', loc="left", fontdict={'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_xlabel("Producto")
        ax.set_ylabel("Precio")
        ax.legend()
        
        plt.xticks(rotation=40)  
        plt.show()  # aqui muestro el grafico

    except Exception as e:
        print(f"Error en la consulta: {e}")

if conexion:
    
    query = "SELECT * FROM ventas"
    
    #Mostrar Todas las ventas (vamoh basico )
    df = pd.read_sql(query, conexion)
    tablas = tb.tabulate(df.values, headers=df.columns, tablefmt='psql')

   
    
    VentasPorPrecioConMatplotlib()
   
    
    conexion.close()
    print("Conexión cerrada")

