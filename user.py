import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

class UsuarioModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='PASSWORD',
            database='rappi2'
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, data=None):
        self.cursor.execute(query, data)
        self.conn.commit()

    def fetch_all(self, query, *args):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

class UsuarioView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Gestión de Usuarios")

        root.grid_columnconfigure(0, weight=1)

        # Labels y Entries para la creación de un usuario
        self.label_nombre = ttk.Label(root, text="Nombre:")
        self.label_tipo_cliente = ttk.Label(root, text="Tipo Cliente:")
        self.label_fecha_nac = ttk.Label(root, text="Fecha Nacimiento:")
        self.label_contrasena = ttk.Label(root, text="Contraseña:")
        self.label_email = ttk.Label(root, text="Email:")
        self.label_direccion = ttk.Label(root, text="Dirección:")

        self.entry_nombre = ttk.Entry(root)
        self.entry_tipo_cliente = ttk.Entry(root)
        self.entry_fecha_nac = ttk.Entry(root)
        self.entry_contrasena = ttk.Entry(root, show="*")
        self.entry_email = ttk.Entry(root)
        self.entry_direccion = ttk.Entry(root)

        # Botones para las acciones CRUD
        self.btn_crear = ttk.Button(root, text="Crear", command=controller.crear_usuario)
        self.btn_buscar = ttk.Button(root, text="Buscar", command=controller.buscar_usuario)
        self.btn_actualizar = ttk.Button(root, text="Actualizar", command=controller.actualizar_usuario)
        self.btn_mostrar = ttk.Button(root, text="Mostrar Listado", command=controller.mostrar_todos_usuarios)
        self.btn_eliminar = ttk.Button(root, text="Eliminar", command=controller.eliminar_usuario)

        # Organización de los widgets en la interfaz
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre.grid(row=1, column=0, padx=20, pady=2)
        self.label_tipo_cliente.grid(row=2, column=0)
        self.entry_tipo_cliente.grid(row=3, column=0, padx=20, pady=2)
        self.label_fecha_nac.grid(row=4, column=0)
        self.entry_fecha_nac.grid(row=5, column=0, padx=20, pady=2)
        self.label_contrasena.grid(row=6, column=0)
        self.entry_contrasena.grid(row=7, column=0, padx=20, pady=2)
        self.label_email.grid(row=8, column=0)
        self.entry_email.grid(row=9, column=0, padx=20, pady=2)
        self.label_direccion.grid(row=10, column=0)
        self.entry_direccion.grid(row=11, column=0, padx=20, pady=2)

        self.btn_crear.grid(row=12, column=0, pady=5)

        # Label y Entry para buscar usuario por nombre
        self.label_buscar = ttk.Label(root, text="Buscar Usuario por Nombre:")
        self.entry_buscar = ttk.Entry(root)
        self.label_buscar.grid(row=13, column=0)
        self.entry_buscar.grid(row=14, column=0, padx=20, pady=2)
        self.btn_buscar.grid(row=15, column=0, pady=5)

        # Botones para las demás acciones de CRUD
        self.btn_actualizar.grid(row=16, column=0, pady=5)
        self.btn_mostrar.grid(row=17, column=0, pady=5)
        self.btn_eliminar.grid(row=18, column=0, pady=5)

        # Ajustar el ancho de las columnas para que los widgets se expandan y se centren
        for i in range(0, 19):
            root.grid_rowconfigure(i, weight=1)
            
    def obtener_datos_para_actualizar(self, id_o_nombre ):
        self.id_o_nombre_para_actualizar = id_o_nombre  # Almacenamos el ID para usarlo después
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Usuario")

        # Crea y organiza los widgets en la ventana emergente
        tk.Label(self.update_window, text="Nuevo Nombre:").grid(row=0, column=0)
        self.entry_update_nombre = ttk.Entry(self.update_window)
        self.entry_update_nombre.grid(row=0, column=1)

        tk.Label(self.update_window, text="Nuevo Tipo Cliente:").grid(row=1, column=0)
        self.entry_update_tipo_cliente = ttk.Entry(self.update_window)
        self.entry_update_tipo_cliente.grid(row=1, column=1)

        tk.Label(self.update_window, text="Nueva Fecha Nacimiento:").grid(row=2, column=0)
        self.entry_update_fecha_nac = ttk.Entry(self.update_window)
        self.entry_update_fecha_nac.grid(row=2, column=1)

        tk.Label(self.update_window, text="Nueva Contraseña:").grid(row=3, column=0)
        self.entry_update_contrasena = ttk.Entry(self.update_window, show="*")
        self.entry_update_contrasena.grid(row=3, column=1)

        tk.Label(self.update_window, text="Nuevo Email:").grid(row=4, column=0)
        self.entry_update_email = ttk.Entry(self.update_window)
        self.entry_update_email.grid(row=4, column=1)

        tk.Label(self.update_window, text="Nueva Dirección:").grid(row=5, column=0)
        self.entry_update_direccion = ttk.Entry(self.update_window)
        self.entry_update_direccion.grid(row=5, column=1)

        # Botón para confirmar la actualización
        ttk.Button(self.update_window, text="Actualizar Datos", command=self.confirmar_actualizacion).grid(row=6, column=0, columnspan=2)

    def confirmar_actualizacion(self):
        nuevo_nombre = self.entry_update_nombre.get()
        nuevo_tipo_cliente = self.entry_update_tipo_cliente.get()
        nueva_fecha_nac = self.entry_update_fecha_nac.get()
        nueva_contrasena = self.entry_update_contrasena.get()
        nuevo_email = self.entry_update_email.get()
        nueva_direccion = self.entry_update_direccion.get()

        # Llama al método del controlador para actualizar los datos del usuario
        self.controller.actualizar_datos_usuario(
            self.id_o_nombre_para_actualizar,
            nuevo_nombre,
            nuevo_tipo_cliente,
            nueva_fecha_nac,
            nueva_contrasena,
            nuevo_email,
            nueva_direccion)
        self.update_window.destroy()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Mensaje", mensaje)

    def mostrar_listado(self, usuarios):
        listado_window = tk.Toplevel(self.root)
        listado_window.title("Listado de Usuarios")
        
        # Configuración de la barra de desplazamiento
        scrollbar = ttk.Scrollbar(listado_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Creación del Listbox con la barra de desplazamiento
        listbox = tk.Listbox(listado_window, yscrollcommand=scrollbar.set)
        
        # Establecer el ancho del Listbox más grande para adaptarse al contenido
        # Este es un valor estimado, ajusta según sea necesario
        listbox.config(width=50)
        
        # Empaquetar el Listbox después de configurar la barra de desplazamiento
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configurar la barra de desplazamiento para que se mueva con el Listbox
        scrollbar.config(command=listbox.yview)

        # Insertar usuarios en el Listbox
        for usuario in usuarios:
            listbox.insert(tk.END, usuario)

        # Configurar el tamaño de la ventana emergente al tamaño del contenido o al tamaño máximo deseado
        listado_window.geometry("")

    def obtener_nombre_o_id(self, operacion):
        return simpledialog.askstring(f"{operacion} Usuario", f"Ingrese el ID del usuario que desea {operacion.lower()}:")

    def obtener_id_para_eliminar(self):
        return self.obtener_nombre_o_id("Eliminar")

class UsuarioController:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view

    def set_view(self, view):
        self.view = view
        self.view.controller = self

    def crear_usuario(self):
        nombre = self.view.entry_nombre.get()
        tipo_cliente = self.view.entry_tipo_cliente.get()  # Corregido de entry_tipo a entry_tipo_cliente
        fecha_nac = self.view.entry_fecha_nac.get()
        contrasena = self.view.entry_contrasena.get()
        email = self.view.entry_email.get()
        direccion = self.view.entry_direccion.get()

        query = "INSERT INTO usuario (NombreUsuario, TipoCliente, FechaNacimiento, Contraseña, Email, Direccion) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (nombre, tipo_cliente, fecha_nac, contrasena, email, direccion)
        
        try:
            self.model.execute_query(query, data)
            self.view.mostrar_mensaje("Usuario creado correctamente")
        except Exception as e:
            self.view.mostrar_mensaje(f"Error al crear el usuario: {e}")
            
    def buscar_usuario(self):
        nombre = self.view.entry_nombre.get()
        query = "SELECT * FROM usuario WHERE NombreUsuario = %s"
        data = (nombre,)
        try:
            usuarios = self.model.fetch_all(query, *data)
            self.view.mostrar_listado(usuarios)
        except Exception as e:
            self.view.mostrar_mensaje(f"Error al buscar el usuario: {e}")
            
    def actualizar_datos_usuario(self, id_o_nombre, nombre, tipo_cliente, fecha_nac, contrasena, email, direccion):
        query = """
            UPDATE usuario
            SET NombreUsuario = %s, TipoCliente = %s, FechaNacimiento = %s, Contraseña = %s, Email = %s, Direccion = %s
            WHERE idUsuario = %s
        """
        data = (nombre, tipo_cliente, fecha_nac, contrasena, email, direccion, id_o_nombre)
        
        try:
            self.model.execute_query(query, data)
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el usuario: {e}")
            
    def actualizar_usuario(self):
        id_o_nombre = self.view.obtener_nombre_o_id("Actualizar")
        if id_o_nombre:
            self.view.obtener_datos_para_actualizar(id_o_nombre)
            
    def mostrar_todos_usuarios(self):
        query = "SELECT * FROM usuario"
        try:
            usuarios = self.model.fetch_all(query)
            self.view.mostrar_listado(usuarios)
        except Exception as e:
            self.view.mostrar_mensaje(f"Error al mostrar los usuarios: {e}")

    def eliminar_usuario(self):
        id_o_nombre = self.view.obtener_id_para_eliminar()
        if id_o_nombre:
            query = "DELETE FROM usuario WHERE idUsuario = %s OR NombreUsuario = %s"
            data = (id_o_nombre, id_o_nombre)
            
            try:
                self.model.execute_query(query, data)
                self.view.mostrar_mensaje("Usuario eliminado correctamente")
            except Exception as e:
                self.view.mostrar_mensaje(f"Error al eliminar el usuario: {e}")

def main():
    root = tk.Tk()
    model = UsuarioModel()
    controller = UsuarioController(root, model, None) 
    view = UsuarioView(root, controller)  
    controller.set_view(view) 
    root.mainloop()


if __name__ == "__main__":
    main()
