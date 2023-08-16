from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=4, max=25)])
    ape_mat = StringField('Apellido materno', validators=[DataRequired(), Length(min=4, max=25)])
    ape_pat = StringField('Apellido paterno', validators=[DataRequired(), Length(min=4, max=25)])
    direction = StringField('Dirección', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ProfileForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=4, max=25)])
    ape_mat = StringField('Apellido materno', validators=[DataRequired(), Length(min=4, max=25)])
    ape_pat = StringField('Apellido paterno', validators=[DataRequired(), Length(min=4, max=25)])
    direction = StringField('Dirección', validators=[DataRequired()])
    submit = SubmitField('Actualizar')
