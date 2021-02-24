from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class registration_form(FlaskForm):
    email = StringField("Please input your email", validators=[DataRequired(), Email()])
    username = StringField("Please input your username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])
    submit = SubmitField("Submit")
