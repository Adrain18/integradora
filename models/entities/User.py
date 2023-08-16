from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, Nombre,Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.Nombre = Nombre
        self.Ape_pat = Ape_pat
        self.Ape_mat = Ape_mat
        self.Edad = Edad
        self.GdoEstudios = GdoEstudios
        self.Direccion = Direccion
        self.Estado = Estado
        self.Municipio = Municipio
        self.Telefono = Telefono

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)