# user_views.py
from flask import Blueprint, render_template, redirect, url_for

from utils.file_handler import save_image

user_views = Blueprint('user', __name__)
