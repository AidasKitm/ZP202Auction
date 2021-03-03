import datetime
from flask import redirect, url_for, render_template, session, flash, request
from flask.views import MethodView
from models import db
from models.user import User
from models.offer import Offer
from models.auction import Auction


class Auctions(MethodView):

    def get(self, auction_id):
        auction = Auction.query.filter_by(id=auction_id).first()

        if auction is None:
            return redirect(url_for('index'))

        auction.views += 1
        db.session.commit()

        offers_in_auction = Offer.query.filter_by(
            auction_id=auction.id).order_by(Offer.price.desc()).limit(5).all()
        top_bidders = []
        if offers_in_auction is not None:
            for offer in offers_in_auction:
                top_bidders.append(User.query.filter_by(id=offer.user_id).first())

        return render_template("auctionListing.html",
                               auction=auction,
                               offers=offers_in_auction,
                               top_bidders=top_bidders)

    def post(self, auction_id):
        auction = Auction.query.filter_by(id=auction_id).first()

        try:
            new_price = request.form.get('price')
            if new_price < auction.minimal_price:
                raise ValueError
        except ValueError:
            flash("Price is lower than auctions minimal price")
            return redirect(url_for('auction', auction_id=auction.id))
        except Exception:
            flash("Something went wrong")
            return redirect(url_for('auction', auction_id=auction.id))

        user = User.query.filter_by(username=session.get('username')).first()
        new_offer = Offer(auction_id=auction.id,
                          user_id=user.id,
                          price=new_price)

        db.session.add(new_offer)
        db.session.commit()

        return redirect(url_for('auction', auction_id=auction.id))
