import tkinter as tk
from app.controlador_usuarios import ControladorUsuarios
from database.modelo_usuarios import UsuarioModelo
from interfaces.vista_usuarios import VentanaUsuarios

if __name__ == "__main__":
    root = tk.Tk()

    modelo = UsuarioModelo()
    controlador = ControladorUsuarios(modelo)
    vista = VentanaUsuarios(root, controlador)

    root.mainloop()
