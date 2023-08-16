from .entities.User import User
from conexionBD import * 

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono FROM user 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, password, Nombre, Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1],None, row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        