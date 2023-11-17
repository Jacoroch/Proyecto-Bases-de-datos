import tkinter as tk
from model import RappitenderoModel
from view import RappitenderoView
from controller import RappitenderoController

def main():
    root = tk.Tk()
    model = RappitenderoModel('localhost', 'root', 'CONTRASENA.', 'rappi2')  
    view = RappitenderoView(root, None)  # Inicialmente pasamos None para el controlador
    controller = RappitenderoController(view, model)
    view.controller = controller  # Ahora establecemos el controlador en la vista
    root.mainloop()

if __name__ == "__main__":
    main()
