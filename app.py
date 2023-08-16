from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from controller.UserController import *
from controller.EquipoController import *
from controller.ClientesController import *
from controller.ContactoController import *
from controller.ProyectosController import *

from werkzeug.security import generate_password_hash
from config import config
from views.admin_views import admin_views
from views.user_views import user_views
from views.equipo_views import equipo_views
from views.clientes_views import clientes_views
from views.proyectos_views import proyectos_views

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)
app.register_blueprint(admin_views)
app.register_blueprint(user_views)
app.register_blueprint(equipo_views)
app.register_blueprint(clientes_views)
app.register_blueprint(proyectos_views)


csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'],None,None,None,None,None,None,None,None,None)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('inicio'))
            else:
                flash("Contraseña invalida")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/inicio')
@login_required
def inicio():
    return render_template('admin/inicio.html')


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


@app.route('/usuario')
@login_required
def usuario():
    return render_template('admin/usuario.html')


@app.route('/registrar-user', methods=['GET','POST'])
def addUser():
    return render_template('users/register.html')

########### CRUD USUARIOS ###########

@app.route('/usuario', methods=['POST'])
def formAddUser():
    if request.method == 'POST':
        username           = request.form['username']
        password           = request.form['password']
        Nombre             = request.form['Nombre']
        Ape_pat            = request.form['Ape_pat']
        Ape_mat            = request.form['Ape_mat']
        Edad               = request.form['Edad']
        GdoEstudios        = request.form['GdoEstudios']
        Direccion          = request.form['Direccion']
        Estado             = request.form['Estado']
        Municipio          = request.form['Municipio']
        Telefono           = request.form['Telefono']
        id_team           = request.form['id_team']
        
        password = generate_password_hash(password)
        resultData = registrarUser(username, password, Nombre,Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team)
        if(resultData ==1):
             return render_template('admin/usuario.html', miData = listaUser(), msg='El Registro fue un éxito', tipo=1)
        else:
            return render_template('admin/usuario.html', msg = 'Metodo HTTP incorrecto', tipo=1)   



