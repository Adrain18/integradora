from flask import Blueprint, render_template, redirect, url_for

from utils.file_handler import save_image

clientes_views = Blueprint('clientes', __name__)
