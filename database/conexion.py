#Importacion a la libreria de MySQL
import mysql.connector as mysql

#Funcion encargada de la conexion a la base de datos
def conexion_bd():
    try:

        #Seccion encargada a la conexion de la base de datos
        conexion = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="pythonapp"
        )
        #Imprimira si la conexion fue exitosa
        print("Conexion exitosa")
        return conexion

    #En caso de errores 
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos local")
        print(error)
        return None

conexion_bd()