@app.route('/usuario/<string:id>/update', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateUser(id)
        if resultData:
            return render_template('users/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaUser(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaUser(), msg = 'Metodo HTTP incorrecto', tipo=1)          


@app.route('/actualizar-usuario/<string:idUser>', methods=['POST'])
def  formActualizarUser(idUser):
    if request.method == 'POST':
        username           = request.form['username']
        password           = request.form['password']
        Nombre             = request.form['Nombre']
        Ape_pat            = request.form['Ape_pat']
        Ape_mat            = request.form['Ape_mat']
        Edad               = request.form['Edad']
        GdoEstudios        = request.form['GdoEstudios']
        Direccion          = request.form['Direccion']
        Estado             = request.form['Estado']
        Municipio          = request.form['Municipio']
        Telefono           = request.form['Telefono']
        id_team           = request.form['id_team']
       
        resultData = recibeActualizarUser(username, password, Nombre,Ape_pat,Ape_mat,Edad,GdoEstudios,Direccion,Estado,Municipio,Telefono,id_team,idUser)

        if(resultData ==1):
            return render_template('admin/usuario.html', miData = listaUser(), msg='Datos del carro actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('admin/usuario.html', miData = listaUser(), msg='No se pudo actualizar', tipo=1)


@app.route('/borrar-usuario/<string:id>', methods=['GET','POST'])
def formViewBorrarUsuario(id):
    if request.method == 'GET':
        resultData  = eliminarUser(id)
    
        if(resultData ==1):
            return render_template('admin/usuario.html', miData = listaUser(), msg='Registro borrado con exito', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('admin/usuario.html', miData = listaUser(), msg='No se pudo actualizar', tipo=1)



########### CRUD TEAM ########### 



@app.route('/equipo', methods=['POST'])
def formAddEquipo():
   if request.method == 'POST':
       Nombre           = request.form['Nombre']
       Descripcion      = request.form['Descripcion']
       resultData = registrarEquipo(Nombre, Descripcion)
       if(resultData ==1):
        return render_template('admin/equipo.html', miData = listaEquipo(), msg='El Registro fue un éxito', tipo=1)
       else:
        return render_template('admin/usuario.html', msg = 'Metodo HTTP incorrecto', tipo=1)  



@app.route('/registrar-equipo', methods=['GET','POST'])
def addTeam():
    return render_template('team/register.html')

@app.route('/equipo/<string:id>/update', methods=['GET','POST'])
def formViewUpdateTeam(id):
    if request.method == 'GET':
        resultData = getEquipoById(id)
        if resultData:
            return render_template('team/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaEquipo(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaEquipo(), msg = 'Metodo HTTP incorrecto', tipo=1)          


@app.route('/actualizar-equipo/<string:idTeam>', methods=['POST'])
def  formActualizarTeam(idTeam):
    if request.method == 'POST':
        Nombre           = request.form['Nombre']
        Descripcion      = request.form['Descripcion']
       
        resultData = recibeActualizarEquipo(Nombre, Descripcion,idTeam)

        if(resultData ==1):
            return render_template('admin/equipo.html', miData = listaEquipo(), msg='Datos del carro actualizados', tipo=1)
        else:
            return render_template('admin/equipo.html', miData = listaEquipo(), msg='No se pudo actualizar', tipo=1)


@app.route('/borrar-equipo/<string:id>', methods=['GET','POST'])
def formViewBorrarTeam(id):
    if request.method == 'GET':
        resultData  = eliminarEquipo(id)
    
        if(resultData ==1):
            return render_template('admin/equipo.html', miData = listaEquipo(), msg='Registro borrado con exito', tipo=1)
        else:
            return render_template('admin/equipo.html', miData = listaEquipo(), msg='No se pudo actualizar', tipo=1)



########### CRUD CLIENTES ########### 


@app.route('/clientes', methods=['POST'])
def formAddCliente():
   if request.method == 'POST':
       Nombre_cliente   = request.form['Nombre_cliente']
       Descripcion      = request.form['Descripcion']
       
       resultData = registrarCliente(Nombre_cliente, Descripcion)
       
       if(resultData ==1):
        return render_template('admin/clientes.html', miData = listaCliente(), msg='El Registro fue un éxito', tipo=1)
       else:
        return render_template('admin/clientes.html', msg = 'Metodo HTTP incorrecto', tipo=1)  



@app.route('/registrar-clientes', methods=['GET','POST'])
def addCliente():
    return render_template('clientes/register.html')

@app.route('/clientes/<string:id>/update', methods=['GET','POST'])
def formViewUpdateCliente(id):
    if request.method == 'GET':
        resultData = getClienteById(id)
        if resultData:
            return render_template('clientes/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaEquipo(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaEquipo(), msg = 'Metodo HTTP incorrecto', tipo=1)          


@app.route('/actualizar-cliente/<string:idCliente>', methods=['POST'])
def  formActualizarCliente(idCliente):
    if request.method == 'POST':
        Nombre_cliente   = request.form['Nombre_cliente']
        Descripcion      = request.form['Descripcion']
       
        resultData = recibeActualizarCliente(Nombre_cliente, Descripcion,idCliente)

        if(resultData ==1):
            return render_template('admin/clientes.html', miData = listaCliente(), msg='Datos del carro actualizados', tipo=1)
        else:
            return render_template('admin/clientes.html', miData = listaCliente(), msg='No se pudo actualizar', tipo=1)


@app.route('/borrar-cliente/<string:id>', methods=['GET','POST'])
def formViewBorrarCliente(id):
    if request.method == 'GET':
        resultData  = eliminarCliente(id)
    
        if(resultData ==1):
            return render_template('admin/clientes.html', miData = listaCliente(), msg='Registro borrado con exito', tipo=1)
        else:
            return render_template('admin/clientes.html', miData = listaCliente(), msg='No se pudo actualizar', tipo=1)

#### CRUD PROYECTOS ##############





########### CRUD CLIENTES ########### 

@app.route('/proyecto', methods=['POST'])
def formAddProyecto():
   if request.method == 'POST':
       Nombre_proyecto   = request.form['Nombre_proyecto']
       Descripcion_proyecto      = request.form['Descripcion_proyecto']
       Fecha_inicio      = request.form['Fecha_inicio']
       id_cliente       = request.form['id_cliente']
       id_team          = request.form['id_team']
       
       resultData = registrarProyecto(Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente,id_team)
       
       if(resultData ==1):
        return render_template('admin/proyectos.html', miData = listaProyecto(), msg='El Registro fue un éxito', tipo=1)
       else:
        return render_template('admin/proyectos.html', msg = 'Metodo HTTP incorrecto', tipo=1)  



@app.route('/registrar-proyecto', methods=['GET','POST'])
def addProyecto():
    return render_template('proyectos/register.html')

@app.route('/proyecto/<string:id>/update', methods=['GET','POST'])
def formViewUpdateProyecto(id):
    if request.method == 'GET':
        resultData = getProyectoById(id)
        if resultData:
            return render_template('proyectos/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaProyecto(), msg='No existe el carro', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaProyecto(), msg = 'Metodo HTTP incorrecto', tipo=1)          


@app.route('/actualizar-proyecto/<string:idProyecto>', methods=['POST'])
def  formActualizarProyecto(idProyecto):
    if request.method == 'POST':
       Nombre_proyecto   = request.form['Nombre_proyecto']
       Descripcion_proyecto      = request.form['Descripcion_proyecto']
       Fecha_inicio      = request.form['Fecha_inicio']
       id_cliente       = request.form['id_cliente']
       id_team          = request.form['id_team']
       
       resultData = recibeActualizarProyecto(Nombre_proyecto, Descripcion_proyecto,Fecha_inicio,id_cliente,id_team,idProyecto)

       if(resultData ==1):
            return render_template('admin/proyectos.html', miData = listaProyecto(), msg='Datos del carro actualizados', tipo=1)
       else:
            return render_template('admin/proyectos.html', miData = listaProyecto(), msg='No se pudo actualizar', tipo=1)


@app.route('/borrar-proyecto/<string:id>', methods=['GET','POST'])
def formViewBorrarProyecto(id):
    if request.method == 'GET':
        resultData  = eliminarProyecto(id)
    
        if(resultData ==1):
            return render_template('admin/proyectos.html', miData = listaProyecto(), msg='Registro borrado con exito', tipo=1)
        else:
            return render_template('admin/proyectos.html', miData = listaProyecto(), msg='No se pudo actualizar', tipo=1)



##### FORM CONTACTO #######


@app.route('/contact', methods=['POST'])
def formAddContact():
   if request.method == 'POST':
       Nombre   = request.form['Nombre']
       Correo      = request.form['Correo']
       Asunto      = request.form['Asunto']
       Mensaje      = request.form['Mensaje']
       
       registrarContacto(Nombre, Correo,Asunto,Mensaje)
       return render_template('admin/contacto.html', miData = listaEquipo(), msg='El Registro fue un éxito', tipo=1)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()