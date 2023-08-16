from random import sample
from conexionBD import *  #Importando conexion BD

#Creando una funcion para obtener la lista de carros.
def listaProyecto():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM proyect ORDER BY id_proyecto  DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def getProyectoById(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM proyect WHERE id_proyecto = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarProyecto(Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente ,id_team):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO proyect(Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente ,id_team ) VALUES (%s, %s,%s,%s,%s)")
        valores     = (Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente ,id_team)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert
  


def  recibeActualizarProyecto(Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente ,id_team,id_proyecto ):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE proyect
            SET 
               Nombre_proyecto = %s,
               Descripcion_proyecto = %s,
               Fecha_inicio = %s,
               id_cliente = %s,
               id_team = %s
            WHERE id_proyecto=%s
            """, (Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente ,id_team,id_proyecto ))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

def eliminarProyecto(id):
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
    
        cur.execute('DELETE FROM proyect WHERE id_proyecto=%s', (id,))
        conexion_MySQLdb.commit()
        resultado_eliminar = cur.rowcount #retorna 1 o 0
        return resultado_eliminar
