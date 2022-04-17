import json
from flask import send_from_directory, request, jsonify, Blueprint
import stripe

from models import User, db

api = Blueprint('api', __name__)

stripe.api_key = 'sk_test_A7KwHovQkSWcNug7jSvfro59'

@api.route('/')
def index():
    return send_from_directory('templates', "index.html")

@api.route('/checkout/complete')
def complete():
    return send_from_directory('templates', "index.html")

@api.route('/secret')
def secret():
    intent = stripe.PaymentIntent.create(
            amount=100,
            currency='eur',
            payment_method_types=["ideal"],
        )
    return jsonify({
            'clientSecret': intent['client_secret']
        })

@api.route('/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    print(data)
    user = User(email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({
            'ok': True
        })