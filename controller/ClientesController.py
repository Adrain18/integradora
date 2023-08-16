from random import sample
from conexionBD import *  #Importando conexion BD

#Creando una funcion para obtener la lista de carros.
def listaCliente():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM client ORDER BY id_cliente DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def getClienteById(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM client WHERE id_cliente = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarCliente(Nombre_cliente, Descripcion):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO client(Nombre_cliente, Descripcion) VALUES (%s, %s)")
        valores     = (Nombre_cliente, Descripcion)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert
  


def  recibeActualizarCliente(Nombre_cliente,Descripcion,id_cliente):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE client
            SET 
               Nombre_cliente = %s,
               Descripcion = %s
            WHERE id_cliente=%s
            """, (Nombre_cliente,Descripcion,id_cliente))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

def eliminarCliente(id):
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
    
        cur.execute('DELETE FROM client WHERE id_cliente=%s', (id,))
        conexion_MySQLdb.commit()
        resultado_eliminar = cur.rowcount #retorna 1 o 0
        return resultado_eliminar
