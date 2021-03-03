from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    first_name = StringField("Please input your first name", validators=[DataRequired()])
    last_name = StringField("Please input your last name", validators=[DataRequired()])
    email = EmailField("Please input your email", validators=[DataRequired(), Email()])
    address = StringField("Please input your address", validators=[DataRequired()])
    username = StringField("Please input your username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])