from wtforms import StringField,DateField, TextAreaField, SelectField,DecimalField, TimeField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired
from .category import categories
from flask_wtf.file import FileField,FileRequired

class AuctionForm(FlaskForm):

    title = StringField("Auction title:",validators=[InputRequired()])
    category = SelectField('Category', choices=categories.values())
    city = StringField("City", validators=[InputRequired()])
    minimum_price = IntegerField("Mnimum price",validators=[InputRequired("Please input price")])
    auction_image = FileField("auction_image")
    end_day = DateField("The day it's ending", validators=[DataRequired()])
    end_hour = TimeField("Time to end auction on", validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])