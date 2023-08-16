from flask import Blueprint, render_template, redirect, url_for

from utils.file_handler import save_image

proyectos_views = Blueprint('proyectos', __name__)
