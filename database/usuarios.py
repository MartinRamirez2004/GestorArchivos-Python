#Importacion de la funcion conexion_bd desde el archivo conexion.py para uso en usuarios.py
from database.conexion import conexion_bd
from tkinter import messagebox

class UsuarioDB:
    def __init__(self):
        self.conexion = conexion_bd()
        if self.conexion:
            self.cursor = self.conexion.cursor()
        else:
            messagebox.showerror("Error", "Imposible conectar con la base de datos.")

    # Metodo para la creacion de un usuario
    def crear_usuario(self, nombres, apellidos, correo, contraseña):
        try:
            sql = "INSERT INTO usuarios (nombres, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)"
            valores = (nombres, apellidos, correo, contraseña)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            messagebox.showinfo("Éxito", "✅ Usuario registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ No se pudo registrar el usuario:\n{e}")

    # 🔹 Leer todos los usuarios
    def obtener_usuarios(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"❌ No se pudieron obtener los usuarios:\n{e}")
            return []

    # 🔹 Actualizar usuario
    def actualizar_usuario(self, id_usuario, nombres, apellidos, correo, contraseña):
        try:
            sql = """UPDATE usuarios 
                     SET nombres=%s, apellidos=%s, correo=%s, contraseña=%s 
                     WHERE id=%s"""
            valores = (nombres, apellidos, correo, contraseña, id_usuario)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            messagebox.showinfo("Éxito", "✅ Usuario actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ No se pudo actualizar el usuario:\n{e}")

    # 🔹 Eliminar usuario
    def eliminar_usuario(self, id_usuario):
        try:
            sql = "DELETE FROM usuarios WHERE id = %s"
            self.cursor.execute(sql, (id_usuario,))
            self.conexion.commit()
            messagebox.showinfo("Éxito", "✅ Usuario eliminado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ No se pudo eliminar el usuario:\n{e}")

    # 🔹 Cerrar conexión
    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
