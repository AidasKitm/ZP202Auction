from flask import Flask
from flask_socketio import SocketIO, emit
from models.user import User
from models.auction import Auction
from models.offer import Offer
from models import db
from views.index import Index
from views.registration import Register
from views.login import Login
from views.logout import LogOut
from views.create_auction import CreateAuction
from views.auction_details import AuctionDetails
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
socketio = SocketIO(app=app)

with app.app_context():
    db.create_all(app=app)

app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/register', view_func=Register.as_view('register'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=LogOut.as_view('logout'))
app.add_url_rule('/create_auction', view_func=CreateAuction.as_view('create_auction'))
app.add_url_rule('/auction/<int:auction_id>', view_func=AuctionDetails.as_view('auction'))


@socketio.on('auction')
def auction(response):
    auction_listing = Auction.query.filter_by(id=response['auctionId']).first()
    offers = Offer.query.filter_by(
        auction_id=auction_listing.id).order_by(Offer.price.desc()).limit(5).all()
    highest_offer = []
    for offer in offers:
        user = User.query.filter_by(id=offer.user_id).first()
        single_offer = {'username': user.username, 'price': offer.price}
        highest_offer.append(single_offer)

    auction_response = {'auction_id': auction_listing.id,
                        'views':auction_listing.views,
                        'offers': highest_offer}
    emit('auctionResponse' + str(auction_response['auction_id']), auction_response, broadcast=True)

if __name__ == '__main__':
    socketio.run(app=app, host='localhost')
