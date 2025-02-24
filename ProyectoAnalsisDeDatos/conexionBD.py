import mysql.connector

def ConexionBD():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="root",
            password="",  
            database="analisis_datos"
        )
        
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion  # Retorna la conexión para usarla en otro archivo

    except mysql.connector.Error as error:
        print(f"Error al conectar la base de datos: {error}")
        return None
