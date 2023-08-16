from random import sample
from conexionBD import *  #Importando conexion BD

#Creando una funcion para obtener la lista de carros.
def listaUser():
    print("entro aqui")
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM user ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateUser(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM user WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarUser(username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO user(username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
        valores     = (username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        return resultado_insert
  


def  recibeActualizarUser(username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team,id):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE user
            SET 
               username     = %s,
               password     = %s,
               Nombre       = %s,
               Ape_pat      = %s,
               Ape_mat      = %s,
               Edad         = %s,
               GdoEstudios  = %s,
               Direccion    = %s,
               Estado       = %s,
               Municipio    = %s,
               Telefono     = %s,
               id_team     = %s
            WHERE id=%s
            """, (username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team,id))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

def eliminarUser(id):
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
    
        cur.execute('DELETE FROM user WHERE id=%s', (id,))
        conexion_MySQLdb.commit()
        resultado_eliminar = cur.rowcount #retorna 1 o 0
        return resultado_eliminar

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio