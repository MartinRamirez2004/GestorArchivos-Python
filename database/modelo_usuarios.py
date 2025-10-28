from database.conexion import ConexionDB

class Usuario:
    def __init__(self, nombres, apellidos, correo, contraseña):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.contraseña = contraseña


class UsuarioModelo:
    @staticmethod
    def crear_usuario(usuario):
        db = ConexionDB()
        sql = "INSERT INTO usuarios (nombres, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)"
        valores = (usuario.nombres, usuario.apellidos, usuario.correo, usuario.contraseña)
        db.cursor.execute(sql, valores)
        db.conexion.commit()
        db.cerrar()
        print("Usuario creado correctamente")

    @staticmethod
    def obtener_todos():
        db = ConexionDB()
        db.cursor.execute("SELECT * FROM usuarios")
        resultado = db.cursor.fetchall()
        db.cerrar()
        return resultado
