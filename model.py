import mysql.connector
from mysql.connector import Error

class RappitenderoModel:
    def __init__(self, host, user, passwd, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=passwd,
                database=database
            )
            self.cursor = self.connection.cursor(buffered=True)  # Crear el cursor aquí y mantenerlo
        except Error as e:
            print("Error al conectar a MySQL", e)

    def create_rappitendero(self, nombre, afiliado, dias_trabajados, horas_trabajadas, calificacion, telefono):
        try:
            sql = "INSERT INTO Rappitendero (NombreRappitendero, AfiliadoSalud, DiasTrabajados, HorasTrabajadas, Calificacion, NumeroTelefonico) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (nombre, afiliado, dias_trabajados, horas_trabajadas, calificacion, telefono)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Rappitendero creado exitosamente")
        except Error as e:
            print("Error al crear rappitendero", e)

    def read_rappitenderos(self):
        try:
            self.cursor.execute("SELECT * FROM Rappitendero")
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print("Error al leer rappitenderos", e)

    def update_rappitendero(self, id, nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono):
        try:
            query = f"UPDATE rappitendero SET NombreRappitendero=%s, AfiliadoSalud=%s, DiasTrabajados=%s, HorasTrabajadas=%s, Calificacion=%s, NumeroTelefonico=%s WHERE idRappitendero=%s"
            values = (nombre, afiliado_salud, dias_trabajados, horas_trabajadas, calificacion, telefono, id)
            self.cursor.execute(query, values)
            self.connection.commit()
        except Error as e:
            print("Error al actualizar el Rappitendero", e)

    def delete_rappitendero(self, id_rappitendero):
        try:
            sql = "DELETE FROM Rappitendero WHERE idRappitendero = %s"
            val = (id_rappitendero,)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Rappitendero eliminado exitosamente")
        except Error as e:
            print("Error al eliminar rappitendero", e)
            
    def buscar_rappitendero_por_nombre(self, nombre):
        try:
            self.cursor.execute("SELECT * FROM Rappitendero WHERE NombreRappitendero = %s", (nombre,))
            return self.cursor.fetchall()
        except Error as e:
            print("Error al buscar rappitendero", e)
