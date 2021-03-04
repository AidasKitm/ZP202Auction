from flask import redirect,url_for,render_template, session,request
from flask.views import MethodView
from forms.auction_form import AuctionForm
from models import db
from models.user import User
from models.auction import Auction
import os
from werkzeug.utils import secure_filename
import tinify


class CreateAuction(MethodView):
    def get(self):
        auction_form = AuctionForm()

        if session.get('username') is None:
            return redirect(url_for('login'))

        return render_template('createAuction.html', auction_form=auction_form)

    def post(self):
        auction_form = AuctionForm()

        if auction_form.validate_on_submit():
            user = User.query.filter_by(username=session.get('username')).first()

            file = auction_form.auction_image.data
            if file is not None:
                print(f"File name : {file}")
                file_name = user.username + "_" + file.filename
                print(f"File name : {file_name}")
                image_file = secure_filename(file_name)
                tinify.tinify.key = '41fZm74Q31R6hTWpMGM0ld9tRZ5HFfQ0'
                tinify.tinify.from_file(path=file).to_file(os.path.join("./static/auction_images", image_file))

            else:
                image_file = "default_auction.jpg"
            new_auction = Auction(title=auction_form.title.data,
                                  category=auction_form.category.data,
                                  city=auction_form.city.data,
                                  minimal_price=auction_form.minimum_price.data,
                                  image=image_file,
                                  end_day=auction_form.end_day.data,
                                  end_hour=auction_form.end_hour.data,
                                  description=auction_form.description.data,
                                  user_id=user.id)
            db.session.add(new_auction)
            db.session.commit()

            return redirect(url_for('auction', auction_id = Auction.query.order_by(Auction.id.desc()).first().id))
        else:
            return redirect(url_for('create_auction'))