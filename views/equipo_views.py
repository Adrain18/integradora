from flask import Blueprint, render_template, redirect, url_for

from utils.file_handler import save_image

equipo_views = Blueprint('equipo', __name__)
