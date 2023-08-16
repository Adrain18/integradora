from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name_material = StringField('Nombre del material', validators=[DataRequired(), Length(min=4, max=25)])
    price = IntegerField('Precio', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
class ProfileForm(FlaskForm):
    name_material = StringField('Nombre del material', validators=[DataRequired(), Length(min=4, max=25)])
    price = IntegerField('Precio', validators=[DataRequired()])
    submit = SubmitField('Actualizar')