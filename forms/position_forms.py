from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name_position = StringField('Nombre del puesto', validators=[DataRequired(), Length(min=4, max=25)])
    machinery_in_use = StringField('Maquinaria a cargo', validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField('Registrar')

class ProfileForm(FlaskForm):
    name_position = StringField('Nombre del puesto', validators=[DataRequired(), Length(min=4, max=25)])
    machinery_in_use = StringField('Maquinaria a cargo', validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField('Actualizar')
