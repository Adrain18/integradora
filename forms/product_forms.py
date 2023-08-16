from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name_product = StringField('Nombre del producto', validators=[DataRequired(), Length(min=4, max=25)])
    id_material = SelectField('Material', coerce=int, validators=[DataRequired()], choices=[])
    size = StringField('Talla', validators=[DataRequired()])
    price = IntegerField('Precio', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class ProfileForm(FlaskForm):
    name_product = StringField('Nombre del producto', validators=[DataRequired(), Length(min=4, max=25)])
    id_material = SelectField('Material', coerce=int, validators=[DataRequired()], choices=[])
    size = SelectField('Talla', coerce=int, validators=[DataRequired()], choices=[])
    price = IntegerField('Precio', validators=[DataRequired()])
    submit = SubmitField('Actualizar')