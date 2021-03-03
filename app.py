from flask import Flask, render_template, request, redirect,session
from models.user import User
from models.auction import Auction
from models.offer import Offer
from models import db
from views.index import Index
from views.registration import Register
from views.login import Login
from config import Config
import os



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/index', view_func=Index.as_view('index'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))



if __name__ == '__main__':
    db.create_all(app=app)
    app.run()
