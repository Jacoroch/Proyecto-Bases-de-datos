class RappitenderoController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.create_rappitendero = self.create_rappitendero

    def create_rappitendero(self, nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono):
        # Obtiene los valores de los campos de entrada
        nombre = self.view.entry_nombre.get()
        afiliado_salud = self.view.entry_afiliado_salud.get()
        dias_trabajados = self.view.entry_dias_trabajados.get()
        horas_trabajadas = self.view.entry_horas_trabajadas.get()
        calificacion = self.view.entry_calificacion.get()
        telefono = self.view.entry_telefono.get()

        # Aquí puedes agregar validaciones para los datos

        # Llama al método del modelo para crear el Rappitendero
        try:
            # Asegúrate de convertir los valores a los tipos adecuados, si es necesario
            self.model.create_rappitendero(nombre, afiliado_salud, int(dias_trabajados), int(horas_trabajadas), int(calificacion), telefono)
            self.view.show_message("Rappitendero creado exitosamente")
        except Exception as e:
            self.view.show_message("Error al crear rappitendero: " + str(e))
    
    def delete_rappitendero(self, id_rappitendero):
        try:
            self.model.delete_rappitendero(id_rappitendero)
        except Exception as e:
            raise e
    
    
    def get_all_rappitenderos(self):
        try:
            rappitenderos = self.model.read_rappitenderos()
            return rappitenderos
        except Exception as e:
            raise e  # Puedes manejar el error aquí o simplemente pasarlo al método llamador

    
    def buscar_rappitendero(self, nombre):
        try:
            resultados = self.model.buscar_rappitendero_por_nombre(nombre)
            if resultados:
                # Aquí podrías llamar a una función de la vista que muestre los resultados
                self.view.show_search_results(resultados)
            else:
                self.view.show_message("Rappitendero no encontrado.")
        except Exception as e:
            self.view.show_message(f"Error al buscar rappitendero: {e}")

    def update_rappitendero(self, id_to_update, nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono):
        self.model.update_rappitendero(id_to_update, nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono)


    def delete_rappitendero(self, id_rappitendero):
        try:
            self.model.delete_rappitendero(id_rappitendero)
            self.view.show_message("Rappitendero eliminado exitosamente")
        except Exception as e:
            self.view.show_message(f"Error al eliminar rappitendero: {e}")
