from flask import redirect,url_for,session
from flask.views import MethodView


class LogOut(MethodView):
    def get(self):
        if session.get('username'):
            session.pop('username')
            return redirect(url_for('index'))