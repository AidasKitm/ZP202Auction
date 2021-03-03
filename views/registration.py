from flask import render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash
from flask.views import MethodView
from models.user import User
from models import db
from forms.registration_form import RegisterForm



class Register(MethodView):

    def get(self):
        if session.get('username'):
            return redirect(url_for('index'))

        registration_form = RegisterForm()
        return render_template('register.html', registration_form=registration_form, session=session.get('username'))

    def post(self):
        registration_form = RegisterForm()
        if registration_form.validate_on_submit():
            user = User(first_name=registration_form.first_name.data,
                        last_name=registration_form.last_name.data,
                        username=registration_form.username.data,
                        email=registration_form.email.data,
                        address=registration_form.address.data,
                        password=generate_password_hash(registration_form.password.data))
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('index'))




