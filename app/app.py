import tkinter as tk
from tkinter import ttk
from database.usuarios import UsuarioDB

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Usuarios")
root.geometry("800x600")
root.resizable(True, True)

# Instancia de la base de datos
db = UsuarioDB()

# Etiquetas y campos de entrada
tk.Label(root, text="Nombres:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, text="Apellidos:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, text="Correo:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, text="Contraseña:").grid(row=3, column=0, padx=10, pady=10, sticky="e")

nombres = tk.Entry(root, width=40)
apellidos = tk.Entry(root, width=40)
correo = tk.Entry(root, width=40)
contraseña = tk.Entry(root, width=40, show="*")

nombres.grid(row=0, column=1, padx=10, pady=10)
apellidos.grid(row=1, column=1, padx=10, pady=10)
correo.grid(row=2, column=1, padx=10, pady=10)
contraseña.grid(row=3, column=1, padx=10, pady=10)

# Función para registrar usuario
def registrar_usuario():
    if nombres.get() and apellidos.get() and correo.get() and contraseña.get():
        db.crear_usuario(nombres.get(), apellidos.get(), correo.get(), contraseña.get())
        limpiar_campos()
        mostrar_usuarios()
    else:
        tk.messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

# Función para limpiar campos
def limpiar_campos():
    nombres.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    correo.delete(0, tk.END)
    contraseña.delete(0, tk.END)

# Función para mostrar los usuarios en una tabla
def mostrar_usuarios():
    for fila in tree.get_children():
        tree.delete(fila)
    usuarios = db.obtener_usuarios()
    for usuario in usuarios:
        tree.insert("", "end", values=usuario)

# Tabla para visualizar usuarios
tree = ttk.Treeview(root, columns=("ID", "Nombres", "Apellidos", "Correo", "Contraseña"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombres", text="Nombres")
tree.heading("Apellidos", text="Apellidos")
tree.heading("Correo", text="Correo")
tree.heading("Contraseña", text="Contraseña")
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Botón para registrar usuario
btn_registrar = tk.Button(root, text="Registrar Usuario", command=registrar_usuario, bg="#4CAF50", fg="white", width=20)
btn_registrar.grid(row=4, column=0, columnspan=2, pady=10)

# Cargar usuarios al inicio
mostrar_usuarios()

root.mainloop()
