import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog



class RappitenderoView:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master
        self.master.title('Gestión de Rappitenderos')

        # Widgets para crear un Rappitendero
        self.label_nombre = tk.Label(master, text="Nombre del Rappitendero")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.label_afiliado_salud = tk.Label(master, text="Afiliado a Salud")
        self.label_afiliado_salud.pack()
        self.entry_afiliado_salud = tk.Entry(master)
        self.entry_afiliado_salud.pack()

        self.label_dias_trabajados = tk.Label(master, text="Días Trabajados")
        self.label_dias_trabajados.pack()
        self.entry_dias_trabajados = tk.Entry(master)
        self.entry_dias_trabajados.pack()

        self.label_horas_trabajadas = tk.Label(master, text="Horas Trabajadas")
        self.label_horas_trabajadas.pack()
        self.entry_horas_trabajadas = tk.Entry(master)
        self.entry_horas_trabajadas.pack()

        self.label_calificacion = tk.Label(master, text="Calificación")
        self.label_calificacion.pack()
        self.entry_calificacion = tk.Entry(master)
        self.entry_calificacion.pack()

        self.label_telefono = tk.Label(master, text="Número Telefónico")
        self.label_telefono.pack()
        self.entry_telefono = tk.Entry(master)
        self.entry_telefono.pack()

        self.button_create = tk.Button(master, text="Crear Rappitendero", command=self._on_create)
        self.button_create.pack()

        # Widgets para buscar un Rappitendero
        self.label_buscar = tk.Label(master, text="Buscar Rappitendero por Nombre")
        self.label_buscar.pack()
        self.entry_buscar = tk.Entry(master)
        self.entry_buscar.pack()

        self.button_buscar = tk.Button(master, text="Buscar", command=self._on_buscar)
        self.button_buscar.pack()
        
        # Widget para mostrar todos los rappitenderos
        self.button_mostrar_rappitenderos = tk.Button(master, text="Mostrar todos los Rappitenderos", command=self._on_mostrar_rappitenderos)
        self.button_mostrar_rappitenderos.pack()
        
        #eliminar
        self.button_eliminar_rappitendero = tk.Button(master, text="Eliminar Rappitendero", command=self._on_eliminar_rappitendero)
        self.button_eliminar_rappitendero.pack()
        #actualizar
        self.update_button = tk.Button(master, text="Actualizar Rappitendero", command=self.update_rappitendero)
        self.update_button.pack()

    def _on_create(self):
        # Este método se activa cuando se presiona el botón Crear Rappitendero
        nombre = self.entry_nombre.get()
        afiliado_salud = self.entry_afiliado_salud.get()
        dias_trabajados = self.entry_dias_trabajados.get()
        horas_trabajadas = self.entry_horas_trabajadas.get()
        calificacion = self.entry_calificacion.get()
        telefono = self.entry_telefono.get()
        self.controller.create_rappitendero(nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono)
        
    def _on_eliminar_rappitendero(self):
        try:
            # Solicitar al usuario el ID del Rappitendero a eliminar
            id_rappitendero = self.pedir_id()

            if id_rappitendero is not None:
                # Llama al método del controlador para eliminar el Rappitendero
                self.controller.delete_rappitendero(id_rappitendero)
                self.show_message("Rappitendero eliminado exitosamente")
        except Exception as e:
            self.show_message("Error al eliminar Rappitendero: " + str(e))
    
    
    def pedir_id(self):
        # Utiliza un cuadro de diálogo de entrada de datos para que el usuario ingrese el ID
        id_rappitendero = simpledialog.askinteger("Eliminar Rappitendero", "Ingrese el ID del Rappitendero a eliminar:")
        return id_rappitendero

    
    def _on_mostrar_rappitenderos(self):
        try:
            # Llama al método del controlador para obtener la lista de rappitenderos
            rappitenderos = self.controller.get_all_rappitenderos()

            # Formatea la lista de rappitenderos como una cadena
            rappitenderos_str = "\n".join(str(r) for r in rappitenderos)

            # Muestra la lista en una ventana emergente
            self.show_message("Lista de Rappitenderos:\n" + rappitenderos_str)
        except Exception as e:
            self.show_message("Error al mostrar la lista de rappitenderos: " + str(e))

    def _on_buscar(self):
        # Este método se activa cuando se presiona el botón Buscar
        nombre_busqueda = self.entry_buscar.get()
        self.controller.buscar_rappitendero(nombre_busqueda)
        
    def update_rappitendero(self):
        id_to_update = simpledialog.askstring("Actualizar Rappitendero", "Ingrese el ID del Rappitendero a actualizar")
        if id_to_update:
            # Solicitar los nuevos valores para los campos
            nombre = simpledialog.askstring("Actualizar Rappitendero", "Nuevo nombre:")
            afiliado_salud = simpledialog.askstring("Actualizar Rappitendero", "Nuevo poliza de salud:")
            dias_trabajados = simpledialog.askinteger("Actualizar Rappitendero", "Nuevos días trabajados:")
            horas_trabajadas = simpledialog.askinteger("Actualizar Rappitendero", "Nuevas horas trabajadas:")
            calificacion = simpledialog.askfloat("Actualizar Rappitendero", "Nueva calificación:")
            telefono = simpledialog.askstring("Actualizar Rappitendero", "Nuevo teléfono:")

            # Llamar al controlador para actualizar
            self.controller.update_rappitendero(id_to_update, nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono)

    def show_message(self, message):
        messagebox.showinfo("Información", message)

    def show_search_results(self, resultados):
        result_string = "\n".join(str(resultado) for resultado in resultados)
        messagebox.showinfo("Resultados de Búsqueda", result_string)
