from database.modelo_usuarios import UsuarioModelo

class ControladorUsuarios:
    def __init__(self, modelo):
        self.modelo = modelo

    def registrar_usuario(self, nombres, apellidos, correo, contraseña):
        self.modelo.crear_usuario(nombres, apellidos, correo, contraseña)
