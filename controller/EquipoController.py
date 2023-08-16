from random import sample
from conexionBD import *  #Importando conexion BD

#Creando una funcion para obtener la lista de carros.
def listaEquipo():
    print("entro aqui")
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM team ORDER BY id_team DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def getEquipoById(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM team WHERE id_team = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarEquipo(Nombre, Descripcion):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO team(Nombre, Descripcion) VALUES (%s, %s)")
        valores     = (Nombre, Descripcion)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert
  


def  recibeActualizarEquipo(Nombre, Descripcion,id_team):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE team
            SET 
               Nombre = %s,
               Descripcion = %s
            WHERE id_team=%s
            """, (Nombre, Descripcion,id_team))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

def eliminarEquipo(id):
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
    
        cur.execute('DELETE FROM team WHERE id_team=%s', (id,))
        conexion_MySQLdb.commit()
        resultado_eliminar = cur.rowcount #retorna 1 o 0
        return resultado_eliminar
