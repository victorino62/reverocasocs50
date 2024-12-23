from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    message = TextAreaField('Mensagem', validators=[DataRequired()])
    subscribe = BooleanField('Quero me inscrever na newsletter')
    submit = SubmitField('Enviar')

