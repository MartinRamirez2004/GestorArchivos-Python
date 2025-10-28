import tkinter as tk
from tkinter import messagebox

class VentanaUsuarios:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Gestión de Usuarios")

        # Campos de entrada
        tk.Label(root, text="Nombres:").grid(row=0, column=0)
        self.entry_nombres = tk.Entry(root)
        self.entry_nombres.grid(row=0, column=1)

        tk.Label(root, text="Apellidos:").grid(row=1, column=0)
        self.entry_apellidos = tk.Entry(root)
        self.entry_apellidos.grid(row=1, column=1)

        tk.Label(root, text="Correo:").grid(row=2, column=0)
        self.entry_correo = tk.Entry(root)
        self.entry_correo.grid(row=2, column=1)

        tk.Label(root, text="Contraseña:").grid(row=3, column=0)
        self.entry_contraseña = tk.Entry(root, show="*")
        self.entry_contraseña.grid(row=3, column=1)

        tk.Button(root, text="Registrar", command=self.registrar).grid(row=4, column=0, columnspan=2)

    def registrar(self):
        nombres = self.entry_nombres.get()
        apellidos = self.entry_apellidos.get()
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()

        self.controlador.registrar_usuario(nombres, apellidos, correo, contraseña)
        messagebox.showinfo("Éxito", "Usuario registrado con éxito")
