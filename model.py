from wtforms import SubmitField, BooleanField, StringField, validators
from flask_wtf import FlaskForm


class RegForm(FlaskForm):
    nome = StringField('Nome completo', [validators.DataRequired()])
    precisa_assento = BooleanField('Não é criança de colo', [validators.DataRequired()])
    submit = SubmitField('Submit')