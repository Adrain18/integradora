from flask import Blueprint, render_template
from controller.UserController import *
from controller.EquipoController import *
from controller.ClientesController import *
from controller.ProyectosController import *

from flask_login import LoginManager, login_user, logout_user, login_required
admin_views = Blueprint('admin', __name__)



@admin_views.route('/inicio/')
@login_required
def inicio():
    return render_template('admin/inicio.html')

@admin_views.route('/usuario')
@login_required
def usuario():
    return render_template('admin/usuario.html', miData = listaUser())


@admin_views.route('/equipo')
@login_required
def equipo():
    return render_template('admin/equipo.html', miData = listaEquipo())

@admin_views.route('/clientes')
@login_required
def clientes():
    return render_template('admin/clientes.html', miData = listaCliente())


@admin_views.route('/contacto')
@login_required
def contacto():
    return render_template('admin/contacto.html')

@admin_views.route('/nosotros')
@login_required
def nosotros():
    return render_template('admin/nosotros.html')

@admin_views.route('/proyectos')
@login_required
def proyectos():
    return render_template('admin/proyectos.html', miData = listaProyecto())