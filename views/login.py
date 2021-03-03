from flask import redirect,url_for,render_template,session
from flask.views import MethodView
from werkzeug.security import check_password_hash
from forms.login_form import LoginForm
from models.user import User

class Login(MethodView):
    def get(self):
        if session.get('username'):
            return redirect(url_for('index'))
        form = LoginForm()
        return render_template("login.html", login_form= form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                return redirect(url_for('login'))
            elif check_password_hash(user.password, form.password.data):
                session['username'] = user.username
                print("Logged in")
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))