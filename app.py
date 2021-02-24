from flask import Flask, render_template, request, redirect
from forms import registration_form
from flask_sqlalchemy import SQLAlchemy
from models.user import User

import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/index')
def hello_world():
    numbers = ["one", "two", "three"]
    word = "some words"
    context = {"some_list": numbers, "word1": word}
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run()

# ORM (Object relational mapper) = SQL -> Mapping -> Python
# ORM = Python -> Mapping -> SQL

# MVT -> Model -> (View Templates)

# @app.route('/register', methods=["GET", "POST"])
# def register():
#     form = registration_form()
#     if request.method == "POST":
#         form = registration_form(request.form)
#         if form.validate_on_submit():
#             user = User(None, form.email, form.username, form.password)
#             database.session.add(user)
#             database.session.commit()
#
#         return redirect('/index')
#     return render_template("register.html", form=form)
