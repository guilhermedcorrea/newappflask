from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields import SelectField,SubmitField
from ..extensions import db



class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class BarraBuscaPrecosgoogle(FlaskForm):
    pass

class Selectfiledform(FlaskForm):
    #VejaMais
    opcoes = SelectField('departamentos', choices=[])
    submit = SubmitField('Salvar')




