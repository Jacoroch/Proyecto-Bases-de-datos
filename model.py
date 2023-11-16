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

    def update_rappitendero(self, id_rappitendero, nombre, afiliado, dias_trabajados, horas_trabajadas, calificacion, telefono):
        try:
            sql = "UPDATE Rappitendero SET NombreRappitendero = %s, AfiliadosAud = %s, DiasTrabajados = %s, HorasTrabajadas = %s, Calificacion = %s, NumeroTelefono = %s WHERE idRappitendero = %s"
            val = (nombre, afiliado, dias_trabajados, horas_trabajadas, calificacion, telefono, id_rappitendero)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Rappitendero actualizado exitosamente")
        except Error as e:
            print("Error al actualizar rappitendero", e)

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
