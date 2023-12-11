import mysql.connector
from mysql.connector import Error

class DAO ():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(

                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'tienda'
            )
        except Error as ex:
            print("Error al conectar a la base de datos: {0}".format(ex))
    def listarProducto (self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM producto ORDER BY producto ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al conectar a la base de datos: {0}".format(ex))