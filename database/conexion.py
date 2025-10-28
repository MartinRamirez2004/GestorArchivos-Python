import mysql.connector

class ConexionDB:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pythonapp"
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a MySQL")
        except mysql.connector.Error as err:
            print(f'Error al conectar a la base de datos: {err}')

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
