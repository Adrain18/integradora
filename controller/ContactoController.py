from random import sample
from conexionBD import *  #Importando conexion BD




def registrarContacto(Nombre, Correo,Asunto,Mensaje):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO contact(Nombre, Correo,Asunto,Mensaje) VALUES (%s, %s,%s,%s)")
        valores     = (Nombre, Correo,Asunto,Mensaje)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert
  