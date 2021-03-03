from flask import render_template, session
from flask.views import MethodView



class Index(MethodView):
    def get(self):
        numbers = ["one", "two", "three"]
        word = "some words"
        context = {"some_list": numbers, "word1": word}
        return render_template("index.html", **context)
