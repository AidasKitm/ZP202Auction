from wtforms import StringField,DateField, TextAreaField, SelectField,DecimalField, FileField, TimeField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired
from .category import categories

class AuctionForm(FlaskForm):

    title = StringField("Auction title:",validators=[InputRequired()])
    category = SelectField('Category', choices=categories)
    city = StringField("City", validators=[InputRequired()])
    minimum_price = DecimalField("Mnimum price",validators=[InputRequired("Please input price")])
    auction_image = FileField("Image", validators=[InputRequired("please upload a photo of auction item")])
    end_day = DateField("The day it's ending", validators=[DataRequired()])
    end_hour = TimeField("Time to end auction on", validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])